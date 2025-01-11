#!/usr/bin/env python
# coding: utf-8

from PIL import ImageEnhance, ImageFile

from hifilter import HiFilter, filters

@filters
class C1Filter(HiFilter):
    """
    C1 风格以高饱和度、暖色调为主，适合风景照片
    """

    def __init__(self):
        super().__init__("c1")

    def effect(self) -> ImageFile:
        """
        spectific handle image process
        """
        # 增加饱和度
        enhancer = ImageEnhance.Color(self.img)
        self.img = enhancer.enhance(1.3)  # 增加饱和度

        # 增加亮度
        enhancer = ImageEnhance.Brightness(self.img)
        self.img = enhancer.enhance(1.1)  # 增加亮度

        # 增加对比度
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(1.2)  # 增加对比度

        return self.img
