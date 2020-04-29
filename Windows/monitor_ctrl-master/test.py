#!python3
# coding = utf-8

import os
import sys
import logging
import argparse
import vcp

try:
    import tkinter
    from tkinter import ttk
    TK_IMPORTED = True
except ImportError:
    TK_IMPORTED = False


__VERSION__ = '1.0'
__APP_NAME__ = 'monitor_ctrl'
__LOGGING_FORMAT = "%(levelname)s:[%(filename)s:%(lineno)s-%(funcName)s()] %(message)s"

DEFAULT_LOGFILE_PATH = os.path.join(os.environ.get('TEMP', './'), __APP_NAME__, 'log.txt')
_LOGGER = logging.getLogger(__name__)

print(" -----start------  ")

print(__VERSION__)
print(__APP_NAME__)
print(__LOGGING_FORMAT)
print(DEFAULT_LOGFILE_PATH)
print(_LOGGER)
print(' -----------end------  ')

