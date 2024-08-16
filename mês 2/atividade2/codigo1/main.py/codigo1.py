import cv2
import numpy as np

#imprimir images 
img1 = cv2.imread('street-00.jpg')
img2 = cv2.imread('street-01.jpg')
assert img1 is not None, 'Imagem não encontrada, verifique se o path existe'
assert img2 is not None, 'Imagem não encontrada, verifique se o path existe'

#transformar para escala cinza 
img1_gray= cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#calcular diferença absoluta entre duas imagens 
dif_abs = cv2.absdiff(img1_gray, img2_gray) 

#binarizar imagens
ret, thresh = cv2.threshold(dif_abs, 30, 255, cv2.THRESH_BINARY)
 
#calcular contornos 
contornos, ret = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#imprimir imagem e mostrar os carros detectados com um retangulo
result = img2.copy()
for contorno in contornos:
    if cv2.contourArea(contorno) > 400: 
        x, y, w, h = cv2.boundingRect(contorno)
        cv2.rectangle(result, (x, y), (w+x, h+y), (0, 255, 0), 2)

#abrir janela 
cv2.imshow('Carros Detectados', result)
cv2.waitKey(0)
cv2.destroyAllWindows()