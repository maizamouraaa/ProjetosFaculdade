import cv2
import numpy as np 

def resize(imagem):
    largura = imagem.shape[1]
    altura = imagem.shape[0]
    proporcao = float(altura / largura)
    larguraN = 100
    alturaN = int(larguraN * proporcao)
    imagem_redimensionada = cv2.resize(imagem, (larguraN, alturaN), interpolation=cv2.INTER_AREA)
    return imagem_redimensionada

def mudar_brilho(imagem, valor):
    img = imagem.astype(np.float32)
    img = img + valor
    img = np.clip(img, 0, 255).astype(np.uint8)
    return img

def bluring(imagem):
    imagem_blur = cv2.blur(imagem, (20, 20))
    return imagem_blur

def binaria(imagem):
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    _, thresh_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)
    _, thresh_otsu = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh_binaria, thresh_otsu

def mostrar_imagem(janela, imagem):
    cv2.imshow(janela, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    imagem = cv2.imread('IEEE_RAS.png')
    while True:
        print("Escolha uma opção:")
        print("1. Mostrar imagem com novas medidas")
        print("2. Mostrar imagem clara ou escura")
        print("3. Mostrar imagem com blur")
        print("4. Mostrar imagem binária")
        print("5. Sair")
        escolha = input("Opção: ")

        if escolha == '1':
            imagem_redimensionada = resize(imagem)
            mostrar_imagem("Imagem Redimensionada", imagem_redimensionada)
        elif escolha == '2': 
            valor_brilho = int(input("Digite o valor para ajuste de brilho (-255 a 255): "))
            imagem_brilho = mudar_brilho(imagem, valor_brilho)
            mostrar_imagem("Imagem com Brilho Ajustado", imagem_brilho)
        elif escolha == '3': 
            imagem_blur = bluring(imagem)
            mostrar_imagem("Imagem com Blur", imagem_blur)
        elif escolha == '4': 
            imagem_binaria, imagem_otsu = binaria(imagem)
            mostrar_imagem("Imagem com Thresholding Simples", imagem_binaria)
            mostrar_imagem("Imagem com Otsu Thresholding", imagem_otsu)
        elif escolha == '5':
           break
        else:
            print("Opção inválida. Tente novamente.")

main()
