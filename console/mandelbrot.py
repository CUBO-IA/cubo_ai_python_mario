"""
Explorador interactivo del conjunto de Mandelbrot en la terminal.

Controles:
  w/a/s/d  -> mover la vista (arriba/izquierda/abajo/derecha)
  +/-      -> hacer zoom in / zoom out
  r        -> resetear la vista inicial
  c        -> cambiar paleta de colores
  q        -> salir

Ejecutar:
  python mandelbrot.py
"""

import os
import sys

# Paletas de color ANSI (256 colores) para pintar las iteraciones
PALETTES = [
    [16, 17, 18, 19, 20, 21, 27, 33, 39, 45, 51, 87, 123, 159, 195, 231],
    [16, 52, 88, 124, 160, 196, 202, 208, 214, 220, 226, 227, 228, 229, 230, 231],
    [16, 22, 28, 34, 40, 46, 82, 118, 154, 190, 226, 227, 228, 229, 230, 231],
    [16, 54, 56, 58, 90, 92, 126, 128, 160, 162, 196, 198, 199, 200, 201, 213],
]

ASCII_RAMP = " .:-=+*#%@"


def mandelbrot_escape(cx, cy, max_iter):
    """Devuelve el numero de iteraciones antes de escapar (o max_iter si no escapa)."""
    x, y = 0.0, 0.0
    x2, y2 = 0.0, 0.0
    i = 0
    while x2 + y2 <= 4.0 and i < max_iter:
        y = 2 * x * y + cy
        x = x2 - y2 + cx
        x2 = x * x
        y2 = y * y
        i += 1
    return i


def render(center_x, center_y, scale, width, height, max_iter, palette_idx):
    """Renderiza el fractal como una lista de lineas con codigos de color ANSI."""
    palette = PALETTES[palette_idx % len(PALETTES)]
    aspect_fix = 0.5  # los caracteres de terminal son ~2x mas altos que anchos
    lines = []
    for row in range(height):
        chars = []
        cy = center_y + (row - height / 2) * scale * aspect_fix
        for col in range(width):
            cx = center_x + (col - width / 2) * scale
            it = mandelbrot_escape(cx, cy, max_iter)
            if it >= max_iter:
                chars.append("\x1b[48;5;16m \x1b[0m")
            else:
                ramp_pos = int((it / max_iter) * (len(ASCII_RAMP) - 1))
                color_pos = int((it / max_iter) * (len(palette) - 1))
                ch = ASCII_RAMP[ramp_pos]
                color = palette[color_pos]
                chars.append(f"\x1b[38;5;{color}m{ch}\x1b[0m")
        lines.append("".join(chars))
    return "\n".join(lines)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_key():
    """Lee una sola tecla sin esperar Enter (Windows y Unix)."""
    try:
        import msvcrt
        return msvcrt.getch().decode("utf-8", errors="ignore").lower()
    except ImportError:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()


def main():
    width, height = 100, 42
    center_x, center_y = -0.5, 0.0
    scale = 3.0 / width
    max_iter = 80
    palette_idx = 0

    while True:
        clear_screen()
        print(render(center_x, center_y, scale, width, height, max_iter, palette_idx))
        print(
            f"centro=({center_x:.6f}, {center_y:.6f})  zoom={1/scale:.1f}x  "
            f"iter={max_iter}  paleta={palette_idx+1}/{len(PALETTES)}"
        )
        print("[w/a/s/d] mover  [+/-] zoom  [r] reset  [c] paleta  [q] salir")

        key = get_key()

        move_step = scale * width * 0.2
        if key == "w":
            center_y -= move_step * 0.5
        elif key == "s":
            center_y += move_step * 0.5
        elif key == "a":
            center_x -= move_step
        elif key == "d":
            center_x += move_step
        elif key == "+":
            scale /= 1.6
            max_iter = min(1000, int(max_iter * 1.15) + 1)
        elif key == "-":
            scale *= 1.6
            max_iter = max(50, int(max_iter / 1.15))
        elif key == "r":
            center_x, center_y = -0.5, 0.0
            scale = 3.0 / width
            max_iter = 80
        elif key == "c":
            palette_idx += 1
        elif key == "q":
            clear_screen()
            print("Hasta la proxima exploracion fractal!")
            break


if __name__ == "__main__":
    main()
