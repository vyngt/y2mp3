"""
-> exe
"""
import PyInstaller.__main__

PyInstaller.__main__.run(
    [
        "y2mp3.py",
        "--onefile",
        "--icon=raw_design/icon.ico",
        "--add-binary=ffmpeg/ffmpeg.exe;ffmpeg",
    ]
)
