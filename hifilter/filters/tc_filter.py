#!/usr/bin/env python
# coding: utf-8

from hifilter import AIFilter, filters


@filters
class TCFilter(AIFilter):
    """
    tc tiny cute 风格
    """

    def __init__(self):
        super().__init__("tc", "AnimeGANv3_tiny_Cute.onnx")
