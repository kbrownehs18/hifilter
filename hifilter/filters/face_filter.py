#!/usr/bin/env python
# coding: utf-8

import os
import sys

import cv2
import numpy as np

np.int = np.int32

from hifilter import AIFilter, filters

_root_path = os.path.dirname(os.path.dirname(__file__))
_thirdparty_path = os.path.join(_root_path, "thirdparty")
_source_path = os.path.join(_thirdparty_path, "DCT-Net")
if _source_path not in sys.path:
    sys.path.append(_source_path)

from source.cartoonize import Cartoonizer


@filters
class FaceFilter(AIFilter):
    """
    DCT-NET 人像卡通化
    """

    def __init__(self):
        super().__init__("face", "cv_unet_person-image-cartoon_compound-models")

    def effect(self):
        """
        use model to process image
        """
        algo = Cartoonizer(
            dataroot=os.path.join(_thirdparty_path, "models", self.model)
        )
        img = cv2.imread(self.img)
        img0 = img.astype(np.float32)
        shape = img0.shape

        img = img[..., ::-1]
        self._image = algo.cartoonize(img)
        self._size = (shape[1], shape[0])

    def save(self, image_path: str = ""):
        image = cv2.resize(self._image, self._size)
        cv2.imwrite(image_path, image)
