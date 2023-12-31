"""
Program: Youtube to MP3
"""
import argparse

from core import converter, downloader
from core.logger import get_logger
from utils import utils

_logger = get_logger("Y2MP3")


def download_and_convert(url: str, output: str):
    """
    Download video(s), then convert to MP3 format\n
    Finally, cleanup
    """
    _logger.info("Starting")

    _logger.info("Phase 1/3: Downloading")
    downloader.download(url)
    _logger.info("Phase 1/3: Done")

    _logger.info("Phase 2/3: Converting")
    converter.convert_to_audio(output)
    _logger.info("Phase 2/3: Done")

    _logger.info("Phase 3/3: Cleaning")
    utils.cleanup()
    _logger.info("Phase 3/3: Done")

    _logger.info("Completed, Have fun ^ _ ^!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="y2mp3",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Ultimate tool for convert youtube to mp3 format",
        epilog="""
        example:
            y2mp3 https://www.youtube.com/watch?v=xxxxxxx
            y2mp3 "https://www.youtube.com/watch?v=xxxxxxx" -o "path/to/save"
            y2mp3 "https://www.youtube.com/playlist?list=abcxxxxxxxxyyyyyzzzzz"


        Have fun ^^
        """,
    )

    parser.add_argument(
        "u",
        type=str,
        help="String: youtube url\n eg: http://youtube.com/watch?v=xxxxxxx",
    )

    parser.add_argument(
        "-o",
        type=str,
        help="output: path to save",
        default="./output/",
    )

    parser_args = parser.parse_args()
    u: str = parser_args.u
    o: str = parser_args.o

    download_and_convert(u, o)
