"""
Phase 2: Converting
"""
import os
import subprocess

from core import settings
from core.utils import discover, resource_path


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


def write_audio(output: str):
    """
    Write to audio file
    """
    # Ensure available destination
    destination = get_output_path(output)
    if not os.path.exists(destination):
        os.mkdir(destination)

    for src in _video_src():
        audio_file_name = os.path.split(src)[1].split(".")[0] + settings.AUDIO_EXT
        des = os.path.join(destination, audio_file_name)
        subprocess.run(
            [resource_path(settings.FFMPEG), "-v", "quiet", "-stats", "-i", src, des],
            check=True,
        )


def convert_to_audio(output=settings.AUDIO_OUTPUT):
    """
    Convert video to audio
    """
    write_audio(output)
