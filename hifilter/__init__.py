#!/usr/bin/env python
# coding: utf-8

import sys

from hifilter.base import *
from hifilter.filters import *

__all__ = ["HiFilter"]

filter_moduels = sys.modules.get("hifilter.filters")

all_filters = {
    name.replace('Filter', '').lower(): cls
    for name, cls in filter_moduels.__dict__.items()
    if isinstance(cls, type) and cls.__name__.startswith("__hifilter__")
}

__all__.append("all_filters")
