#!/usr/bin/env python3
# -*- coding:utf-8 -*-


with open("README.md", "r") as fh:
        long_description = fh.read()


from setuptools import  setup, find_packages

setup(
    name="gpsdistance",
    version="0.0.1",
    keywords=("distance"),
    description="GPS distance between 2D and 3D",
    long_description=long_description,
    license="MIT Licence",
    url="https://github.com/krnick/geodistance",
    author="SONG,JUN-WEI",
    author_email="sungboss2004@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["math"],
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License"
        ],
)
