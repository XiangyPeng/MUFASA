# MUFASA: Multi-view Fusion and Adaptation Network with Spatial Awareness for Radar Object Detection

![motivation](https://s2.loli.net/2025/05/14/oS8UYNJdnyxDKWu.png)

## Abstract

In recent years, approaches based on radar object detection have made significant progress in autonomous driving systems due to their robustness under adverse weather compared to LiDAR. However, the sparsity of radar point clouds poses challenges in achieving precise object detection, highlighting the importance of effective and comprehensive feature extraction technologies. To address this challenge, this paper introduces a comprehensive feature extraction method for radar point clouds. This study first enhances the capability of detection networks by using a plug-and-play module, GeoSPA. It leverages the Lalonde features to explore local geometric patterns. Additionally, a distributed multi-view attention mechanism, DEMVA, is designed to integrate the shared information across the entire dataset with the global information of each individual frame. By employing the two modules, we present our method, MUFASA, which enhances object detection performance through improved feature extraction. The approach is evaluated on the VoD and TJ4DRaDSet datasets to demonstrate its effectiveness. In particular, we achieve state-of-the-art results among radar-based methods on the VoD dataset with the mAP of 50.24%

## Architecture

![arch-1](https://s2.loli.net/2025/05/14/CNzcgHtKI6hD7wl.png)

## Result

![mre-1](https://s2.loli.net/2025/05/14/yahgYjicSIkmn5E.png)

## Getting Started

The implementation is based on [OpenPCDet](https://github.com/open-mmlab/OpenPCDet).

### Installation

Please refer to this file ([Installation](https://github.com/open-mmlab/OpenPCDet/blob/master/docs/INSTALL.md)) to install the latest version of OpenPCDet.

### Dataset Preparation

Please refer to this file ([Dataset Preparation](https://github.com/tudelft-iv/view-of-delft-dataset)) to prepare VoD dataset. 
Please refer to this file ([Dataset Preparation](https://github.com/TJRadarLab/TJ4DRadSet)) to prepare TJ4DRadSet dataset.


## BibTex

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
