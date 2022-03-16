"""
Phase 1: Downloading
"""
import re
import os
from pytube import YouTube, Playlist
from core import settings


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
    valid_url, isplaylist = check_type(url)
    if valid_url:
        if isplaylist:
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


def download(url: str):
    """
    Download videos to /temp/
    """
    make_temp_dir()
    videos = fetch_videos(url)
    if videos:
        for video in videos:
            stream = video.streams.get_audio_only()
            if stream:
                stream.download(SAVE_TO)
                print(f"{video.title}: Dowloaded")
