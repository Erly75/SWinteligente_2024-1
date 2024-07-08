# -*- coding: utf-8 -*-
"""
Created on Fri May 26 17:08:20 2023

@author: lolo_
"""


import numpy as np
from matplotlib import pyplot as plt
import cv2
# =============================================================================
# Ecualización del histograma imagenes
# =============================================================================
img = cv2.imread("a.jpg", 0) ## leemos la imagen de entrada y la guardamos en la variable img
equ = cv2.equalizeHist(img) ## realizamos la equialización del histograma

res = np.hstack((img,equ)) ##concatenamos la imagen de entrada con la imagen equializada

cv2.namedWindow("resultado", cv2.WINDOW_NORMAL)#construimos nuestra ventana donde se mostrara la imagen
cv2.imshow("resultado", res) ##mostramos la imagen concatenada
cv2.waitKey()
cv2.destroyAllWindows()

# =============================================================================
# obteniendo histograma de la imagen original y la equalizada
# =============================================================================
hist, bins = np.histogram(img.flatten(), 256, [0,256])
plt.hist(img.flatten(), 256, [0,256], color = 'b')
plt.xlim([0,256])
plt.legend('H', loc = 'upper left')
plt.show()

hist, bins = np.histogram(equ.flatten(), 256, [0,256])
plt.hist(equ.flatten(), 256, [0,256], color = 'b')
plt.xlim([0,256])
plt.legend('H', loc = 'upper left')
plt.show()

# =============================================================================
# Aplicacion de umbralización adaptativa
# clipLimit: este parámetro establece el umbral para la limitación del contraste. El valor predeterminado es 40.
# tileGridSize: establece el número de mosaicos en la fila y la columna. Por defecto es 8×8. Se utiliza mientras la imagen se divide en mosaicos para aplicar CLAHE.
# =============================================================================

# img = cv2.imread("antes.jpg", 0) ## leemos la imagen de entrada y la guardamos en la variable img
# clahe = cv2.createCLAHE(clipLimit = 5.0 , tileGridSize = (8,8)) ##creamos la configuración  para el algoritmo
# ##CLAHE con un humbral de 1.0 y un kernel de 8 x 8

# cl1 = clahe.apply(img) ## aplicamos el metodo a la imagen de entrada
# res = np.hstack((img,cl1)) ##concatenamos la imagen de entrada con la imagen equializada

# cv2.namedWindow("resultado", cv2.WINDOW_NORMAL)#construimos nuestra ventana donde se mostrara la imagen
# cv2.imshow("resultado", res) ##mostramos la imagen concatenada
# cv2.waitKey()
# cv2.destroyAllWindows()

# hist, bins = np.histogram(img.flatten(), 256, [0,256])
# plt.hist(img.flatten(), 256, [0,256], color = 'b')
# plt.xlim([0,256])
# plt.legend('H', loc = 'upper left')
# plt.show()

# hist, bins = np.histogram(cl1.flatten(), 256, [0,256])
# plt.hist(cl1.flatten(), 256, [0,256], color = 'b')
# plt.xlim([0,256])
# plt.legend('H', loc = 'upper left')
# plt.show()