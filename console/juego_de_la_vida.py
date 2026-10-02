"""
Juego de la Vida de Conway - animado en la terminal.

Controles (antes de iniciar):
  Elige un patron inicial del menu, o aleatorio.

Durante la simulacion:
  Ctrl+C -> salir

Ejecutar:
  python juego_de_la_vida.py
"""

import os
import random
import sys
import time

LIVE = "\x1b[38;5;46m#\x1b[0m"
DEAD = " "

# Patrones clasicos, como listas de coordenadas (fila, columna) relativas
PATTERNS = {
    "glider": [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    "pulsar": [
        (0, 2), (0, 3), (0, 4), (0, 8), (0, 9), (0, 10),
        (2, 0), (2, 5), (2, 7), (2, 12),
        (3, 0), (3, 5), (3, 7), (3, 12),
        (4, 0), (4, 5), (4, 7), (4, 12),
        (5, 2), (5, 3), (5, 4), (5, 8), (5, 9), (5, 10),
        (7, 2), (7, 3), (7, 4), (7, 8), (7, 9), (7, 10),
        (8, 0), (8, 5), (8, 7), (8, 12),
        (9, 0), (9, 5), (9, 7), (9, 12),
        (10, 0), (10, 5), (10, 7), (10, 12),
        (12, 2), (12, 3), (12, 4), (12, 8), (12, 9), (12, 10),
    ],
    "gosper_glider_gun": [
        (0, 24),
        (1, 22), (1, 24),
        (2, 12), (2, 13), (2, 20), (2, 21), (2, 34), (2, 35),
        (3, 11), (3, 15), (3, 20), (3, 21), (3, 34), (3, 35),
        (4, 0), (4, 1), (4, 10), (4, 16), (4, 20), (4, 21),
        (5, 0), (5, 1), (5, 10), (5, 14), (5, 16), (5, 17), (5, 22), (5, 24),
        (6, 10), (6, 16), (6, 24),
        (7, 11), (7, 15),
        (8, 12), (8, 13),
    ],
    "lwss": [  # lightweight spaceship
        (0, 1), (0, 4),
        (1, 0),
        (2, 0), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3),
    ],
}


def make_grid(rows, cols):
    return [[0] * cols for _ in range(rows)]


def place_pattern(grid, pattern, row_offset, col_offset):
    rows, cols = len(grid), len(grid[0])
    for dr, dc in pattern:
        r, c = row_offset + dr, col_offset + dc
        if 0 <= r < rows and 0 <= c < cols:
            grid[r][c] = 1


def random_grid(rows, cols, density=0.2):
    return [[1 if random.random() < density else 0 for _ in range(cols)] for _ in range(rows)]


def count_neighbors(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    total = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = (r + dr) % rows, (c + dc) % cols  # bordes toroidales
            total += grid[nr][nc]
    return total


def step(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = make_grid(rows, cols)
    for r in range(rows):
        for c in range(cols):
            n = count_neighbors(grid, r, c)
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if n in (2, 3) else 0
            else:
                new_grid[r][c] = 1 if n == 3 else 0
    return new_grid


def render(grid, generation, population):
    lines = []
    for row in grid:
        lines.append("".join(LIVE if cell else DEAD for cell in row))
    header = f"Generacion: {generation}   Poblacion: {population}   (Ctrl+C para salir)"
    return header + "\n" + "\n".join(lines)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def choose_pattern():
    print("Juego de la Vida de Conway\n")
    print("Elige un patron inicial:")
    options = list(PATTERNS.keys()) + ["aleatorio"]
    for i, name in enumerate(options, 1):
        print(f"  {i}. {name}")
    choice = input(f"Opcion [1-{len(options)}] (Enter = aleatorio): ").strip()

    if choice == "" or not choice.isdigit() or not (1 <= int(choice) <= len(options)):
        return "aleatorio"
    return options[int(choice) - 1]


def main():
    rows, cols = 35, 90

    selection = choose_pattern()

    if selection == "aleatorio":
        grid = random_grid(rows, cols, density=0.22)
    else:
        grid = make_grid(rows, cols)
        pattern = PATTERNS[selection]
        max_dr = max(p[0] for p in pattern)
        max_dc = max(p[1] for p in pattern)
        row_offset = max(0, (rows - max_dr) // 2)
        col_offset = max(0, (cols - max_dc) // 2)
        place_pattern(grid, pattern, row_offset, col_offset)

    generation = 0
    try:
        while True:
            population = sum(sum(row) for row in grid)
            clear_screen()
            print(render(grid, generation, population))

            if population == 0:
                print("\nTodas las celulas han muerto.")
                break

            grid = step(grid)
            generation += 1
            time.sleep(0.1)
    except KeyboardInterrupt:
        clear_screen()
        print("Simulacion detenida. Hasta la proxima!")


if __name__ == "__main__":
    main()
