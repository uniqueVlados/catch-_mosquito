import pygame
from random import randint

# -----------КОНСТАНТЫ-------------------
# TODO: блок для объявления констант
GAME_LOOP = True
WIDTH, HEIGHT = 1200, 600
FPS = 30
BLOCK_SIZE = 60
SPEED = 20
ROCKET_W = 75
AMOUNT_TO_LOOSE = 5
WHITE_COLOR = (255, 255, 255)
# ---------------------------------------

# -----------ИЗОБРАЖЕНИЯ-----------------
# TODO: загружайте изображения здесь
rocket = pygame.image.load("img/rocket.png")
komar = pygame.image.load("img/komar.png")
background = pygame.image.load("img/room.png")
# ---------------------------------------

# -----------ИНИЦИАЛИЗАЦИЯ---------------
# TODO: блок инициализации параметров игры
pygame.init()
pygame.display.set_caption("Clicker")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 36)
pygame.display.set_icon(komar)
pygame.mouse.set_visible(False)
# ---------------------------------------


# -----------ФУНКЦИИ---------------------
def create_new(blocs_list):
    x = randint(0, WIDTH - BLOCK_SIZE)
    y = randint(0, HEIGHT - BLOCK_SIZE)
    blocs_list.append((x, y))


def draw(block_coord):
    screen.blit(komar, block_coord)


def draw_rocket():
    m_x, m_y = pygame.mouse.get_pos()
    m_x -= ROCKET_W // 2
    m_y -= ROCKET_W // 2
    screen.blit(rocket, (m_x, m_y))


def check_colission(block_):
    m_x, m_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]

    block_x, block_y = block_
    if click:
        return block_x <= m_x <= block_x + BLOCK_SIZE and block_y <= m_y <= block_y + BLOCK_SIZE

    return False


def draw_background():
    screen.blit(background, (0, 0))


def draw_score():
    text1 = font.render(str(score), True, WHITE_COLOR)
    screen.blit(text1, (30, 0))

# ---------------------------------------


# -----------MAIN------------------------
blocks = []
score = 0
timer = 0

create_new(blocks)


while GAME_LOOP:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    draw_background()

    for block in blocks[::-1]:
        if check_colission(block):
            blocks.remove(block)
            score += 1

        draw(block)

    draw_rocket()

    if timer == SPEED:
        create_new(blocks)
        timer = 0
    timer += 1

    draw_score()

    if len(blocks) == AMOUNT_TO_LOOSE:
        GAME_LOOP = False

    clock.tick(FPS)
    pygame.display.update()