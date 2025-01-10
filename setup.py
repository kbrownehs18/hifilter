#!/usr/bin/env python
# coding: utf-8

from setuptools import find_packages, setup

setup(
    name="hifilter",
    version="0.1.0",
    author="last911",
    author_email="",
    description="image filter lib",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kbrownehs18/hifilter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=["pillow"],
)
