#!/usr/bin/env python
# coding: utf-8

from PIL import Image, ImageEnhance, ImageFile

from hifilter import HiFilter, filters


@filters
class KK2Filter(HiFilter):
    """
    KK2 风格以高饱和度、暖色调为主，适合食物照片
    """

    def __init__(self):
        super().__init__("kk2")

    def effect(self) -> ImageFile:
        """
        spectific handle image process
        """
        # 增加饱和度
        enhancer = ImageEnhance.Color(self.img)
        self.img = enhancer.enhance(1.4)  # 增加饱和度

        # 增加亮度
        enhancer = ImageEnhance.Brightness(self.img)
        self.img = enhancer.enhance(1.2)  # 增加亮度

        # 增加暖色调（通过调整 RGB 通道）
        self.channels = self.split_channels()
        # rgba
        self.modify_channel(
            0, lambda c: self._modify_channel(c, 1.2)
        )
        self.modify_channel(
            2, lambda c: self._modify_channel(c, 0.8)
        )
        self.merge_channels()
        # r, g, b = self.img.split()
        # r = r.point(lambda x: x * 1.2)  # 增强红色通道
        # b = b.point(lambda x: x * 0.8)  # 减弱蓝色通道
        # self.img = Image.merge("RGB", (r, g, b))

        return self.img
