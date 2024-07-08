# -*- coding: utf-8 -*-

##Espacios de color

import cv2 ## importamos la libreria opencv

# img = cv2.imread("1.jpeg") ## leemos la imagen original

# B, G, R = cv2.split(img) ## separamos la imagen en sus 3 canales de color B G R

# img2 = cv2.merge((B,G,R)) ## unimos los 3 canales y guardamos la imagen resultante en img2

# cv2.namedWindow("RGB", cv2.WINDOW_NORMAL) ## CREAR ventana normal redimensionable
# cv2.namedWindow("B", cv2.WINDOW_NORMAL)
# cv2.namedWindow("G", cv2.WINDOW_NORMAL)
# cv2.namedWindow("R", cv2.WINDOW_NORMAL)
# cv2.namedWindow("BGR", cv2.WINDOW_NORMAL)

# cv2.imshow("RGB", img)
# cv2.imshow("B", B)
# cv2.imshow("G", G)
# cv2.imshow("R", R)
# cv2.imshow("BGR", img2)

# cv2.waitKey()
# cv2.destroyAllWindows()


# ##espacio de color HSV, es mayormente utilizado para la detección de objetos mediante color

# img = cv2.imread("1.jpeg")

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# h, s, v = cv2.split(hsv)

# cv2.imshow("HSV", hsv)
# cv2.imshow("H", h)
# cv2.imshow("S", s)
# cv2.imshow("V", v)
# cv2.waitKey()
# cv2.destroyAllWindows()



##Conversión a escala de grises

# img = cv2.imread("1.jpeg") ## leemos la imagen y la cargamos en img

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("RGB", img)
# cv2.imshow("gray", gray)

# cv2.waitKey()
# cv2.destroyAllWindows()