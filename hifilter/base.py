#!/usr/bin/env python
# coding: utf-8

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

        return self.effect()

    def save(self, image_path: str = ""):
        """
        save filted image
        """
        if not self.img:
            raise ValueError("image is none")

        self.img.save(image_path)
