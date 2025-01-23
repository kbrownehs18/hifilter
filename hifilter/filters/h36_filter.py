#!/usr/bin/env python
# coding: utf-8

from hifilter import AIFilter, filters


@filters
class H36Filter(AIFilter):
    """
    h36 Hayao 宫崎骏风格漫画
    """

    def __init__(self):
        super().__init__("h36", "AnimeGANv3_Hayao_36.onnx")
