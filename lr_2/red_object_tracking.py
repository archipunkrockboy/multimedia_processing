import cv2
import numpy as np


def on_change():
    pass


cv2.namedWindow('Trackbars')
cv2.createTrackbar('h_low', 'Trackbars', 0, 180, on_change)
cv2.createTrackbar('h_high', 'Trackbars', 0, 180, on_change)
cv2.createTrackbar('s_low', 'Trackbars', 0, 255, on_change)
cv2.createTrackbar('s_high', 'Trackbars', 0, 255, on_change)
cv2.createTrackbar('v_low', 'Trackbars', 0, 255, on_change)
cv2.createTrackbar('v_high', 'Trackbars', 0, 255, on_change)


def red_object_tracking():
    video_capture = cv2.VideoCapture(0)
    while video_capture.isOpened():

        is_successful, frame = video_capture.read(cv2.COLOR_BGR2HSV)
        if is_successful:

            h_low = cv2.getTrackbarPos('h_low', 'Trackbars')
            h_high = cv2.getTrackbarPos('h_high', 'Trackbars')
            s_low = cv2.getTrackbarPos('s_low', 'Trackbars')
            s_high = cv2.getTrackbarPos('s_high', 'Trackbars')
            v_low = cv2.getTrackbarPos('v_low', 'Trackbars')
            v_high = cv2.getTrackbarPos('v_high', 'Trackbars')

            low = np.array([h_low, s_low, v_low])
            high = np.array([h_high, s_high, v_high])

            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            filtered_frame = cv2.inRange(hsv_frame, low, high)
            cv2.imshow('red_object_tracking', filtered_frame)
            result = cv2.bitwise_and(frame, frame, mask=filtered_frame)
            cv2.imshow('result', result)

            key = cv2.waitKey(5)
            if cv2.waitKey(5) == ord('q') or key == 27:
                break
        else:
            break
    video_capture.release()
    cv2.destroyAllWindows()


red_object_tracking()
