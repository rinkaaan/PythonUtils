import os
import sys


def is_pyinstaller():
    return getattr(sys, 'frozen', False)


def get_bundle_dir():
    if is_pyinstaller():
        # Frozen application
        bundle_dir = sys._MEIPASS
    else:
        # Development mode
        bundle_dir = os.getcwd()
    return bundle_dir


def get_path(filename):
    if is_pyinstaller():
        # Frozen application
        data_path = os.path.join(sys._MEIPASS, filename)
    else:
        # Development mode
        data_path = os.path.join(os.getcwd(), filename)
    return data_path
