"""
This is a setup.py script that gets py2exe to create an executable file.

Usage:
    python setup.py py2exe
"""

from distutils.core import setup
import py2exe

setup(console=['nCoda.py'])
