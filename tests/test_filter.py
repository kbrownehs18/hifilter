#!/usr/bin/env python
# coding: utf-8

import os
import unittest

from hifilter import all_filters


class TestFilter(unittest.TestCase):
    """
    test filter
    """

    def test_init(self):
        """
        test init
        """
        print(all_filters)

    def test_filters(self):
        """
        all filters
        """
        root_path = os.path.dirname(os.path.abspath(__file__))
        for k in all_filters:
            f = all_filters[k]()
            f.handle(f"{root_path}/tmp/starcraft.png")
            f.save(f"{root_path}/tmp/starcraft_{k}.png")


if __name__ == "__main__":
    unittest.main()
