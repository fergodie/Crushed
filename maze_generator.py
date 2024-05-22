import random

def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve_passages_from(x, y, maze):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[ny - dy][nx - dx] = 0
                carve_passages_from(nx, ny, maze)

    maze[1][1] = 0
    carve_passages_from(1, 1, maze)

    maze[height - 2][width - 2] = 0  # Asegura que haya una salida
    return maze
