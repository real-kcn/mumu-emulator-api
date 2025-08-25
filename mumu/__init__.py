#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mumu Android Emulator Python API

A Python wrapper for controlling Mumu Android emulators through MuMuManager.exe.
Provides comprehensive control over emulator operations including power management,
app installation, ADB operations, screen automation, and more.

Author: wlkjyy
Email: wlkjyy@vip.qq.com
"""

__version__ = "1.0.0"
__author__ = "wlkjyy"
__email__ = "wlkjyy@vip.qq.com"
__license__ = "MIT"

from .mumu import Mumu
from .constant import MacAddress, IMEI

# Public API
__all__ = ["Mumu", "MacAddress", "IMEI"]