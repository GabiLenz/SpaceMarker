import pygame
import tkinter as tk
from tkinter import simpledialog

# Inicialização do Pygame
pygame.init()

sys = SystemExit
# Configuração da janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("SPACE MARKER")

# Carregamento dos recursos (sons, imagens, etc.)
fundo = pygame.image.load("imagem.fundo.jpg")
fundo = pygame.transform.scale(fundo, (largura, altura))

# Carregamento do som de fundo
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)  # Reproduzir em looping

# Carregamento do ícone
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)

import pygame
import tkinter as tk
from tkinter import simpledialog

# Definição das cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Variáveis para armazenar as marcações das estrelas
marcacoes = {}
# Variáveis para armazenar as linhas e as somas das distâncias
linhas = []
distancias = []

# Função para abrir a caixa de diálogo e obter o nome da estrela
def obter_nome_estrela():
    root = tk.Tk()
    root.withdraw()
    nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    return nome

# Função para calcular a distância entre dois pontos
def calcular_distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia

# Loop principal do jogo
try:
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                # Salvar as marcações antes de fechar
                with open("marcacoes.txt", "w") as arquivo:
                    for posicao, nome in marcacoes.items():
                        arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")
                
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    # Obter a posição do clique do mouse
                    posicao_mouse = pygame.mouse.get_pos()
                    
                    # Abrir caixa de diálogo para obter o nome da estrela
                    nome_estrela = obter_nome_estrela()
                    
                    # Adicionar a marcação ao dicionário de marcações
                    marcacoes[posicao_mouse] = nome_estrela

        # Renderizar a imagem de fundo e as marcações
        janela.blit(fundo, (0, 0))

        for posicao, nome in marcacoes.items():
            # Desenhar uma marcação (círculo) na posição
            pygame.draw.circle(janela, vermelho, posicao, 10)
            
            # Desenhar o nome da estrela
            fonte = pygame.font.Font(None, 20)
            texto = fonte.render(nome, True, branco)
            janela.blit(texto, (posicao[0], posicao[1] + 20))


        pygame.display.update()
              # Obter a posição do clique do mouse
             
             
    posicao_mouse = pygame.mouse.get_pos()

  # Adicionar a marcação ao dicionário de marcações
    marcacoes.txt[posicao_mouse] = nome_estrela

             # Calcular a distância e adicionar à lista de distâncias
    if len(marcacoes) > 1:
             posicoes = list(marcacoes.keys())
    distancia = calcular_distancia(posicoes[-2], posicoes[-1])
    distancias.append(distancia)
    print ("marcacoes.tex")
 

except Exception as erro:
    # Lidar com erros
     print(f"Ocorreu um erro: {erro}")
     pygame.quit()
     sys.exit()
