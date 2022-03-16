"""
Utils
"""
import os
import sys
from core import settings


def discover(directory: str):
    """
    Get absolute path of each file in the directory
    """
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            absolute = os.path.abspath(os.path.join(dirpath, filename))
            yield absolute


def cleanup(directory=settings.VIDEO_SOURCE):
    """
    Cleanup
    """
    for filename in discover(directory):
        os.remove(filename)
    os.rmdir(directory)


def resource_path(relative_path: str):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
