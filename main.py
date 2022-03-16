"""
Program: Youtube to MP3
"""
import argparse
from core import downloader, converter, utils


def download_and_convert(url: str, output: str):
    """
    Download video(s), then convert to MP3 format\n
    Finally, cleanup
    """
    downloader.download(url)
    converter.convert_to_audio(output)
    utils.cleanup()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="y2mp3",
        description="Ultimate tool for convert youtube to mp3 format",
        epilog="example: y2mp3 http://www.youtube.com/watch?v=xxxxxxx",
    )

    parser.add_argument(
        "u",
        type=str,
        help="String: youtube url\n eg: http://youtube.com/watch?v=xxxxxxx",
    )

    parser.add_argument(
        "-o",
        type=str,
        help="output: save to directory",
        default="./output/",
    )

    parser_args = parser.parse_args()
    u: str = parser_args.u
    o: str = parser_args.o
    download_and_convert(u, o)
