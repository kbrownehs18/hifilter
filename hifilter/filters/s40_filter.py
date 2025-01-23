#!/usr/bin/env python
# coding: utf-8

from hifilter import AIFilter, filters


@filters
class S40Filter(AIFilter):
    """
    s40 Shinkai 新海诚风格漫画
    """

    def __init__(self):
        super().__init__("s40", "AnimeGANv3_Shinkai_40.onnx")
