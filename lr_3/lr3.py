import datetime
import time
from typing import Union, List

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


def convolution_operation():
    pass


def gauss_blur(img: cv2.mat_wrapper, kernel_size: int, standard_deviation: int) -> cv2.mat_wrapper:
    kernel = get_normalized_matrix(get_gauss_matrix(kernel_size, standard_deviation))
    x_start = y_start = kernel_size // 2
    copy_image = img.copy()
    for i in range(x_start, copy_image.shape[0] - x_start):
        for j in range(y_start, copy_image.shape[1] - y_start):
            val = 0
            for k in range(-(kernel_size // 2), kernel_size // 2 + 1):
                for l in range(-(kernel_size // 2), kernel_size // 2 + 1):
                    val += img[i + k][j + l] * kernel[k + (kernel_size // 2)][l + (kernel_size // 2)]
            copy_image[i][j] = val
    return copy_image


def main():
    img = cv2.imread("test2.jpg", cv2.IMREAD_GRAYSCALE)

    #  размер ядра фильтра и стандартное отклонение
    kernel_size = 5
    standard_deviation = 100

    img_blur_1 = gauss_blur(img, kernel_size, standard_deviation)

    cv2.imshow(str(kernel_size) + 'x' + str(kernel_size) + ' and deviation ' + str(standard_deviation), img_blur_1)
    cv2.waitKey(0)


main()
