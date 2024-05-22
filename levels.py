from maze_generator import generate_maze

def next_level(current_level, levels):
    if current_level + 1 < len(levels):
        return current_level + 1
    else:
        return None

# Inicializa niveles con laberintos generados
levels = [generate_maze(20, 20) for _ in range(5)]  # Genera 5 niveles
