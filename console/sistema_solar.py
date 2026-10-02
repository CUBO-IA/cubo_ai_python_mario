"""
Simulador de un sistema solar simplificado - fisica orbital real (gravitacion
newtoniana) animada en la terminal con ASCII art.

Usa unidades astronomicas: distancias en AU, tiempo en anios, masa en masas
solares. Con estas unidades la constante gravitacional es G = 4*pi^2, lo que
reproduce automaticamente la Tercera Ley de Kepler (T^2 = a^3) y permite
comprobar la conservacion de energia del sistema en vivo.

Integracion: Velocity Verlet (leapfrog), estable para orbitas periodicas.

Controles:
  Ctrl+C -> salir

Ejecutar:
  python sistema_solar.py
"""

import math
import os
import time

G = 4 * math.pi ** 2  # unidades: AU, anios, masas solares
EARTH_MASS_IN_SUN = 3.003e-6

# Datos orbitales reales (semieje mayor en AU, masa en masas terrestres, color ANSI, simbolo)
PLANETS = [
    # nombre,      a (AU), masa (M_tierra), color, simbolo
    ("Mercurio", 0.387, 0.0553, 244, "m"),
    ("Venus", 0.723, 0.815, 221, "v"),
    ("Tierra", 1.000, 1.000, 39, "T"),
    ("Marte", 1.524, 0.107, 203, "M"),
    ("Jupiter", 5.203, 317.8, 180, "J"),
]

TRAIL_LEN = 60
TRAIL_COLOR = 236


class Body:
    def __init__(self, name, mass, x, y, vx, vy, color, symbol):
        self.name = name
        self.mass = mass
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.ax, self.ay = 0.0, 0.0
        self.color = color
        self.symbol = symbol
        self.trail = []


def build_system(include_jupiter):
    bodies = []
    sun = Body("Sol", 1.0, 0.0, 0.0, 0.0, 0.0, 226, "O")
    bodies.append(sun)

    for name, a, mass_earth, color, symbol in PLANETS:
        if name == "Jupiter" and not include_jupiter:
            continue
        mass = mass_earth * EARTH_MASS_IN_SUN
        # orbita circular: v = sqrt(G*M_sol/a), velocidad perpendicular al radio
        v = math.sqrt(G * sun.mass / a)
        x, y = a, 0.0
        vx, vy = 0.0, v
        bodies.append(Body(name, mass, x, y, vx, vy, color, symbol))
    return bodies


def compute_accelerations(bodies, softening=1e-4):
    for b in bodies:
        b.ax, b.ay = 0.0, 0.0
    n = len(bodies)
    for i in range(n):
        bi = bodies[i]
        for j in range(i + 1, n):
            bj = bodies[j]
            dx = bj.x - bi.x
            dy = bj.y - bi.y
            dist2 = dx * dx + dy * dy + softening
            dist = math.sqrt(dist2)
            force = G / (dist2 * dist)
            bi.ax += force * bj.mass * dx
            bi.ay += force * bj.mass * dy
            bj.ax -= force * bi.mass * dx
            bj.ay -= force * bi.mass * dy


def velocity_verlet_step(bodies, dt):
    for b in bodies:
        b.x += b.vx * dt + 0.5 * b.ax * dt * dt
        b.y += b.vy * dt + 0.5 * b.ay * dt * dt
    old_ax = [b.ax for b in bodies]
    old_ay = [b.ay for b in bodies]
    compute_accelerations(bodies)
    for b, ax0, ay0 in zip(bodies, old_ax, old_ay):
        b.vx += 0.5 * (ax0 + b.ax) * dt
        b.vy += 0.5 * (ay0 + b.ay) * dt


def total_energy(bodies):
    kinetic = sum(0.5 * b.mass * (b.vx ** 2 + b.vy ** 2) for b in bodies)
    potential = 0.0
    n = len(bodies)
    for i in range(n):
        for j in range(i + 1, n):
            dx = bodies[j].x - bodies[i].x
            dy = bodies[j].y - bodies[i].y
            dist = math.sqrt(dx * dx + dy * dy) + 1e-9
            potential -= G * bodies[i].mass * bodies[j].mass / dist
    return kinetic + potential


def world_to_screen(x, y, half_range, width, height):
    aspect_fix = 0.5
    col = int(width / 2 + (x / half_range) * (width / 2))
    row = int(height / 2 + (y / half_range) * (height / 2) * aspect_fix)
    return row, col


def render(bodies, half_range, width, height, sim_years, energy_drift):
    grid = [[None] * width for _ in range(height)]

    for b in bodies:
        for (trow, tcol) in b.trail:
            if 0 <= trow < height and 0 <= tcol < width:
                if grid[trow][tcol] is None:
                    grid[trow][tcol] = (".", TRAIL_COLOR)

    for b in bodies:
        row, col = world_to_screen(b.x, b.y, half_range, width, height)
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = (b.symbol, b.color)

    lines = []
    for row in grid:
        chars = []
        for cell in row:
            if cell is None:
                chars.append(" ")
            else:
                ch, color = cell
                chars.append(f"\x1b[38;5;{color}m{ch}\x1b[0m")
        lines.append("".join(chars))

    header = (
        f"Tiempo simulado: {sim_years:6.2f} anios   "
        f"Deriva de energia: {energy_drift:+.4f}%   (Ctrl+C para salir)"
    )
    legend = "  ".join(f"\x1b[38;5;{c}m{s}\x1b[0m={n}" for n, _, _, c, s in
                        [("Sol", 0, 0, 226, "O")] + [(n, a, m, c, s) for n, a, m, c, s in PLANETS])
    return header + "\n" + "\n".join(lines) + "\n" + legend


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def ask_include_jupiter():
    print("Simulador de Sistema Solar (fisica orbital real)\n")
    answer = input("Incluir a Jupiter en la simulacion? [s/N]: ").strip().lower()
    return answer == "s"


def main():
    width, height = 100, 44
    include_jupiter = ask_include_jupiter()
    half_range = 6.2 if include_jupiter else 1.8

    bodies = build_system(include_jupiter)
    compute_accelerations(bodies)
    initial_energy = total_energy(bodies)

    dt = 0.004          # anios por paso de integracion
    steps_per_frame = 4  # pasos de fisica por frame dibujado
    sim_years = 0.0

    try:
        while True:
            for _ in range(steps_per_frame):
                velocity_verlet_step(bodies, dt)
                sim_years += dt

            for b in bodies:
                row, col = world_to_screen(b.x, b.y, half_range, width, height)
                b.trail.append((row, col))
                if len(b.trail) > TRAIL_LEN:
                    b.trail.pop(0)

            energy_now = total_energy(bodies)
            drift = 0.0
            if abs(initial_energy) > 1e-12:
                drift = (energy_now - initial_energy) / abs(initial_energy) * 100

            clear_screen()
            print(render(bodies, half_range, width, height, sim_years, drift))
            time.sleep(0.05)
    except KeyboardInterrupt:
        clear_screen()
        print("Simulacion detenida. Hasta la proxima orbita!")


if __name__ == "__main__":
    main()
