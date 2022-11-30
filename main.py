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
    if not check:
        print('Fim...')
        break

    # Gray image
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(
        imgray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 25, 16)

    imgBlur = cv2.medianBlur(imgTh, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDil = cv2.dilate(imgBlur, kernel, iterations=1)
    nBOpenCar = 0

    for x, y, w, h in vagas:

        # Calcular a quantidade de pixels brancos nas vagas
        clipping = imgDil[y:y+h, x:x+w]
        nBWhitePx = cv2.countNonZero(clipping)

        # Numero na pexels brancos (impresso na tela)
        cv2.putText(img,
                    str(nBWhitePx),
                    (x+5, y+h-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 0, 255), 1, cv2.LINE_AA)

        # Se quantidade de pixels brancos for maior que 3000
        if nBWhitePx > 3000:
            cv2.rectangle(img, (x, y),
                          (x+w, y+h), (0, 0, 255), 3)

        else:
            cv2.rectangle(img, (x, y),
                          (x+w, y+h), (0, 255, 0), 3)
            nBOpenCar += 1

    # Cria um retango na tela com a quantidade de vagas disponiveis
    cv2.rectangle(img, (10, 0), (415, 60), (255, 0, 0), -1)
    cv2.putText(img,
                f'Vagas Livres: {nBOpenCar}/8',
                (15, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 10), 2, cv2.LINE_AA)

    cv2.imshow('Video', img)
    # cv2.imshow('Video TH', imgDil)
    cv2.waitKey(10)
