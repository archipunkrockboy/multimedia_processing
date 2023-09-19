"""
Задание 1. Установить библиотеку OpenCV.
"""
import cv2

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
            cv2.imshow('willem dafoe', frame)
            key = cv2.waitKey(20)
            if cv2.waitKey(5) == ord('q') or key == 27:
                break
        else:
            break

    video_capture.release()
    cv2.destroyAllWindows()


show_video()
"""
Задание 4 Записать видео из файла в другой файл.
"""


def read_and_write(path='media/willem dafoe.mp4'):

    video_capture = cv2.VideoCapture(path)
    video_writer = cv2.VideoWriter(
        'media/output.mp4',
        0,
        20.0,
        (int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
    )
    while video_capture.isOpened():
        is_successful, frame = video_capture.read()
        if is_successful:
            video_writer.write(frame)
            cv2.imshow('willem dafoe', frame)
            key = cv2.waitKey(20)
            if cv2.waitKey(5) == ord('q') or key == 27:
                break
        else:
            break

    video_capture.release()
    video_writer.release()
    cv2.destroyAllWindows()


read_and_write()
show_video('media/output.avi')


"""
Задание 5. Прочитать изображение, перевести его в формат HSV.
Вывести на экран два окна, в одном изображение в формате HSV, в другом –
исходное изображение.
"""



"""
Задание 6. Прочитать изображение с камеры. Вывести
в центре на экране Красный крест в формате, как на изображении. Указать
команды, которые позволяют это сделать. 
"""


"""
Задание 7. Отобразить информацию с вебкамеры,
записать видео в файл, продемонстрировать видео."""

"""
Задание 8. Залить крест одним из 3 цветов – красный,
зеленый, синий по следующему правилу: НА ОСНОВАНИИ ФОРМАТА RGB 
определить, центральный пиксель ближе к какому из цветов красный,
зеленый, синий и таким цветом заполнить крест.
"""


"""
Подключите телефон, подключитесь к его
камере, выведете на экран видео с камеры. Продемонстрировать процесс на
ноутбуке преподавателя и своем телефоне.
"""