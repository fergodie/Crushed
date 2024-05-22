import pygame
from pygame.locals import *
from levels import levels, next_level

# Inicializar Juego
pygame.init()

# Configuración de los Nieveles
TILE_SIZE = 40
maze_width, maze_height = 10, 10  # Tamaño del laberinto
SCREEN_WIDTH = maze_width * TILE_SIZE
SCREEN_HEIGHT = maze_height * TILE_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Juego de Laberinto')

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Definir el nivel y el laberinto inicial
current_level = 0
maze = levels[current_level]

# Posición inicial del jugador
player_pos = [1, 1]
exit_pos = [maze_width - 2, maze_height - 2]  # Posición de la salida

# Estados del juego
START_SCREEN = 0
GAME_SCREEN = 1
END_SCREEN = 2
game_state = START_SCREEN

# Función para dibujar el laberinto
def draw_maze(screen, maze):
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            color = WHITE if tile == 0 else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Función para mover al jugador
def move_player(pos, direction):
    new_pos = pos.copy()
    if direction == 'up':
        new_pos[1] -= 1
    elif direction == 'down':
        new_pos[1] += 1
    elif direction == 'left':
        new_pos[0] -= 1
    elif direction == 'right':
        new_pos[0] += 1
    return new_pos

# Función para comprobar colisiones
def can_move(pos, maze):
    if pos[1] < 0 or pos[1] >= len(maze) or pos[0] < 0 or pos[0] >= len(maze[0]):
        return False
    if maze[pos[1]][pos[0]] == 1:
        return False
    return True

# Función para verificar si el jugador ha llegado a la salida
def check_exit(pos, exit_pos):
    return pos == exit_pos

# Función para mostrar la pantalla principal
def show_start_screen():
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 55)
    title = font.render("Juego de Laberinto", True, BLACK)
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 3))
    
    font = pygame.font.SysFont(None, 35)
    start_button = font.render("Iniciar Juego", True, BLACK)
    screen.blit(start_button, (SCREEN_WIDTH // 2 - start_button.get_width() // 2, SCREEN_HEIGHT // 2))
    
    exit_button = font.render("Salir", True, BLACK)
    screen.blit(exit_button, (SCREEN_WIDTH // 2 - exit_button.get_width() // 2, SCREEN_HEIGHT // 2 + 40))
    pygame.display.flip()

# Función para mostrar la pantalla final
def show_end_screen():
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 55)
    message = font.render("¡Gracias por jugar!", True, BLACK)
    screen.blit(message, (SCREEN_WIDTH // 2 - message.get_width() // 2, SCREEN_HEIGHT // 3))
    
    font = pygame.font.SysFont(None, 35)
    exit_button = font.render("Salir", True, BLACK)
    screen.blit(exit_button, (SCREEN_WIDTH // 2 - exit_button.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if game_state == GAME_SCREEN:
                new_pos = player_pos
                if event.key == K_UP:
                    new_pos = move_player(player_pos, 'up')
                elif event.key == K_DOWN:
                    new_pos = move_player(player_pos, 'down')
                elif event.key == K_LEFT:
                    new_pos = move_player(player_pos, 'left')
                elif event.key == K_RIGHT:
                    new_pos = move_player(player_pos, 'right')

                if can_move(new_pos, maze):
                    player_pos = new_pos

                # Comprueba si el jugador ha llegado a la salida
                if check_exit(player_pos, exit_pos):
                    current_level = next_level(current_level, levels)
                    if current_level is not None:
                        maze = levels[current_level]
                        player_pos = [1, 1]  # Restablece la posición del jugador
                        exit_pos = [maze_width - 2, maze_height - 2]  # Restablece la posición de la salida
                    else:
                        # El jugador ha completado todos los niveles
                        game_state = END_SCREEN

        elif event.type == MOUSEBUTTONDOWN:
            if game_state == START_SCREEN:
                mouse_pos = event.pos
                if SCREEN_WIDTH // 2 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 2 + 50:
                    if SCREEN_HEIGHT // 2 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 40:
                        game_state = GAME_SCREEN
                    elif SCREEN_HEIGHT // 2 + 40 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 80:
                        running = False
            elif game_state == END_SCREEN:
                mouse_pos = event.pos
                if SCREEN_WIDTH // 2 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 2 + 50:
                    if SCREEN_HEIGHT // 2 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 40:
                        running = False

    if game_state == START_SCREEN:
        show_start_screen()
    elif game_state == GAME_SCREEN:
        screen.fill(WHITE)
        draw_maze(screen, maze)
        pygame.draw.rect(screen, GREEN, pygame.Rect(exit_pos[0] * TILE_SIZE, exit_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))  # Dibuja la salida
        pygame.draw.rect(screen, BLUE, pygame.Rect(player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))  # Dibuja el jugador
        pygame.display.flip()
    elif game_state == END_SCREEN:
        show_end_screen()

pygame.quit()
