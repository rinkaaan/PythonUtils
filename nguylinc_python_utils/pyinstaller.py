import os
import sys


def get_path(filename):
    if getattr(sys, 'frozen', False):
        # Frozen application
        data_path = os.path.join(sys._MEIPASS, filename)
    else:
        # Development mode
        data_path = os.path.join(os.getcwd(), filename)
    return data_path
