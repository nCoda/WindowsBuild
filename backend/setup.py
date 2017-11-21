"""
This is a setup.py script that gets py2exe to create an executable file.

Usage:
    python setup.py py2exe
"""

from distutils.core import setup
import py2exe

APP = ['nCoda.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['fujian', 'abjad', 'lychee', 'shelfex'],
    }

setup(
    app=APP,
    data_files=['programs'],
    options={'py2exe': OPTIONS},
    setup_requires=['py2exe'],
)
