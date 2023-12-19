"""
Задание 1. Установить библиотеку OpenCV.
"""
import cv2
import numpy as np

"""
Задание 2. Вывести на экран изображение. Протестировать три
возможных расширения, три различных флага для создания окна и три
различных флага для чтения изображения. 
"""

# image = cv2.imread('media/monkey.bmp', cv2.IMREAD_UNCHANGED)
# cv2.namedWindow('normal', cv2.WINDOW_NORMAL)
# cv2.imshow('normal', image)
#
# image = cv2.imread('media/monkeys.png', cv2.IMREAD_ANYDEPTH)
# cv2.namedWindow('test', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('test', image)
#
# image = cv2.imread('media/monkeys.jpg', cv2.IMREAD_REDUCED_COLOR_4)
# cv2.namedWindow('autosize', cv2.WINDOW_FULLSCREEN)
# cv2.imshow('autosize', image)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
Задание 3. Отобразить видео в окне. Рассмотреть методы класса
VideoCapture и попробовать отображать видео в разных форматах, в частности
размеры и цветовая гамма.
"""


def show_video(path='media/willem dafoe'):
    video_capture = cv2.VideoCapture(path)

    if not video_capture.isOpened():
        raise "Ошибка открытия видео"

    while video_capture.isOpened():
        is_successful, frame = video_capture.read()
        if is_successful:

            frame = cv2.cvtColor(cv2.resize(frame, (300, 700)), cv2.COLOR_RGB2GRAY)

            cv2.imshow('willem dafoe', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            break

    video_capture.release()
    cv2.destroyAllWindows()


# show_video(path='media/willem dafoe.mp4')
"""
Задание 4 Записать видео из файла в другой файл.
"""


def read_and_write(path='media/willem dafoe.mp4'):
    video_capture = cv2.VideoCapture(path)
    w = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(f'output/task_4.mp4', fourcc, 25, (w, h))

    while video_capture.isOpened():
        is_successful, frame = video_capture.read()
        if is_successful:
            cv2.imshow('willem dafoe', frame)
            video_writer.write(frame)
            key = cv2.waitKey(20)
            if cv2.waitKey(5) == ord('q') or key == 27:
                break
        else:
            break

    video_capture.release()
    video_writer.release()
    cv2.destroyAllWindows()


# read_and_write()
# show_video('media/output.mp4')


"""
Задание 5. Прочитать изображение, перевести его в формат HSV.
Вывести на экран два окна, в одном изображение в формате HSV, в другом –
исходное изображение.
"""


def convert_to_hsv(path='media/monkeys.jpg'):
    image = cv2.imread(path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow('image', image)
    cv2.imshow('hsv_image', hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# convert_to_hsv()
"""
Задание 6. Прочитать изображение с камеры. Вывести
в центре на экране Красный крест в формате, как на изображении. Указать
команды, которые позволяют это сделать. 
"""


def draw_cross(video_capture, frame, color, filled=0):
    frame_width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

    cv2.rectangle(
        frame,
        (int(frame_width // 2 - 10), 100),
        (int(frame_width // 2 + 10), int(frame_height - 100)),
        color,
        filled,
    )
    cv2.rectangle(
        frame,
        (200, int(frame_height // 2 - 10)),
        (int(frame_width - 200), int(frame_height // 2 + 10)),
        color,
        filled
    )


def draw_pentagram(video_capture, frame, color):
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    center_x, center_y = width // 2, height // 2
    radius = 120
    pentagon_points = []
    for i in range(5):
        x = center_x + int(radius * np.cos(2 * np.pi * i / 5))
        y = center_y + int(radius * np.sin(2 * np.pi * i / 5))
        pentagon_points.append((x, y))

    for i in range(5):
        cv2.line(frame, pentagon_points[i], pentagon_points[(i + 2) % 5], color, 4)

    cv2.circle(frame, (center_x, center_y), 120, color, 4)


def red_cross():
    video_capture = cv2.VideoCapture(0)
    while video_capture.isOpened():
        is_successful, frame = video_capture.read()
        if is_successful:
            draw_cross(video_capture, frame, (0, 0, 255), 4)
            cv2.imshow('red_cross', frame)
            key = cv2.waitKey(10)
            if cv2.waitKey(5) == ord('q') or key == 27:
                break
        else:
            break
    video_capture.release()
    cv2.destroyAllWindows()


# red_cross()
"""
Задание 7. Отобразить информацию с вебкамеры,
записать видео в файл, продемонстрировать видео."""


def read_web_and_write():
    video_capture = cv2.VideoCapture(0)
    w = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(f'output/task_7.mp4', fourcc, 25, (w, h))

    while video_capture.isOpened():
        is_successful, frame = video_capture.read()
        if is_successful:
            cv2.imshow('willem dafoe', frame)
            video_writer.write(frame)
            key = cv2.waitKey(20)
            if cv2.waitKey(5) == ord('q') or key == 27:
                break
        else:
            break

    video_capture.release()
    video_writer.release()
    cv2.destroyAllWindows()


#read_web_and_write()

"""
Задание 8. Залить крест одним из 3 цветов – красный,
зеленый, синий по следующему правилу: НА ОСНОВАНИИ ФОРМАТА RGB 
определить, центральный пиксель ближе к какому из цветов красный,
зеленый, синий и таким цветом заполнить крест.
"""


def fill_central_pixel():
    video_capture = cv2.VideoCapture(0)
    while video_capture.isOpened():
        is_successful, frame = video_capture.read()

        if is_successful:
            frame_width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
            frame_height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
            central_pixel = frame[
                            int(frame_height // 2):int(frame_height // 2 + 1),
                            int(frame_width // 2):int(frame_width // 2 + 1)
                            ][0][0]
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            central_pixel_hsv = hsv[int(frame_height // 2), int(frame_width // 2)]
            central_pixel_hsv_hue_value = central_pixel_hsv[0]
            if central_pixel_hsv_hue_value < 30 or central_pixel_hsv_hue_value > 150:
                central_pixel_color = (0, 0, 255)
            elif 30 <= central_pixel_hsv_hue_value <= 90:
                central_pixel_color = (0, 255, 0)
            else:
                central_pixel_color = (255, 0, 0)
            # central_pixel_color = (255, 0, 0) if max(central_pixel) == central_pixel[0] else (
            #     (0, 255, 0) if max(central_pixel) == central_pixel[1] else (
            #         (0, 0, 255) if max(central_pixel) == central_pixel[2] else None
            #     )
            # )

            frame[
                int(frame_height // 2 - 3):int(frame_height // 2 + 2),
                int(frame_width // 2 - 3):int(frame_width // 2 + 2)
            ] = central_pixel_color
            #draw_cross(video_capture, frame, central_pixel_color, cv2.FILLED)
            draw_pentagram(video_capture, frame, central_pixel_color)
            cv2.imshow('red_cross', frame)
            key = cv2.waitKey(10)
            if cv2.waitKey(5) == ord('q') or key == 27:
                break
        else:
            break
    video_capture.release()
    cv2.destroyAllWindows()


fill_central_pixel()
