"""
Utils
"""
import itertools
import os
import sys
import time

from core import settings


class Animation:
    def __init__(self):
        self.done = False

    def reset(self):
        self.done = False

    def end(self):
        self.done = True

    def run(self, message: str = "Done"):
        for frame in itertools.cycle(["|", "/", "-", "\\"]):
            print("\b", frame, sep="", end="", flush=True)
            time.sleep(0.1)
            if self.done:
                print(f"\b{message}")
                break


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
        base_path = sys._MEIPASS  # type:ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
