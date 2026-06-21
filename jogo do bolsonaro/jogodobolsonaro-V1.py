import time
import pygame
import sys

# Inicializa os módulos do Pygame
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Configurações da janela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Imagem dos jogadores
bolsonaro = pygame.image.load('bosonaro.jpeg')
alexandre = pygame.image.load('images.jpeg')



pygame.display.set_caption("Bolsonaro run 1")
cenario = pygame.image.load('cenario.jpeg')
cenario = pygame.transform.scale(cenario, (SCREEN_WIDTH, SCREEN_HEIGHT))
# gerenciar o fps do jogo
clock = pygame.time.Clock()

# fonte
font = pygame.font.SysFont(None, 50)

# variáveis do jogo
player_x = 375
player_y = 500
player_speed = 5

player_x2 = 125
player_y2 = 250
player_speed2 = 4

# colisão
bolsonaro_rect = pygame.Rect(player_x, player_y, 50, 50)
alexandre_rect = pygame.Rect(player_x2, player_y2, 50, 50)

# Loop principal do jogo
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # sistema de movimento (jogador 1)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > -10:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y > -10:
        player_y += player_speed

    # sistema de movimento (jogador 2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x2 -= player_speed
    if keys[pygame.K_d] and player_x < SCREEN_WIDTH - 5:
        player_x2 += player_speed
    if keys[pygame.K_w] and player_y > 0:
        player_y2 -= player_speed
    if keys[pygame.K_s] and player_y > 0:
        player_y2 += player_speed

    # atualiza a posição das hitboxes
    bolsonaro_rect.x = player_x
    bolsonaro_rect.y = player_y
    alexandre_rect.x = player_x2
    alexandre_rect.y = player_y2

    # renderizar o jogo

    # cor de fundo
    screen.blit(cenario, (0, 0))

    # desenha os jogadores na tela
    #pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(player_x, player_y, 50, 50))
    screen.blit(bolsonaro, (player_x, player_y, 50, 50))
    screen.blit(alexandre, (player_x2, player_y2, 50, 50))

    # Coisas que acontecem quando o big xande pega o capitão
    if bolsonaro_rect.colliderect(alexandre_rect):
        texto = font.render("preso", True, (255, 0, 0))
        screen.blit(texto, (SCREEN_WIDTH // 2 - texto.get_width() // 2, 50))
        bolsonaro = pygame.image.load('bosonaropreso.jpeg')
        alexandre = pygame.image.load('alexandrerindo.jpeg')
    #  atualiza a tela
    pygame.display.flip()

    #  controle de fps
    clock.tick(60)

# encerra o programa corretamente
pygame.quit()
sys.exit()