import sys
import time
import pygame

# Inicializa os módulos do Pygame
pygame.init()
pygame.mixer.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Configurações da janela do jogo
pygame.display.set_caption("Bolsonaro run 1")

# Imagem dos jogadores
bolsonaro_normal = pygame.image.load("bosonaro.jpeg")
bolsonaro_preso = pygame.image.load("bosonaropreso.jpeg")

alexandre_normal = pygame.image.load("images.jpeg")
alexandre_rindo = pygame.image.load("alexandrerindo.jpeg")

cenario = pygame.image.load("cenario.jpeg")
cenario = pygame.transform.scale(cenario, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Gerenciar o fps do jogo
clock = pygame.time.Clock()

# Fonte
font = pygame.font.SysFont(None, 50)

pygame.mixer.music.load("hino_nacional_brasileiro.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

bolsonaropreso = pygame.mixer.Sound("pegarammeutelefone.mp3")


# função para resetar o jogo
def reset_jogo():
    global player_x, player_y, player_x2, player_y2, bolsonaro, alexandre, prisao
    # Posições iniciais dos jogadores
    player_x = 125
    player_y = 500

    player_x2 = 500
    player_y2 = 100

    # Reseta as imagens para o estado normal
    bolsonaro = bolsonaro_normal
    alexandre = alexandre_normal

    prisao = False


# Inicializa as variáveis do jogo pela primeira vez
reset_jogo()

# Inicializa hitboxes
bolsonaro_rect = pygame.Rect(player_x, player_y, 96, 96)
alexandre_rect = pygame.Rect(player_x2, player_y2, 96, 96)

player_speed = 5
player_speed2 = 3.2

# Loop principal do jogo
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # sistema de movimento dos jogadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - 50:
        player_y += player_speed

    if keys[pygame.K_a] and player_x2 > 0:
        player_x2 -= player_speed2
    if keys[pygame.K_d] and player_x2 < SCREEN_WIDTH - 50:
        player_x2 += player_speed2
    if keys[pygame.K_w] and player_y2 > 0:
        player_y2 -= player_speed2
    if keys[pygame.K_s] and player_y2 < SCREEN_HEIGHT - 50:
        player_y2 += player_speed2

    # atualiza a posição das hitboxes
    bolsonaro_rect.x = player_x
    bolsonaro_rect.y = player_y
    alexandre_rect.x = player_x2
    alexandre_rect.y = player_y2

    # renderizar o jogo
    screen.blit(cenario, (0, 0))

    # Coisas que acontecem quando o big xande pega o capitão
    if bolsonaro_rect.colliderect(alexandre_rect) and not prisao:
        # Troca a imagem dos personagens
        bolsonaro = bolsonaro_preso
        alexandre = alexandre_rindo

        # Desenha o cenário e as novas imagens atualizadas na tela
        screen.blit(cenario, (0, 0))
        screen.blit(bolsonaro, (player_x, player_y))
        screen.blit(alexandre, (player_x2, player_y2))

        # Coloca o texto de derrota
        texto = font.render("PRESO! Reiniciando...", True, (255, 0, 0))
        screen.blit(texto, (SCREEN_WIDTH // 2 - texto.get_width() // 2, 50))

        # Atualiza a tela com as mudanças
        pygame.display.flip()

        # Toca o som de derrota
        pygame.mixer.music.stop()    # para o hino
        bolsonaropreso.play()

        # Espera 3 segundos (3000 milissegundos)
        pygame.time.delay(5000)

        # Limpa comandos enquanto o jogo estava pausado
        pygame.event.clear()

        # Volta a tocar o hino
        pygame.mixer.music.play(-1)

        # Reseta as posições e imagens para a posição inicials
        reset_jogo()
        continue

    # desenha os jogadores na tela se não houver colisão
    screen.blit(bolsonaro, (player_x, player_y))
    screen.blit(alexandre, (player_x2, player_y2))

    # atualiza a tela
    pygame.display.flip()

    # controle de fps
    clock.tick(60)

# encerra o programa corretamente
pygame.quit()
sys.exit()