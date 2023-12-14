import os
import socket
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


def get_free_port():
    """Finds a free port on the current host."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Set SO_REUSEADDR to avoid "Address already in use" errors.
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to port 0, which tells the OS to assign a free port.
        sock.bind(('', 0))
        # Return the assigned port number.
        free_port = sock.getsockname()[1]
        return free_port
