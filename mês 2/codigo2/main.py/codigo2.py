import cv2

def carregar_imagem(nome):
    imagem = cv2.imread(nome)
    if imagem is None:
        print(f"Erro: não foi possível carregar a imagem '{nome}'")
        return None
    return imagem

def mostrar_imagem(janela, imagem):
    if imagem is not None:
        cv2.imshow(janela, imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def dimensoes_imagem(nome):
    imagem = carregar_imagem(nome)
    if imagem is not None:
        print('Largura em pixels: ', imagem.shape[1])
        print('Altura em pixels: ', imagem.shape[0])
        print('Quantidade de canais: ', imagem.shape[2])
    return imagem

def conversao_hsv(nome):
    imagem = carregar_imagem(nome)
    if imagem is not None:
        imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
        lower = (90, 80, 40)  # Matriz, saturação e brilho 
        upper = (120, 255, 255)
        mask = cv2.inRange(imagem_hsv, lower, upper)
        return mask

def converter_imagem(nome):
    imagem = carregar_imagem(nome)
    if imagem is not None:
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        print('Largura em pixels: ', imagem.shape[1])
        print('Altura em pixels: ', imagem.shape[0])
        print('Quantidade de canais: 1')  # Imagem cinza tem 1 canal
        return imagem_cinza

def exibir_menu():
    print("\nEscolha uma opção:")
    print("1. Mostrar dimensões da imagem")
    print("2. Mostrar imagem em cinza e novas dimensões")
    print("3. Mostrar conversão para HSV")
    print("4. Sair")
    return input("Opção: ")

def main():
    nome_imagem = "IEEE.png"  # Nome da imagem a ser carregada
    while True:
        escolha = exibir_menu()
        if escolha == '1':
            imagem = dimensoes_imagem(nome_imagem)
            mostrar_imagem("Logo IEEE", imagem)
        elif escolha == '2': 
            imagem = converter_imagem(nome_imagem)
            mostrar_imagem("Grayscale", imagem)
        elif escolha == '3':
            imagem = conversao_hsv(nome_imagem)
            mostrar_imagem('HSV', imagem)
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
