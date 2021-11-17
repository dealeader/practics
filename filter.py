from PIL import Image
import numpy as np
import doctest

def get_image_brightness(rows, columns, img_array, mosaic_size) -> int:
    """

    :param rows:
    :param columns:
    :param img_array:
    :param mosaic_size:
    :return:
ss
    >>> img_array = np.array(Image.open('donut.jpg'))
    >>> rows = len(img_array)
    >>> columns = len(img_array[0])
    >>> get_image_brightness(rows, columns, img_array, 10)
    0
    """
    return int(np.sum(img_array[rows: rows + mosaic_size, columns: columns + mosaic_size]) // 3 // (mosaic_size ** 2))


def create_img_bit(rows, columns, mosaic_size, brightness, img_array) -> list:
    """

    :param rows:
    :param columns:
    :param mosaic_size:
    :param brightness:
    :param img_array:
    :return:

    >>> img_array = np.array(Image.open('donut.jpg'))
    >>> rows = len(img_array)
    >>> columns = len(img_array[0])
    >>> brightness = get_image_brightness(rows, columns, img_array, 10)
    >>> create_img_bit(rows, columns, 10, brightness, img_array)
    array([[[255, 255, 255],
            [255, 255, 255],
            [255, 255, 255],
            ...,
            [255, 255, 255],
            [255, 255, 255],
            [255, 255, 255]],
    <BLANKLINE>
           [[255, 255, 255],
            [255, 255, 255],
            [255, 255, 255],
            ...,
            [255, 255, 255],
            [255, 255, 255],
            [255, 255, 255]],
    <BLANKLINE>
           [[255, 255, 255],
            [255, 255, 255],
            [255, 255, 255],
            ...,
            [255, 255, 255],
            [255, 255, 255],
            [255, 255, 255]],
    <BLANKLINE>
           ...,
    <BLANKLINE>
           [[255, 255, 255],
            [255, 255, 255],
            [255, 255, 255],
            ...,
            [255, 255, 255],
            [255, 255, 255],
            [255, 255, 255]],
    <BLANKLINE>
           [[255, 255, 255],
            [255, 255, 255],
            [255, 255, 255],
            ...,
            [255, 255, 255],
            [255, 255, 255],
            [255, 255, 255]],
    <BLANKLINE>
           [[255, 255, 255],
            [255, 255, 255],
            [255, 255, 255],
            ...,
            [255, 255, 255],
            [255, 255, 255],
            [255, 255, 255]]], dtype=uint8)
    """
    img_array[rows: rows + mosaic_size, columns: columns + mosaic_size] = np.full(3, brightness)
    return img_array


def create_image(img_array, rows_length, columns_length, mosaic_size, grayscale):
    """

    :param img_array:
    :param rows_length:
    :param columns_length:
    :param mosaic_size:
    :param grayscale:
    :return:

    >>> img_array = np.array(Image.open('donut.jpg'))
    >>> rows = len(img_array)
    >>> columns = len(img_array[0])
    >>> create_image(img_array, rows, columns, 10, 50)
    array([[[250, 250, 250],
            [250, 250, 250],
            [250, 250, 250],
            ...,
            [250, 250, 250],
            [250, 250, 250],
            [250, 250, 250]],
    <BLANKLINE>
           [[250, 250, 250],
            [250, 250, 250],
            [250, 250, 250],
            ...,
            [250, 250, 250],
            [250, 250, 250],
            [250, 250, 250]],
    <BLANKLINE>
           [[250, 250, 250],
            [250, 250, 250],
            [250, 250, 250],
            ...,
            [250, 250, 250],
            [250, 250, 250],
            [250, 250, 250]],
    <BLANKLINE>
           ...,
    <BLANKLINE>
           [[250, 250, 250],
            [250, 250, 250],
            [250, 250, 250],
            ...,
            [250, 250, 250],
            [250, 250, 250],
            [250, 250, 250]],
    <BLANKLINE>
           [[250, 250, 250],
            [250, 250, 250],
            [250, 250, 250],
            ...,
            [250, 250, 250],
            [250, 250, 250],
            [250, 250, 250]],
    <BLANKLINE>
           [[250, 250, 250],
            [250, 250, 250],
            [250, 250, 250],
            ...,
            [250, 250, 250],
            [250, 250, 250],
            [250, 250, 250]]], dtype=uint8)
    """
    for rows in range(0, rows_length, mosaic_size):
        for columns in range(0, columns_length, mosaic_size):
            create_img_bit(rows, columns, mosaic_size,
                           get_image_brightness(rows, columns, img_array, mosaic_size) // grayscale * grayscale,
                           img_array)
    return img_array

doctest.testmod()
img_array = np.array(Image.open(input('Введите имя изображения в директории: ')))
Image.fromarray(create_image(img_array,
                             len(img_array),
                             len(img_array[0]),
                             int(input('Введите размер мозаики: ')),
                             int(input('Введите шаг оттенка: ')))).save('res.jpg')

