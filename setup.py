#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Read requirements
with open(os.path.join(this_directory, "requirements.txt"), encoding="utf-8") as f:
    requirements = []
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            # Handle duplicate adbutils entries by taking the latest version
            if line.startswith("adbutils=="):
                # Remove any existing adbutils entry
                requirements = [req for req in requirements if not req.startswith("adbutils")]
                requirements.append(line)
            else:
                requirements.append(line)

setup(
    name="mumu-emulator-api",
    version="1.0.0",
    author="wlkjyy",
    author_email="wlkjyy@vip.qq.com",
    description="A Python wrapper for controlling Mumu Android emulators through MuMuManager.exe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wlkjyy/mumu-python-api",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Emulators",
        "Topic :: Software Development :: Testing",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "gui": ["opencv-python"],
        "dev": ["pytest", "black", "flake8"],
    },
    keywords="android emulator mumu automation testing adb",
    project_urls={
        "Bug Reports": "https://github.com/wlkjyy/mumu-python-api/issues",
        "Source": "https://github.com/wlkjyy/mumu-python-api",
    },
    include_package_data=True,
    zip_safe=False,
)