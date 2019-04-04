#!/usr/bin/env python3
# -*- coding:utf-8 -*-


with open("README.md", "r") as fh:
        long_description = fh.read()


from setuptools import  setup, find_packages

setup(
    name="gpsdistance",
    version="0.0.5",
    keywords=("distance","GPS"),
    description="GPS distance between 2D and 3D",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",
    url="https://github.com/krnick/gpsdistance",
    author="SONG,JUN-WEI",
    author_email="sungboss2004@gmail.com",
    packages=find_packages(),
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
)
