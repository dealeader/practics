from PIL import Image
import numpy as np
import doctest


def get_image_brightness(rows, columns, image, mosaic_size) -> int:
    """

    :param rows: ширина
    :param columns: высота
    :param image: обрабатываемое изображение
    :param mosaic_size: размер мозаики
    :return: вычисляет и возвращает яркость изображения для дальнейшей обработки
    
    >>> img_array = np.array(Image.open('donut.jpg'))
    >>> rows = len(image)
    >>> columns = len(image[0])
    >>> get_image_brightness(rows, columns, image, 10)
    0
    """
    return int(np.sum(image[rows: rows + mosaic_size, columns: columns + mosaic_size]) // 3 // (mosaic_size ** 2))


def create_img_bit(rows, columns, mosaic_size, brightness, image) -> list:
    """

    :param rows: ширина
    :param columns: высота
    :param mosaic_size: размер мозаики
    :param brightness: яркость изображения
    :param image: обрабатываемое изображение
    :return: возвращает обработанный кусок изображения

    >>> image = np.array(Image.open('donut.jpg'))
    >>> rows = len(image)
    >>> columns = len(image[0])
    >>> brightness = get_image_brightness(rows, columns, image, 10)
    >>> create_img_bit(rows, columns, 10, brightness, image)
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
    image[rows: rows + mosaic_size, columns: columns + mosaic_size] = np.full(3, brightness)
    return image


def create_image(image, rows_length, columns_length, mosaic_size, grayscale):
    """

    :param image: обрабатываемое изображение
    :param rows_length: ширина
    :param columns_length: высота
    :param mosaic_size: размер мозаики
    :param grayscale: градация серого
    :return: возвращает обработанное изображение в черно-белом формате со сжатием при использовании параметра mosaic_size

    >>> image = np.array(Image.open('donut.jpg'))
    >>> rows = len(image)
    >>> columns = len(image[0])
    >>> create_image(image, rows, columns, 10, 50)
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
                           get_image_brightness(rows, columns, image, mosaic_size) // grayscale * grayscale,
                           image)
    return image


doctest.testmod()
img_array = np.array(Image.open(input('Введите имя изображения в директории: ')))
Image.fromarray(create_image(img_array,
                             len(img_array),
                             len(img_array[0]),
                             int(input('Введите размер мозаики: ')),
                             int(input('Введите шаг оттенка: ')))).save('res.jpg')
