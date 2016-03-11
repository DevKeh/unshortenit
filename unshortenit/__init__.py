#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jeff Kehler'
__email__ = 'jeffrey.kehler@gmail.com'
__version__ = '0.2.3'

try:
    from .base import unshorten
except ImportError:
    """requests not installed yet, just ignoring it (setup.py command)"""
