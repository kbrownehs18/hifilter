#!/usr/bin/env python
# coding: utf-8

from importlib.resources import path as resource_path

import cv2
import numpy as np
import onnxruntime as ort
from PIL import Image, ImageFile


def filters(cls):
    """
    decorator for filter
    """
    cls.__name__ = f"__hifilter__{cls.__name__}"
    return cls


class HiFilter(object):
    """
    base filter
    """

    def __init__(self, name: str):
        self.name = name
        self.img = None
        self.original_mode = None
        self.channels = None

    def effect(self) -> ImageFile:
        """
        subclass must realize this function
        """
        raise NotImplementedError("subclass must realize this function")

    def handle(self, image_file: str) -> ImageFile:
        """
        filter image
        """
        self.img = Image.open(image_file)
        self.original_mode = self.img.mode

        return self.effect()

    def save(self, image_path: str = ""):
        """
        save filted image
        """
        if not self.img:
            raise ValueError("image is none")

        self.img.save(image_path)

    def split_channels(self):
        """分离图像通道，支持多种模式"""
        if self.original_mode in ("RGB", "RGBA"):
            self.channels = self.img.split()
        elif self.original_mode == "L":
            # 灰度图像只有一个通道
            self.channels = (self.img,)
        elif self.original_mode == "CMYK":
            # 分离 CMYK 通道
            self.channels = self.img.split()
        elif self.original_mode == "P":
            # 调色板图像转换为 RGB 再处理
            self.img = self.img.convert("RGB")
            self.channels = self.img.split()
        else:
            # 其他模式统一转换为 RGBA 处理
            self.img = self.img.convert("RGBA")
            self.channels = self.img.split()

        return self.channels

    def merge_channels(self) -> ImageFile:
        """将通道重新合并为原始模式"""
        if self.original_mode == "RGB":
            self.img = Image.merge("RGB", self.channels[:3])
        elif self.original_mode == "RGBA":
            self.img = Image.merge("RGBA", self.channels[:4])
        elif self.original_mode == "L":
            self.img = self.channels[0]
        elif self.original_mode == "CMYK":
            self.img = Image.merge("CMYK", self.channels[:4])
        elif self.original_mode == "P":
            # 转换为 RGB 再合并
            self.img = Image.merge("RGB", self.channels[:3])
        else:
            # 默认合并为 RGBA
            self.img = Image.merge("RGBA", self.channels[:4])

        return self.img

    def modify_channel(self, channel_index, modify_function):
        """
        修改指定通道
        - channel_index: 通道索引（0 为第一个通道，依次递增）
        - modify_function: 用于修改通道的函数，接收单通道图像作为输入并返回修改后的图像
        """
        if 0 <= channel_index < len(self.channels):
            original_channel = self.channels[channel_index]
            self.channels = (
                self.channels[:channel_index]
                + (modify_function(original_channel),)
                + self.channels[channel_index + 1 :]
            )
        else:
            raise IndexError(
                f"Channel index {channel_index} out of range for mode {self.original_mode}"
            )

    def _modify_channel(self, channel, value: float):
        return channel.point(lambda x: x * value)


class AIFilter(HiFilter):
    """
    AI model filter
    """

    def __init__(self, name: str, model: str):
        """
        onnx 模型名称
        """
        super().__init__(name)
        self.model = model  # 模型名称
        self._size = None
        self._image = None

    def _process_image(self, img: np.ndarray, model_name):
        h, w = img.shape[:2]

        # resize image to multiple of 8s
        def to_8s(x):
            # If using the tiny model, the multiple should be 16 instead of 8.
            if "tiny" in model_name:
                return 256 if x < 256 else x - x % 16
            else:
                return 256 if x < 256 else x - x % 8

        img = cv2.resize(img, (to_8s(w), to_8s(h)))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32) / 127.5 - 1.0

        return img

    def effect(self):
        with resource_path("hifilter.filters.models", self.model) as model_path:
            session = ort.InferenceSession(
                str(model_path),
                providers=[
                    "CPUExecutionProvider",
                ],
            )
            x = session.get_inputs()[0].name

            img0 = cv2.imread(self.img).astype(np.float32)
            img = self._process_image(img0, self.model)
            img = np.expand_dims(img, axis=0)

            sample_image, shape = img, img0.shape
            handled_img = session.run(None, {x: sample_image})

            self._image = handled_img[0]
            self._size = (shape[1], shape[0])

    def handle(self, image_file: str) -> any:
        """
        filter image
        """
        self.img = image_file

        return self.effect()

    def save(self, image_path: str = ""):
        image = (np.squeeze(self._image) + 1.0) / 2 * 255
        image = np.clip(image, 0, 255).astype(np.uint8)
        image = cv2.resize(image, self._size)
        cv2.imwrite(image_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
