# AOT (Associating Objects with Transformers for Video Object Segmentation) +cycle (Delving into the Cyclic Mechanism in Semi-supervised Video Object Segmentation) in PyTorch

## Requirements
   * Python3
   * pytorch >= 1.7.0 and torchvision
   * opencv-python
   * Pillow
   * Pytorch Correlation (Recommend to install from [source](https://github.com/ClementPinard/Pytorch-Correlation-extension) instead of using `pip`. **The project can also work without this moduel but will lose some efficiency of the short-term attention**.)

Optional:
   * scikit-image (if you want to run our **Demo**, please install)

## Model Zoo and Results
Pre-trained models, benckmark scores, and pre-computed results reproduced by this project can be found in [MODEL_ZOO.md](MODEL_ZOO.md).

## Getting Started
0. Prepare a valid environment follow the [requirements](#requirements).

1. Prepare datasets:

    Please follow the below instruction to prepare datasets in each corresponding folder.
    * **Static** 
    
        [datasets/Static](datasets/Static): pre-training dataset with static images. Guidance can be found in [AFB-URR](https://github.com/xmlyqing00/AFB-URR), which we referred to in the implementation of the pre-training.
    * **YouTube-VOS**

        A commonly-used large-scale VOS dataset.

        [datasets/YTB/2019](datasets/YTB/2019): version 2019, download [link](https://drive.google.com/drive/folders/1BWzrCWyPEmBEKm0lOHe5KLuBuQxUSwqz?usp=sharing). `train` is required for training. `valid` (6fps) and `valid_all_frames` (30fps, optional) are used for evaluation.

        [datasets/YTB/2018](datasets/YTB/2018): version 2018, download [link](https://drive.google.com/drive/folders/1bI5J1H3mxsIGo7Kp-pPZU8i6rnykOw7f?usp=sharing). Only `valid` (6fps) and `valid_all_frames` (30fps, optional) are required for this project and used for evaluation.

    * **DAVIS**

        A commonly-used small-scale VOS dataset.

        [datasets/DAVIS](datasets/DAVIS): [TrainVal](https://data.vision.ee.ethz.ch/csergi/share/davis/DAVIS-2017-trainval-480p.zip) (480p) contains both the training and validation split. [Test-Dev](https://data.vision.ee.ethz.ch/csergi/share/davis/DAVIS-2017-test-dev-480p.zip) (480p) contains the Test-dev split. The [full-resolution version](https://davischallenge.org/davis2017/code.html) is also supported for training and evaluation but not required.
2. Download models:
    Download https://drive.google.com/file/d/1jQ42MVhaX2oUJdYIdMeiAQXgmu3Kt5TJ/view?usp=sharing and put it into folder 'pretrain_models', Download https://drive.google.com/file/d/1o9JXgyDg7xBzlkAZARXSWPPVAqiHx15I/view?usp=sharing and put it into folder 'pretrain_models', Download https://drive.google.com/file/d/1wfuD4Q73E3N4fmiisYoLwKOUQexCxc_4/view?usp=sharing and put it into folder 'pretrain_models'
3. Evaluation
    * **cycle**   
    python tools/eval.py --exp_name aott_cycle --model aott --dataset davis2017 --split val --gpu_num 1 --ckpt_path pretrain_models/AOTT.pth --ensemble pretrain_models/AOTT_cycle.pth
    * **cycle+gc**   
    python tools/eval.py --exp_name aott_cycle_gc --model aott --dataset davis2017 --split val --gpu_num 1 --ckpt_path pretrain_models/AOTT.pth --ensemble pretrain_models/AOTT_cycle.pth --gc

## TODO
- [x] Training cycle

## Citations
Please consider citing the related paper(s) in your publications if it helps your research.
```
@article{yang2021aost,
  title={Associating Objects with Scalable Transformers for Video Object Segmentation},
  author={Yang, Zongxin and Miao, Jiaxu and Wang, Xiaohan and Wei, Yunchao and Yang, Yi},
  journal={arXiv preprint arXiv:2203.11442},
  year={2022}
}
@inproceedings{yang2021aot,
  title={Associating Objects with Transformers for Video Object Segmentation},
  author={Yang, Zongxin and Wei, Yunchao and Yang, Yi},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2021}
}
@article{li2020delving,
  title={Delving into the cyclic mechanism in semi-supervised video object segmentation},
  author={Li, Yuxi and Xu, Ning and Peng, Jinlong and See, John and Lin, Weiyao},
  journal={Advances in Neural Information Processing Systems},
  volume={33},
  pages={1218--1228},
  year={2020}
}
```

## License
This project is released under the BSD-3-Clause license. See [LICENSE](LICENSE) for additional details.
