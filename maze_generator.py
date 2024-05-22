import random

def generate_maze(width, height):
    maze = [[1] * width for _ in range(height)]

    def carve_passages_from(cx, cy, maze):
        directions = [(cx + 2, cy), (cx - 2, cy), (cx, cy + 2), (cx, cy - 2)]
        random.shuffle(directions)
        for (nx, ny) in directions:
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == 1:
                if maze[ny][nx] == 1:
                    maze[ny][nx] = 0
                    maze[cy + (ny - cy) // 2][cx + (nx - cx) // 2] = 0
                    carve_passages_from(nx, ny, maze)

    maze[1][1] = 0
    carve_passages_from(1, 1, maze)

    # Asegurar que la salida sea accesible
    maze[height - 2][width - 2] = 0
    maze[height - 2][width - 3] = 0
    maze[height - 3][width - 2] = 0

    return maze

# Ejemplo de uso
if __name__ == "__main__":
    width, height = 21, 21  # Asegúrar que las dimensiones sean impares
    maze = generate_maze(width, height)
    for row in maze:
        print(''.join(['#' if cell else ' ' for cell in row]))
