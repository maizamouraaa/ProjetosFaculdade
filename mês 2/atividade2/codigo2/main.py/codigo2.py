import cv2
import numpy as np

img_ref = cv2.imread('porta1.jpg')
img1 = cv2.imread('kirra1.jpg')
img2 = cv2.imread('larapio.jpg')

assert img_ref is not None, 'imagem nao encontrada, verifique o path'
assert img1 is not None, 'imagem nao encontrada, verifique o path'
assert img2 is not None, 'imagem nao encontrada, verifique o path'

#passar para escala cinza 
gray_ref = cv2.cvtColor(img_ref, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#borrar imagem p diminuir ruidos 
gray_ref = cv2.GaussianBlur(gray_ref, (5, 5), 0)
gray1 = cv2.GaussianBlur(gray1, (5, 5), 0)
gray2 = cv2.GaussianBlur(gray2, (5, 5), 0)

#calcular dif absoluta 
dif1 = cv2.absdiff(gray_ref, gray1)
dif2 = cv2.absdiff(gray_ref, gray2)

#binarizar imagem 
ret, thresh1 = cv2.threshold(dif1, 25, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(dif2, 25, 255, cv2.THRESH_BINARY)

contornos1, ret = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos2, ret = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contorno in contornos1:
    if cv2.contourArea(contorno) > 400:  
        x, y, w, h = cv2.boundingRect(contorno)
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)

for contorno in contornos2:
    if cv2.contourArea(contorno) > 400:  
        x, y, w, h = cv2.boundingRect(contorno)
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('intrusos Detectados - Imagem 1', img1)
cv2.imshow('intrusos Detectados - Imagem 2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('img1.jpg', img1)
cv2.imwrite('img2.jpg', img2)



