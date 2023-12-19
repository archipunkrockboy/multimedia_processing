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
    kernel = np.ones((5, 5), np.uint8)
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

            # low = np.array([0, 110, 0])
            # high = np.array([15, 200, 255])

            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            filtered_frame = cv2.inRange(hsv_frame, low, high)
            erosion_frame = cv2.erode(filtered_frame, kernel)
            dilation_frame = cv2.dilate(filtered_frame, kernel)

            #opening_frame = cv2.dilate(erosion_frame, kernel)
            opening_frame = cv2.morphologyEx(filtered_frame, cv2.MORPH_OPEN, kernel)

            closing_frame = cv2.erode(dilation_frame, kernel)
            #closing_frame = cv2.morphologyEx(hsv_frame, cv2.MORPH_CLOSE, kernel)
            contours, _ = cv2.findContours(filtered_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            moments = cv2.moments(filtered_frame)
            area = moments['m00']
            print(moments)
            print(f'Площадь: {area}')
            if area > 0:
                if area > 0:
                    width = height = int(np.sqrt(area))
                    c_x = int(moments["m10"] / moments["m00"])
                    c_y = int(moments["m01"] / moments["m00"])

                    cv2.line(frame,
                             (c_x - (width // 32), c_y - (height // 32)),
                             (c_x + (width // 32), c_y + (height // 32)),
                             (0, 0, 0))
                    cv2.line(frame,
                             (c_x - (width // 32), c_y + (height // 32)),
                             (c_x + (width // 32), c_y - (height // 32)),
                             (0, 0, 0))

                    radius = (int)(abs((height // 32) * 1.43))
                    cv2.circle(frame,
                               (c_x, c_y),
                               radius,
                               (0, 0, 0))

            cv2.imshow('start', frame)
            #cv2.imshow('filtered_frame', filtered_frame)
            #cv2.imshow('result', closing_frame)
            # result = cv2.bitwise_and(frame, frame, mask=opening_frame)

            key = cv2.waitKey(1)
            if cv2.waitKey(5) == ord('q') or key == 27:
                break
        else:
            break
    video_capture.release()
    cv2.destroyAllWindows()


red_object_tracking()
