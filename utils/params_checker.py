"""
Parameters Checker
"""
import os
import re

from core.downloader import VIDEO_PATTERN, PLAYLIST_PATTERN


class PChecker:
    """
    PChecker
    """

    def __init__(self, url: str, output: str):
        self.url = url
        self.output = output

    def is_valid_url(self):
        """
        :return True if url is valid, otherwise False
        """
        match = re.search(VIDEO_PATTERN, self.url)
        if match:
            return True

        match = re.search(PLAYLIST_PATTERN, self.url)
        if match:
            return True

        return False

    def is_valid_output(self):
        """
        Is path to save is exists?
        """
        return os.path.exists(self.output)

    def full_check(self):
        """
        Fully checking
        """
        return self.is_valid_url(), self.is_valid_output()
