import os
import cv2
import unicodedata
import numpy as np
import rawpy


def create_thumbnail(img, thumb_size=1000):

    if img.shape[0] > thumb_size or img.shape[1] > thumb_size:
        if img.shape[0] == max(img.shape):
            new_dim = (
                int(img.shape[1] // (img.shape[0] / thumb_size)), thumb_size)

        if img.shape[1] == max(img.shape):
            new_dim = (thumb_size, int(
                img.shape[0] // (img.shape[1] / thumb_size)))

        img = cv2.resize(img, new_dim)

    return img


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def load_file_paths(input_dir):
    file_paths = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            fpth = os.path.join(root, file)
            file_paths.append(fpth)

    return file_paths


def load_image(pth):
    try:
        img = cv2.imdecode(np.fromfile(pth, dtype=np.uint8),
                        cv2.IMREAD_UNCHANGED)

        if img is None:
            with rawpy.imread(pth) as raw:
                img = raw.postprocess()

        if pth.lower().endswith('.arw'):
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        return img

    except Exception as e:
        raise Exception(f'Failed to read image {pth} with exception {e}')

