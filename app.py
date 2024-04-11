from PIL import (
    Image,
    ImageTk
)
from tkinter import (
    Tk,
    Label,
    PhotoImage
)

# Criar a janela principal
janela = Tk()
janela.title("QR Code")

# Definir largura e altura da janela (em pixels)
largura = 640
altura = 480

# Obter as dimensões da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcular as coordenadas para o centro da tela
x = (largura_tela - largura) // 2
y = (altura_tela - altura) // 2

# Carregar o ícone como uma imagem (substitua 'icone.ico' pelo caminho do seu ícone)
icone = PhotoImage(file = "icon.png")

# Carregar a imagem (substitua 'imagem.png' pelo caminho da sua imagem)
imagem = Image.open(fp = "icon.png")

# Redimensionar a imagem para o tamanho desejado
largura_desejada = 200
altura_desejada = 150
imagem_redimensionada = imagem.resize(
    size = (largura_desejada, altura_desejada)
)

# Converter a imagem redimensionada para um formato suportado pelo Tkinter
imagem_tk = ImageTk.PhotoImage(
    imagem_redimensionada
)

# Criar um rótulo para exibir a imagem
label_imagem = Label(
    master = janela,
    image = imagem_tk
)
label_imagem.pack()

# Garantir que a imagem seja mantida em memória
label_imagem.imagem_tk = imagem_tk

# Atribuir o ícone à janela
janela.iconphoto(
    True, icone
)

# Definir a posição da janela
janela.geometry(
    f"{largura}x{altura}+{x}+{y}"
)

# Impedir o redimensionamento da janela
janela.resizable(
    width = False,
    height = False
)

# Rodar o loop principal da aplicação
janela.mainloop()
