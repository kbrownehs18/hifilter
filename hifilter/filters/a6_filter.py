#!/usr/bin/env python
# coding: utf-8

from PIL import ImageEnhance, ImageFile

from hifilter import HiFilter, filters

@filters
class A6Filter(HiFilter):
    """
    A6 风格以低饱和度、冷色调为主，适合冷色系照片
    """

    def __init__(self):
        super().__init__("a6")

    def effect(self) -> ImageFile:
        """
        spectific handle image process
        """
        # 降低饱和度
        enhancer = ImageEnhance.Color(self.img)
        self.img = enhancer.enhance(0.7)  # 减少饱和度

        # 降低亮度
        enhancer = ImageEnhance.Brightness(self.img)
        self.img = enhancer.enhance(0.9)  # 降低亮度

        # 增加对比度
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(1.2)  # 增加对比度

        return self.img
