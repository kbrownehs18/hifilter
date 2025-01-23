#!/usr/bin/env python
# coding: utf-8

from hifilter import AIFilter, filters


@filters
class P25Filter(AIFilter):
    """
    p25 素描风格
    """

    def __init__(self):
        super().__init__("p25", "AnimeGANv3_PortraitSketch_25.onnx")
