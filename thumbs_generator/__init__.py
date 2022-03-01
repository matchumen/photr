import logging
from tqdm import tqdm
import os
import cv2
import rawpy
from utils import create_thumbnail, load_image, remove_accents


def generate_thumbnails(image_file_paths, input_dir, output_dir):
    cnt = 0

    for pth in tqdm(image_file_paths):
        # prepare directory tree
        output_pth_xsm = remove_accents(pth.replace(input_dir, f'{output_dir}\\thumbs_200'))
        output_pth_sm = remove_accents(pth.replace(input_dir, f'{output_dir}\\thumbs_500'))
        output_pth_lg = remove_accents(pth.replace(input_dir, f'{output_dir}\\thumbs_2000'))

        if os.path.exists(output_pth_sm):
            continue

        else:
            if not os.path.exists(os.path.dirname(output_pth_xsm)):
                os.makedirs(os.path.dirname(output_pth_xsm))

            if not os.path.exists(os.path.dirname(output_pth_sm)):
                os.makedirs(os.path.dirname(output_pth_sm))

            if not os.path.exists(os.path.dirname(output_pth_lg)):
                os.makedirs(os.path.dirname(output_pth_lg))

        # load images, create and save thumbnails
        try:
            img = load_image(pth)

            xsm_thumb = create_thumbnail(img, thumb_size=200)
            sm_thumb = create_thumbnail(img, thumb_size=500)
            lg_thumb = create_thumbnail(img, thumb_size=2000)

            cv2.imwrite(output_pth_xsm, xsm_thumb, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
            cv2.imwrite(output_pth_sm, sm_thumb, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            cv2.imwrite(output_pth_lg, lg_thumb, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

            cnt += 1

        except rawpy._rawpy.LibRawIOError as e:
            logging.debug(f'Failed to read {pth} with {e}.')

        except rawpy._rawpy.LibRawFileUnsupportedError as e:
            logging.debug(f'Unsupported file {pth} with {e}.')

        except Exception as e:
            logging.warning(f'Not able to process image {pth} with exception {e}.')

    logging.debug(f'{len(image_file_paths) - cnt} of files failed to process.')