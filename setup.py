#!/usr/bin/env python
# coding: utf-8


from setuptools import find_packages, setup

setup(
    name="hifilter",
    version="0.2.4",
    author="last911",
    author_email="",
    description="image filter lib",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kbrownehs18/hifilter",
    packages=find_packages(include=["hifilter*", "source*"]),
    package_dir={"source": "hifilter/thirdparty/DCT-Net/source"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=["pillow", "opencv-python", "numpy", "onnx", "onnxruntime"],
    include_package_data=True,
    package_data={},
)
