# [ICANN 2024] MUFASA: Multi-view Fusion and Adaptation Network with Spatial Awareness for Radar Object Detection


## Abstract

In recent years, approaches based on radar object detection have made significant progress in autonomous driving systems due to their robustness under adverse weather compared to LiDAR. However, the sparsity of radar point clouds poses challenges in achieving precise object detection, highlighting the importance of effective and comprehensive feature extraction technologies. To address this challenge, this paper introduces a comprehensive feature extraction method for radar point clouds. This study first enhances the capability of detection networks by using a plug-and-play module, GeoSPA. It leverages the Lalonde features to explore local geometric patterns. Additionally, a distributed multi-view attention mechanism, DEMVA, is designed to integrate the shared information across the entire dataset with the global information of each individual frame. By employing the two modules, we present our method, MUFASA, which enhances object detection performance through improved feature extraction. The approach is evaluated on the VoD and TJ4DRaDSet datasets to demonstrate its effectiveness. In particular, we achieve state-of-the-art results among radar-based methods on the VoD dataset with the mAP of 50.24%

## Architecture
<img width="1049" height="356" alt="image" src="https://github.com/user-attachments/assets/c9ac25ce-98fb-4ac1-bf7c-c69f750b6391" />


## Result

<img width="1043" height="739" alt="image" src="https://github.com/user-attachments/assets/c05b687f-c34b-4b23-afc7-7ec36b1d7f98" />


## Installation

### Environment Setting
- The implementation is based on [OpenPCDet](https://github.com/open-mmlab/OpenPCDet).
- Please refer to this file ([Installation](https://github.com/open-mmlab/OpenPCDet/blob/master/docs/INSTALL.md)) to install the latest version of OpenPCDet.
- git clone  https://github.com/XiangyPeng/MUFASA.git
- cd MUFASA
- pip install -r requirement.txt

### Dataset Preparation

- Please refer to this file ([Dataset Preparation](https://github.com/tudelft-iv/view-of-delft-dataset)) to download and prepare VoD dataset. 
- Please refer to this file ([Dataset Preparation](https://github.com/TJRadarLab/TJ4DRadSet)) to download and prepare TJ4DRadSet dataset.


## Citation

If you find this work helpful for your research, please consider citing the following entry:

```
@inproceedings{peng2024mufasa,
  title={Mufasa: Multi-view fusion and adaptation network with spatial awareness for radar object detection},
  author={Peng, Xiangyuan and Tang, Miao and Sun, Huawei and Bierzynski, Kay and Servadei, Lorenzo and Wille, Robert},
  booktitle={International conference on artificial neural networks},
  pages={168--184},
  year={2024},
  organization={Springer}
}

```

## Acknowledgement

Many thanks to these excellent works and repos:

- [OpenPCDet](https://github.com/open-mmlab/OpenPCDet/tree/master)
- [View-of-Delft](https://github.com/tudelft-iv/view-of-delft-dataset)
- [TJ4DRadSet](https://github.com/TJRadarLab/TJ4DRadSet)

## Repository Delivery Notes

This repository has been cleaned for handover:
- Removed generated binaries (`*.so`) from version control.
- Removed local packaging metadata (`pcdet.egg-info`).
- Removed editor-specific launch settings (`tools/.vscode/launch.json`).
- Removed duplicate `copy` files that were not part of the production code path.
- Normalized file names and comments to avoid Chinese characters in tracked source files.
- Fixed two syntax issues in evaluation helper modules.
