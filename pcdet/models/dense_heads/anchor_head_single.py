import numpy as np
import torch.nn as nn

from .anchor_head_template import AnchorHeadTemplate


class AnchorHeadSingle(AnchorHeadTemplate):

    '''
    Args:
        model_cfg: AnchorHeadSingle
        input_channels: 384 
        num_class: 3
        class_names: ['Car','Pedestrian','Cyclist']
        grid_size: (432, 496, 1)
        point_cloud_range: (0, -39.68, -3, 69.12, 39.68, 1)
        predict_boxes_when_training: False
    '''

    def __init__(self, model_cfg, input_channels, num_class, class_names, grid_size, point_cloud_range,
                 predict_boxes_when_training=True, **kwargs):
        super().__init__(
            model_cfg=model_cfg, num_class=num_class, class_names=class_names, grid_size=grid_size, point_cloud_range=point_cloud_range,
            predict_boxes_when_training=predict_boxes_when_training
        )
        #generate_anchorsanchorsnum_anchors_per_location
        # 2(anchor)num_anchors_per_location[2, 2, 2,]-32anchor
        #6(anchor)
        self.num_anchors_per_location = sum(self.num_anchors_per_location)
        #6anchoranchor36*3
        self.conv_cls = nn.Conv2d(
            input_channels, self.num_anchors_per_location * self.num_class,
            kernel_size=1
        )
        #box1x1 conv_box:  Conv2d(384, 42, kernel_size=(1, 1), stride=(1, 1))
        #6anchoranchor7x, y, z, w, l, h, θ6*7
        self.conv_box = nn.Conv2d(
            input_channels, self.num_anchors_per_location * self.box_coder.code_size,
            kernel_size=1
        )
        #6anchoranchor2()6*2
        if self.model_cfg.get('USE_DIRECTION_CLASSIFIER', None) is not None:
            self.conv_dir_cls = nn.Conv2d(
                input_channels,
                self.num_anchors_per_location * self.model_cfg.NUM_DIR_BINS,
                kernel_size=1
            )
        else:
            self.conv_dir_cls = None
        self.init_weights()

    def init_weights(self):
        pi = 0.01
        nn.init.constant_(self.conv_cls.bias, -np.log((1 - pi) / pi))
        nn.init.normal_(self.conv_box.weight, mean=0, std=0.001)

    def forward(self, data_dict):
        spatial_features_2d = data_dict['spatial_features_2d'] # spatial_features_2d  batch_size, 384, 248, 216

        cls_preds = self.conv_cls(spatial_features_2d)
        #cls_predstorch.Size([batch_size, 18, 248, 216])
        #6anchoranchor36*3
        box_preds = self.conv_box(spatial_features_2d)
        #box_predstorch.Size([batch_size, 42, 248, 216])
        #6anchoranchor7x, y, z, w, l, h, θ6*7

        cls_preds = cls_preds.permute(0, 2, 3, 1).contiguous()  # [N, H, W, C] --> (batch_size, 200, 176, 18) 
        box_preds = box_preds.permute(0, 2, 3, 1).contiguous()  # [N, H, W, C] --> (batch_size ,200, 176, 42) 

        self.forward_ret_dict['cls_preds'] = cls_preds
        self.forward_ret_dict['box_preds'] = box_preds
        #
        #dir_cls_predstorch.Size([batch_size, 12, 248, 216])
        #6anchoranchor2()6*2
        if self.conv_dir_cls is not None:
            dir_cls_preds = self.conv_dir_cls(spatial_features_2d)
            dir_cls_preds = dir_cls_preds.permute(0, 2, 3, 1).contiguous()
            self.forward_ret_dict['dir_cls_preds'] = dir_cls_preds
        else:
            dir_cls_preds = None
        #GTloss
        if self.training:
            targets_dict = self.assign_targets(
                gt_boxes=data_dict['gt_boxes']
            )
            self.forward_ret_dict.update(targets_dict)
        #box
        if not self.training or self.predict_boxes_when_training:
            batch_cls_preds, batch_box_preds = self.generate_predicted_boxes(
                batch_size=data_dict['batch_size'],
                cls_preds=cls_preds, box_preds=box_preds, dir_cls_preds=dir_cls_preds
            )
            data_dict['batch_cls_preds'] = batch_cls_preds
            data_dict['batch_box_preds'] = batch_box_preds
            data_dict['cls_preds_normalized'] = False

        return data_dict
