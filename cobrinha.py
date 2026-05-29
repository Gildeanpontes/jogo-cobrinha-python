import pygame
import random

# Inicialização
pygame.init()

# Configurações da tela
LARGURA = 600
ALTURA = 400
TAMANHO_BLOCO = 20

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Relógio
clock = pygame.time.Clock()
FPS = 10

fonte = pygame.font.SysFont(None, 35)


def mostrar_pontuacao(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10, 10))


def desenhar_cobra(lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(
            tela, VERDE,
            [bloco[0], bloco[1], TAMANHO_BLOCO, TAMANHO_BLOCO]
        )


def jogo():
    x = LARGURA // 2
    y = ALTURA // 2

    dx = 0
    dy = 0

    cobra = []
    tamanho_cobra = 1

    comida_x = round(random.randrange(
        0, LARGURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    comida_y = round(random.randrange(
        0, ALTURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    dx = -TAMANHO_BLOCO
                    dy = 0
                elif evento.key == pygame.K_RIGHT:
                    dx = TAMANHO_BLOCO
                    dy = 0
                elif evento.key == pygame.K_UP:
                    dy = -TAMANHO_BLOCO
                    dx = 0
                elif evento.key == pygame.K_DOWN:
                    dy = TAMANHO_BLOCO
                    dx = 0

        x += dx
        y += dy

        # Colisão com bordas
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            rodando = False

        tela.fill(PRETO)

        pygame.draw.rect(
            tela,
            VERMELHO,
            [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO]
        )

        cabeca = [x, y]
        cobra.append(cabeca)

        if len(cobra) > tamanho_cobra:
            del cobra[0]

        # Colisão consigo mesma
        for segmento in cobra[:-1]:
            if segmento == cabeca:
                rodando = False

        desenhar_cobra(cobra)
        mostrar_pontuacao(tamanho_cobra - 1)

        pygame.display.update()

        # Comer comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(
                0, LARGURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
            comida_y = round(random.randrange(
                0, ALTURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
            tamanho_cobra += 1

        clock.tick(FPS)

    pygame.quit()


jogo()