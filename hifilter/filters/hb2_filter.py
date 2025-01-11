#!/usr/bin/env python
# coding: utf-8

from PIL import Image, ImageEnhance, ImageFile

from hifilter import HiFilter, filters


@filters
class HB2Filter(HiFilter):
    """
    HB2 风格以高对比度、冷色调为主，适合街拍照片
    """

    def __init__(self):
        super().__init__("hb2")

    def effect(self) -> ImageFile:
        """
        spectific handle image process
        """
        # 增加对比度
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(1.3)  # 增加对比度

        # 降低饱和度
        enhancer = ImageEnhance.Color(self.img)
        self.img = enhancer.enhance(0.8)  # 降低饱和度

        # 增加冷色调（通过调整 RGB 通道）
        r, g, b = self.img.split()
        b = b.point(lambda x: x * 1.1)  # 增强蓝色通道
        r = r.point(lambda x: x * 0.9)  # 减弱红色通道
        self.img = Image.merge("RGB", (r, g, b))

        return self.img
