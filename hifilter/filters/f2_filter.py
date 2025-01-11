#!/usr/bin/env python
# coding: utf-8

from PIL import ImageEnhance, ImageFile

from hifilter import HiFilter, filters

@filters
class F2Filter(HiFilter):
    """
    F2 风格以低对比度、柔和色调为主，适合静物照片
    """

    def __init__(self):
        super().__init__("f2")

    def effect(self) -> ImageFile:
        """
        spectific handle image process
        """
        # 降低对比度
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(0.8)  # 降低对比度

        # 降低饱和度
        enhancer = ImageEnhance.Color(self.img)
        self.img = enhancer.enhance(0.9)  # 降低饱和度

        # 增加亮度
        enhancer = ImageEnhance.Brightness(self.img)
        self.img = enhancer.enhance(1.1)  # 增加亮度


        return self.img
