"""
Simulador de evolucion genetica en la terminal.

Una poblacion de "criaturas" (strings aleatorios) evoluciona generacion tras
generacion -mediante seleccion, cruce y mutacion- hasta converger en una
frase objetivo. Inspirado en el "programa de la comadreja" de Richard
Dawkins, pero con seleccion por torneo, cruce y elitismo (un algoritmo
genetico real, no solo mutacion pura).

El color de cada caracter imita el feedback de Wordle:
  verde  -> letra correcta en la posicion correcta
  gris   -> letra incorrecta

Controles:
  Ctrl+C -> salir en cualquier momento

Ejecutar:
  python evolucion_genetica.py
"""

import os
import random
import string
import time

CHARSET = string.ascii_letters + string.digits + " .,!?'-:;"

POP_SIZE = 200
MUTATION_RATE = 0.012
TOURNAMENT_SIZE = 5
ELITE_COUNT = 2
SHOWCASE = 6  # cuantos individuos de la poblacion se muestran cada frame

GREEN = "\x1b[38;5;46m"
GRAY = "\x1b[38;5;240m"
RESET = "\x1b[0m"
CYAN = "\x1b[38;5;51m"


def build_charset(target):
    charset = set(CHARSET)
    charset.update(target)
    return "".join(sorted(charset))


def random_individual(length, charset):
    return "".join(random.choice(charset) for _ in range(length))


def fitness(individual, target):
    return sum(1 for a, b in zip(individual, target) if a == b)


def tournament_select(population, fitnesses):
    best = None
    best_fit = -1
    for _ in range(TOURNAMENT_SIZE):
        idx = random.randrange(len(population))
        if fitnesses[idx] > best_fit:
            best_fit = fitnesses[idx]
            best = population[idx]
    return best


def crossover(parent_a, parent_b):
    point = random.randrange(1, len(parent_a))
    return parent_a[:point] + parent_b[point:]


def mutate(individual, charset):
    chars = list(individual)
    for i in range(len(chars)):
        if random.random() < MUTATION_RATE:
            chars[i] = random.choice(charset)
    return "".join(chars)


def next_generation(population, fitnesses, charset):
    ranked = sorted(zip(population, fitnesses), key=lambda p: -p[1])
    new_population = [ind for ind, _ in ranked[:ELITE_COUNT]]

    while len(new_population) < len(population):
        parent_a = tournament_select(population, fitnesses)
        parent_b = tournament_select(population, fitnesses)
        child = crossover(parent_a, parent_b)
        child = mutate(child, charset)
        new_population.append(child)

    return new_population


def colorize(individual, target):
    out = []
    for ch, target_ch in zip(individual, target):
        if ch == target_ch:
            out.append(f"{GREEN}{ch}{RESET}")
        else:
            out.append(f"{GRAY}{ch}{RESET}")
    return "".join(out)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def render(generation, population, fitnesses, target, best_history):
    ranked = sorted(zip(population, fitnesses), key=lambda p: -p[1])
    best_ind, best_fit = ranked[0]
    avg_fit = sum(fitnesses) / len(fitnesses)
    length = len(target)

    bar_width = 40
    filled = int((best_fit / length) * bar_width)
    bar = "#" * filled + "-" * (bar_width - filled)

    lines = []
    lines.append(f"Objetivo:    {CYAN}{target}{RESET}")
    lines.append(f"Generacion:  {generation}")
    lines.append(f"Mejor fit:   [{bar}] {best_fit}/{length} ({best_fit/length*100:.1f}%)")
    lines.append(f"Fit promedio poblacion: {avg_fit:.2f}/{length}")
    lines.append("")
    lines.append("Mejores individuos de esta generacion:")
    for ind, fit in ranked[:SHOWCASE]:
        lines.append(f"  {colorize(ind, target)}   ({fit}/{length})")
    lines.append("")
    lines.append("Historial del mejor fitness (ultimas 30 generaciones):")
    sparkline = sparkline_from_history(best_history, length)
    lines.append("  " + sparkline)
    lines.append("")
    lines.append("(Ctrl+C para salir)")
    return "\n".join(lines)


def sparkline_from_history(history, max_value):
    ramp = " .:-=+*#%@"
    recent = history[-60:]
    chars = []
    for value in recent:
        pos = int((value / max_value) * (len(ramp) - 1))
        chars.append(ramp[pos])
    return "".join(chars)


def main():
    print("Evolucion genetica de una frase objetivo\n")
    target = input("Escribe la frase objetivo (Enter = frase por defecto): ").strip()
    if not target:
        target = "METHINKS IT IS LIKE A WEASEL"

    charset = build_charset(target)
    length = len(target)

    population = [random_individual(length, charset) for _ in range(POP_SIZE)]
    generation = 0
    best_history = []

    try:
        while True:
            fitnesses = [fitness(ind, target) for ind in population]
            best_fit = max(fitnesses)
            best_history.append(best_fit)

            clear_screen()
            print(render(generation, population, fitnesses, target, best_history))

            if best_fit == length:
                print("\nObjetivo alcanzado! La poblacion convergio por completo.")
                break

            population = next_generation(population, fitnesses, charset)
            generation += 1
            time.sleep(0.08)
    except KeyboardInterrupt:
        clear_screen()
        print("Evolucion detenida. Hasta la proxima generacion!")


if __name__ == "__main__":
    main()
