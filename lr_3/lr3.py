import datetime
from typing import Union

import cv2
import numpy as np


def gaussian_function(x: int, y: int, omega: int, a: int, b: int) -> np.float64:
    """Функция для получения значений функции Гаусса для двумерной случайной величины"""
    return 1 / (np.pi * (2 * omega**2)) * np.exp(-((x - a) ** 2 + (y - b) ** 2) / (2 * omega**2))


def get_gauss_matrix(kernel_size: int, standard_deviation: Union[int, float]) -> list[list[float]]:
    """Функция для получения ядра свёртки"""
    a = b = (kernel_size + 1) // 2
    return [[gaussian_function(i, j, standard_deviation, a, b) for j in range(kernel_size)] for i in range(kernel_size)]


def get_normalized_matrix(matrix: list[list[Union[int, float]]]) -> list[list[Union[int, float]]]:
    """Функция для нормализации матрицы"""

    sum_of_elements = sum(map(sum, matrix))
    return list(map(lambda row: list(map(lambda elem: elem / sum_of_elements, row)), matrix))


def gauss_blur(img: cv2.mat_wrapper, kernel_size: int, standard_deviation: int) -> cv2.mat_wrapper:
    kernel = np.array(get_normalized_matrix(get_gauss_matrix(kernel_size, standard_deviation)))
    x_start = y_start = kernel_size // 2
    copy_image = img.copy()
    for i in range(x_start, copy_image.shape[0] - x_start):
        for j in range(y_start, copy_image.shape[1] - y_start):
            val = 0
            for k in range(-(kernel_size // 2), kernel_size // 2 + 1):
                for l in range(-(kernel_size // 2), kernel_size // 2 + 1):
                    val += img[i + k, j + l] * kernel[k + (kernel_size // 2), l + (kernel_size // 2)]
            copy_image[i][j] = val
    return copy_image


def main():
    # Задание 1: построить матрицу Гаусса
    # gauss_matrix_5_100 = get_gauss_matrix(5, 100)
    # gauss_matrix_7_50 = get_gauss_matrix(7, 50)

    # Задание 2: нормировать матрицу
    # norm_gauss_5_100 = get_normalized_matrix(gauss_matrix_5_100)
    # norm_gauss_7_50 = get_normalized_matrix(gauss_matrix_7_50)

    img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow(f'image', img)
    # Задание 3-4: реализовать фильтр гаусса средствами языка python

    img1 = gauss_blur(img, 5, 100)
    cv2.imshow(f'my gauss blur with kernel 5x5 and SD 100', img1)

    img2 = gauss_blur(img, 7, 50)
    cv2.imshow(f'my gauss blur with kernel 7x7 and SD 50', img2)

    # # Задание 5: реализовать фильтр гаусса методами cv2

    img3 = cv2.GaussianBlur(img, (5, 5), 5)
    cv2.imshow(f'cv2 gauss blur with kernel 5x5 and SD 5', img3)

    # # Задание 6: сравнить
    cv2.waitKey(0)


main()
