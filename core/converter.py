"""
Phase 2: Converting
"""
import functools
import itertools
import os
import subprocess
import threading
import time
from datetime import datetime
from typing import Callable

from core import settings
from utils.utils import Animation, discover, resource_path


def _video_src(src=settings.VIDEO_SOURCE):
    """
    Get videos source
    """
    return discover(src)


def get_output_path(output: str):
    """
    Check valid output path\n
    If not valid -> use the default\n
    Return path
    """
    if not os.path.exists(output):
        output = settings.AUDIO_OUTPUT
    return output


def run_ffmpeg(src: str, des: str, callback=Callable):
    subprocess.run(
        [resource_path(settings.FFMPEG), "-v", "quiet", "-stats", "-i", src, des],
        capture_output=True,
        check=True,
    )

    callback()


def write_audio(output: str):
    """
    Write to audio file
    """
    # Ensure available destination
    destination = get_output_path(output)
    if not os.path.exists(destination):
        os.mkdir(destination)

    animation = Animation()

    for src in _video_src():
        animation.reset()
        src_name = os.path.split(src)[1]
        title = src_name.split(".")[0]
        audio_file_name = title + settings.AUDIO_EXT
        des = os.path.join(destination, audio_file_name)
        _run_convert = functools.partial(run_ffmpeg, src, des, animation.end)
        t = threading.Thread(target=_run_convert)
        now = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
        t.start()
        print(f"{now} - Converting - {title} -  ", end="", flush=True)
        animation.run()
        t.join()


def convert_to_audio(output=settings.AUDIO_OUTPUT):
    """
    Convert video to audio
    """
    write_audio(output)
