#!/usr/bin/env python
# coding: utf-8

import os
import unittest

from hifilter import all_filters


class TestFilter(unittest.TestCase):
    """
    test filter
    """

    def test_face(self):
        """
        test face
        """
        root_path = os.path.dirname(os.path.abspath(__file__))
        k = "face"
        f = all_filters[k]()
        f.handle(f"{root_path}/tmp/starcraft.png")
        f.save(f"{root_path}/tmp/starcraft_{k}.png")


if __name__ == "__main__":
    unittest.main()
