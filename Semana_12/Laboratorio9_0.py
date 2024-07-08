# -*- coding: utf-8 -*-


# Procesamiemto digital de imagenes
# Lbreria OPENCV
# Librería de visión artificial, originalmente desarrollada por intel
# Desarrollada en C y C++
# Libre para investigación o fines comerciales
# Multiplataforma
# Amplia documentación
# Gran comunidad

# =============================================================================
# TEMARIO
# Leer imágenes
# Mostrar imágenes
# Guardar imágenes
# Campos de color
# Trabajando con pixeles
# =============================================================================

# Instalar la libreia OPENCV : pip install opencv-contrib-python

import cv2 ## Importamos la librería OPENCV

##Utilizando el comando imread de opencv, leeremos la imagen 1.jpeg y la guardaremos en la variable img
img = cv2.imread("1.jpeg")
## Utilizando el comando imshow de opencv, mostraremos la imagen en una ventana llamada ventana1
cv2.imshow("ventana1", img)
##Controla el tiempo de muestreo de la señal de entrada por teclado
cv2.waitKey()
## destruye o cierra las ventanas creadas por opencv
cv2.destroyAllWindows()
# ##Guardamos la imagen contenida en la variable img en el archivo imagenGuardada1.jpeg
# cv2.imwrite("imagenGuardada1.jpeg", img)


# ##mandamos llamar la imagen 1.jpeg en escala de grises y la guardamos en la variable img
# img1 = cv2.imread("1.jpeg", cv2.IMREAD_GRAYSCALE) #tambien se puede remplazar cv2.IMREAD_GRAYSCALE por un 0 zero
# cv2.imshow("imagen en escala de grises", img1)
# cv2.waitKey()
# cv2.destroyAllWindows()

## Propiedad Full screen
# img2 = cv2.imread("1.jpeg",0)
# cv2.imshow("ventana", img2) ## Mostramos la imagen en la ventana "ventana", es redimensionable pero no cambia su escala
# cv2.waitKey()
# cv2.destroyAllWindows()

# img2 = cv2.imread("1.jpeg",0)
# cv2.namedWindow("ventana", cv2.WND_PROP_FULLSCREEN) ## Aplicamos la propiedad full screen a la ventana

# ##Activamos la propiedad full screen
# cv2.setWindowProperty("ventana", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) ## cv2.setWindowProperty("ventana", 0, 1)
# cv2.imshow("ventana", img2) ## Mostramos la imagen en la ventana "ventana", es redimensionable pero no cambia su escala
# cv2.waitKey()
# cv2.destroyAllWindows()

# ##Activamos la propiedad redimensionar
# cv2.namedWindow("ventana", cv2.WINDOW_NORMAL) ## Esta propiedad nos permite redimensionar la ventana
# cv2.imshow("ventana", img2) ## Mostramos la imagen en la ventana "ventana", es redimensionable pero no cambia su escala
# cv2.waitKey()
# cv2.destroyAllWindows()

# cv2.namedWindow("ventana", cv2.WINDOW_AUTOSIZE)




