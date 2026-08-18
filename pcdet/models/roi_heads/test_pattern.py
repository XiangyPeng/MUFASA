import torch
import torch.nn.functional as F
from torch.autograd import Function

class ComputeLFeaturesFunction(Function):
   @staticmethod
   def forward(ctx, points, radius):
       # BallTree
       tree = BallTree(points)
       idx = tree.query_radius(points, r=radius)
       L1_arr, L2_arr, L3_arr = [], [], []

       for i in range(len(points)):
           neighbors = points[idx[i]]
           # Covariance matrix
           if neighbors.shape[0] < 2:
               # Handle the insufficient neighbors case
               L1_arr.append(0)  # or some other default value
               L2_arr.append(0)  # or some other default value
               L3_arr.append(0)  # or some other default value
               continue  # skip to next iteration
           cov_matrix = torch.cov(neighbors, rowvar=False, bias=True)
           # Eigenvalues
           d1, d2, d3 = torch.sorted(torch.eigvalsh(cov_matrix), dim=-1, descending=True)
           sum_d = d1 + d2 + d3
           # Normalize eigenvalues
           d1 /= sum_d
           d2 /= sum_d
           d3 /= sum_d
           L1 = d1
           L2 = d1 - d2
           L3 = d2 - d3
           L1_arr.append(L1)
           L2_arr.append(L2)
           L3_arr.append(L3)

       ctx.save_for_backward(points, idx, radius)

       return torch.tensor(L1_arr), torch.tensor(L2_arr), torch.tensor(L3_arr)

   @staticmethod
   def backward(ctx, grad_L1, grad_L2, grad_L3):
       points, idx, radius = ctx.saved_tensors
       grad_points = torch.zeros_like(points)

       # 
       for i in range(len(points)):
           neighbors = points[idx[i]]
           if neighbors.shape[0] < 2:
               continue

           # 
           cov_matrix_grad = torch.zeros_like(cov_matrix)
           d1, d2, d3 = torch.sorted(torch.eigvalsh(cov_matrix), dim=-1, descending=True)
           sum_d = d1 + d2 + d3
           d1_grad = torch.sum(grad_L1[i] * (2 * d1 / sum_d - 1))
           d2_grad = torch.sum(grad_L2[i] * (2 * (d1 - d2) / sum_d - 1))
           d3_grad = torch.sum(grad_L3[i] * (2 * (d2 - d3) / sum_d - 1))

           # 
           grad_points[idx[i]] += torch.matmul(neighbors.t(), cov_matrix_grad)

       return grad_points, None

def compute_L_features_pytorch(points, radius):
   return ComputeLFeaturesFunction.apply(points, radius)