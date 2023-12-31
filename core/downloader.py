"""
Phase 1: Downloading
"""
import functools
import os
import re
import threading
from datetime import datetime
from typing import Callable

from pytube import Playlist, YouTube
from pytube.streams import Stream

from core import settings
from utils.utils import Animation

VIDEO_PATTERN = r"^(https\:\/\/)?(www\.)?(youtube.com\/)watch\?v=.*"
PLAYLIST_PATTERN = r"^(https\:\/\/)?(www\.)?(youtube.com\/)playlist\?list=.*"


SAVE_TO = settings.VIDEO_SOURCE


def check_type(url: str):
    """
    Determine the type of valid url (Single or Playlist)
    """
    playlist = False

    match = re.search(VIDEO_PATTERN, url)
    if match:
        return (match.group(0), playlist)

    match = re.search(PLAYLIST_PATTERN, url)
    if match:
        playlist = True
        return (match.group(0), playlist)

    return None, None


def fetch_videos(url: str):
    """
    Fetch Videos
    """
    youtube = None
    valid_url, is_playlist = check_type(url)
    if valid_url:
        if is_playlist:
            youtube = Playlist(valid_url).videos
        else:
            youtube = [YouTube(valid_url)]

    return youtube


def make_temp_dir():
    """
    Make a temporary directory
    """
    if not os.path.exists(SAVE_TO):
        os.mkdir(SAVE_TO)


def _perform_download(stream: Stream, callback: Callable):
    stream.download(SAVE_TO)
    callback()


def download(url: str):
    """
    Download videos to /temp/
    """
    make_temp_dir()
    videos = fetch_videos(url)
    if videos:
        animation = Animation()
        for video in videos:
            stream = video.streams.get_audio_only()
            if stream:
                animation.reset()
                now = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
                perform = functools.partial(_perform_download, stream, animation.end)
                t = threading.Thread(target=perform)
                print(f"{now} - Downloading - {video.title} -  ", end="", flush=True)
                t.start()
                animation.run("Completed")
                t.join()
