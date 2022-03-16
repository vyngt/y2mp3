"""
-> exe
"""
import PyInstaller.__main__

PyInstaller.__main__.run(
    [
        "main.py",
        "--onefile",
        "--add-binary=ffmpeg/ffmpeg.exe;ffmpeg",
    ]
)
