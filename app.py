import tkinter as tk

# Criar a janela principal
janela = tk.Tk()
janela.title("QR Code")

# Definir largura e altura da janela (em pixels)
largura = 400
altura = 300

# Obter as dimensões da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcular as coordenadas para o centro da tela
x = (largura_tela - largura) // 2
y = (altura_tela - altura) // 2

# Carregar o ícone como uma imagem (substitua 'icone.ico' pelo caminho do seu ícone)
icone = tk.PhotoImage(file="icon.png")

# Atribuir o ícone à janela
janela.iconphoto(True, icone)

# Definir a posição da janela
janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Impedir o redimensionamento da janela
janela.resizable(False, False)


# Rodar o loop principal da aplicação
janela.mainloop()
