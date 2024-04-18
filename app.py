"""
    Autor: Carlos Daniel Gomes Santana
    Contato: cdgomessantana@gmail.com
    Descrição: Esse é um aplicativo desktop que
    cria QR Code personalizados com uma licensa
    de software livre (BSD 2-Clause License)
"""

from tkinter import Button, Entry, Label, PhotoImage, Tk

from PIL import Image, ImageTk

# Criar a janela principal
janela = Tk()

# Definir largura e altura da janela (em pixels)
LARGURA = 640
ALTURA = 480

# Obter as dimensões da tela
LARGURA_DA_TELA = janela.winfo_screenwidth()
ALTURA_DA_TELA = janela.winfo_screenheight()

# Calcular as coordenadas para o centro da tela
x = (LARGURA_DA_TELA - LARGURA) // 2
y = (ALTURA_DA_TELA - ALTURA) // 2

# Carregar a imagem
imagem = Image.open(fp="icon.png")

# Carregar o ícone como uma imagem
icone = PhotoImage(file="icon.png")

# Redimensionar a imagem para o tamanho desejado
LARGURA_DESEJADA = int(LARGURA * 0.38)
ALTURA_DESEJADA = int(ALTURA * 0.38)
imagem_redimensionada = imagem.resize(size=(LARGURA_DESEJADA, ALTURA_DESEJADA))

# Posicionamento da Label da imagem
# Converter a imagem redimensionada para um formato suportado pelo Tkinter
imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)

# Criar um rótulo para exibir a imagem
COORDENADA_X_LABEL_IMAGEM = (LARGURA - LARGURA_DESEJADA) // 2
COORDENADA_Y_LABEL_IMAGEM = (ALTURA - ALTURA_DESEJADA) // 2 - 135
label_imagem = Label(
    master=janela, image=imagem_tk,  # type: ignore[arg-type]
    bd=2, relief="solid"
)
label_imagem.place(x=COORDENADA_X_LABEL_IMAGEM, y=COORDENADA_Y_LABEL_IMAGEM)

# Atribuir o ícone à janela
janela.iconphoto(True, icone)

# Posicionamento da Entry do dados do QR Code
# Criar uma entrada de texto
LARGURA_ENTRADA = 50
COORDENADA_X_ENTRADA = (LARGURA - LARGURA_DESEJADA - LARGURA_ENTRADA) // 2
COORDENADA_Y_ENTRADA = (LARGURA - LARGURA_DESEJADA) // 2 + 10
entrada = Entry(
    janela,
    width=LARGURA_ENTRADA,
)
entrada.place(x=COORDENADA_X_ENTRADA, y=COORDENADA_Y_ENTRADA)

# Posicionamento dos Button do dados do QR Code
# Criar um botão para gerar o QR Code
ALTURA_BOTAO_GERAR = 1
LARGURA_BOTAO_GERAR = 12
botao_gerar = Button(
    janela,
    text="Gerar",
    height=ALTURA_BOTAO_GERAR,
    width=LARGURA_BOTAO_GERAR,
    command=lambda: print("Gerar"),
)

COORDENADA_X_BOTAO_GERAR = (LARGURA - botao_gerar.winfo_reqwidth()) // 2
COORDENADA_Y_BOTAO_GERAR = (LARGURA - botao_gerar.winfo_reqheight()) // 2
botao_gerar.place(x=COORDENADA_X_BOTAO_GERAR, y=COORDENADA_Y_BOTAO_GERAR)

# Criar um botão para baixar o QR Code
ALTURA_BOTAO_BAIXAR = 1
LARGURA_BOTAO_BAIXAR = 12
botao_baixar = Button(
    janela,
    text="Baixar",
    height=ALTURA_BOTAO_BAIXAR,
    width=LARGURA_BOTAO_BAIXAR,
    command=lambda: print("Baixar"),
)
COORDENADA_X_BOTAO_BAIXAR = (LARGURA - botao_baixar.winfo_reqwidth()) // 2
COORDENADA_Y_BOTAO_BAIXAR = (
    LARGURA - botao_baixar.winfo_reqheight() + botao_gerar.winfo_reqwidth()
) // 2
botao_baixar.place(x=COORDENADA_X_BOTAO_BAIXAR, y=COORDENADA_Y_BOTAO_BAIXAR)

# Configurações da janela
# Definir a posição da janela
janela.geometry(f"{LARGURA}x{ALTURA}+{x}+{y}")

# Impedir o redimensionamento da janela
janela.resizable(width=False, height=False)

# Adicionando um título
janela.title("QR Code")

# Definindo a cor do fundo de tela
janela.configure(bg="#E5E1DA")

# Rodar o loop principal da aplicação
janela.mainloop()
