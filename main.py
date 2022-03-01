from config import SUPPORTED_IMAGE_EXTENSIONS
from utils import load_file_paths
import logging
from thumbs_generator import generate_thumbnails


def main():
    logging.basicConfig(level=logging.DEBUG)

    # retrieve image paths

    input_dir = 'C:\\Users\\matchumen\\Desktop\\DCIM'
    output_dir = 'data'
    logging.debug(f'Scanning {input_dir}.')

    file_paths = load_file_paths(input_dir)
    logging.debug(f'{len(file_paths)} of files found.')

    image_file_paths = [f for f in file_paths if f.split(
        '.')[-1].lower() in SUPPORTED_IMAGE_EXTENSIONS]
    logging.debug(f'{len(image_file_paths)} of supported images found.')

    # generate thumbnails

    generate_thumbnails(image_file_paths, input_dir, output_dir)


if __name__ == '__main__':
    main()
