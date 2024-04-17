from PIL import (
    Image,
    ImageTk
)
from tkinter import (
    Tk,
    Label,
    Entry,
    Button,
    PhotoImage
)

# Criar a janela principal
janela = Tk()

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
largura_desejada = int(largura*0.38)
altura_desejada = int(altura*0.38)
imagem_redimensionada = imagem.resize(
    size = (
        largura_desejada,
        altura_desejada
    )
)

# Posicionamento da Label da imagem
# Converter a imagem redimensionada para um formato suportado pelo Tkinter
imagem_tk = ImageTk.PhotoImage(
    imagem_redimensionada
)

# Criar um rótulo para exibir a imagem
coordenada_x_label_imagem = (largura - largura_desejada)//2
coordenada_y_label_imagem = (altura - altura_desejada)//2 - 135
label_imagem = Label(
    master = janela,
    image = imagem_tk,
    bd = 2,
    relief = "solid"
)
label_imagem.place(
    x = coordenada_x_label_imagem,
    y = coordenada_y_label_imagem
)

# Garantir que a imagem seja mantida em memória
label_imagem.imagem_tk = imagem_tk

# Atribuir o ícone à janela
janela.iconphoto(
    True, icone
)

# Posicionamento da Entry do dados do QR Code
# Criar uma entrada de texto
largura_entrada = 50
coordenada_x_entrada = (largura - largura_desejada - largura_entrada)//2 
coordenada_y_entrada = (largura - largura_desejada)//2 + 10
entrada = Entry(
    janela,
    width = largura_entrada,
)
entrada.place(
    x = coordenada_x_entrada,
    y = coordenada_y_entrada
)

# Posicionamento dos Button do dados do QR Code
# Criar um botão para gerar o QR Code
altura_botao_gerar = 1
largura_botao_gerar = 12
botao_gerar = Button(
    janela,
    text="Gerar",
    height=altura_botao_gerar,
    width=largura_botao_gerar,
    command=lambda : print("Gerar")
)

coordenada_x_botao_gerar = (largura - botao_gerar.winfo_reqwidth())//2
coordenada_y_botao_gerar = (largura - botao_gerar.winfo_reqheight())//2
botao_gerar.place(
    x = coordenada_x_botao_gerar,
    y = coordenada_y_botao_gerar
)

# Criar um botão para baixar o QR Code
altura_botao_baixar = 1
largura_botao_baixar = 12
botao_baixar = Button(
    janela,
    text="Baixar",
    height=altura_botao_baixar,
    width=largura_botao_baixar,
    command=lambda : print("Baixar")
)
coordenada_x_botao_baixar = (largura - botao_baixar.winfo_reqwidth())//2
coordenada_y_botao_baixar = (largura - botao_baixar.winfo_reqheight() + botao_gerar.winfo_reqwidth())//2
botao_baixar.place(
    x = coordenada_x_botao_baixar,
    y = coordenada_y_botao_baixar
)

# Configurações da janela
# Definir a posição da janela
janela.geometry(
    f"{largura}x{altura}+{x}+{y}"
)

# Impedir o redimensionamento da janela
janela.resizable(
    width = False,
    height = False
)

# Adicionando um título
janela.title("QR Code")

# Definindo a cor do fundo de tela
janela.configure(bg='#E5E1DA')

# Rodar o loop principal da aplicação
janela.mainloop()
