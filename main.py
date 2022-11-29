import cv2
import numpy as np

vagas1 = [1, 89, 108, 213]
vagas2 = [115, 87, 152, 211]
vagas3 = [289, 89, 138, 212]
vagas4 = [439, 87, 135, 212]
vagas5 = [591, 90, 132, 206]
vagas6 = [738, 93, 139, 204]
vagas7 = [881, 93, 138, 201]
vagas8 = [1027, 94, 147, 202]

vagas = [vagas1, vagas2, vagas3, vagas4, vagas5, vagas6, vagas7, vagas8]


# Video Capture
video = cv2.VideoCapture('video.mp4')

while True:
    check, img = video.read()

    # Gray image
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(
        imgray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    if not check:
        print('Fim...')
        break

    for x, y, w, h in vagas:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', img)
    cv2.imshow('Video TH', imgTh)
    cv2.waitKey(10)
