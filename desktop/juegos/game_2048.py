import tkinter as tk
import random


# ============================================================
# CONFIGURACIÓN
# ============================================================

BOARD_SIZE = 4

BG_COLOR = "#faf8ef"
BOARD_COLOR = "#bbada0"

TILE_COLORS = {
    0: ("#cdc1b4", "#776e65"),
    2: ("#eee4da", "#776e65"),
    4: ("#ede0c8", "#776e65"),
    8: ("#f2b179", "#f9f6f2"),
    16: ("#f59563", "#f9f6f2"),
    32: ("#f67c5f", "#f9f6f2"),
    64: ("#f65e3b", "#f9f6f2"),
    128: ("#edcf72", "#f9f6f2"),
    256: ("#edcc61", "#f9f6f2"),
    512: ("#edc850", "#f9f6f2"),
    1024: ("#edc53f", "#f9f6f2"),
    2048: ("#edc22e", "#f9f6f2"),
}


# ============================================================
# LÓGICA DEL 2048
# ============================================================

class Game2048:

    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [
            [0 for _ in range(BOARD_SIZE)]
            for _ in range(BOARD_SIZE)
        ]

        self.score = 0
        self.game_over = False
        self.won = False

        self.add_random_tile()
        self.add_random_tile()

    def empty_cells(self):
        cells = []

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                if self.board[row][col] == 0:
                    cells.append((row, col))

        return cells

    def add_random_tile(self):
        cells = self.empty_cells()

        if not cells:
            return

        row, col = random.choice(cells)

        self.board[row][col] = (
            4 if random.random() < 0.1 else 2
        )

    def compress(self, row):
        return [
            value
            for value in row
            if value != 0
        ]

    def merge(self, row):

        result = []
        index = 0

        while index < len(row):

            if (
                index + 1 < len(row)
                and row[index] == row[index + 1]
            ):
                new_value = row[index] * 2

                result.append(new_value)

                self.score += new_value

                if new_value == 2048:
                    self.won = True

                index += 2

            else:
                result.append(row[index])
                index += 1

        return result

    def process_row(self, row):

        row = self.compress(row)

        row = self.merge(row)

        while len(row) < BOARD_SIZE:
            row.append(0)

        return row

    def move_left(self):

        changed = False

        for row in range(BOARD_SIZE):

            old = self.board[row].copy()

            new = self.process_row(old)

            self.board[row] = new

            if old != new:
                changed = True

        return changed

    def move_right(self):

        changed = False

        for row in range(BOARD_SIZE):

            old = self.board[row].copy()

            reversed_row = old[::-1]

            new = self.process_row(reversed_row)

            new.reverse()

            self.board[row] = new

            if old != new:
                changed = True

        return changed

    def move_up(self):

        changed = False

        for col in range(BOARD_SIZE):

            old = [
                self.board[row][col]
                for row in range(BOARD_SIZE)
            ]

            new = self.process_row(old)

            for row in range(BOARD_SIZE):
                self.board[row][col] = new[row]

            if old != new:
                changed = True

        return changed

    def move_down(self):

        changed = False

        for col in range(BOARD_SIZE):

            old = [
                self.board[row][col]
                for row in range(BOARD_SIZE)
            ]

            reversed_column = old[::-1]

            new = self.process_row(reversed_column)

            new.reverse()

            for row in range(BOARD_SIZE):
                self.board[row][col] = new[row]

            if old != new:
                changed = True

        return changed

    def can_move(self):

        # Espacios disponibles
        if self.empty_cells():
            return True

        # Horizontal
        for row in range(BOARD_SIZE):

            for col in range(BOARD_SIZE - 1):

                if (
                    self.board[row][col]
                    == self.board[row][col + 1]
                ):
                    return True

        # Vertical
        for row in range(BOARD_SIZE - 1):

            for col in range(BOARD_SIZE):

                if (
                    self.board[row][col]
                    == self.board[row + 1][col]
                ):
                    return True

        return False

    def move(self, direction):

        if self.game_over:
            return

        if direction == "left":
            changed = self.move_left()

        elif direction == "right":
            changed = self.move_right()

        elif direction == "up":
            changed = self.move_up()

        elif direction == "down":
            changed = self.move_down()

        else:
            return

        if changed:
            self.add_random_tile()

        if not self.can_move():
            self.game_over = True


# ============================================================
# INTERFAZ 2048
# ============================================================

class Game2048Screen:

    def __init__(self, root, back_to_menu):

        self.root = root
        self.back_to_menu = back_to_menu

        self.game = Game2048()

        self.create_screen()

        self.root.bind(
            "<Key>",
            self.handle_key
        )

        self.update_board()

        self.root.focus_force()

    # ========================================================
    # LIMPIAR
    # ========================================================

    def clear(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # ========================================================
    # PANTALLA
    # ========================================================

    def create_screen(self):

        self.clear()

        header = tk.Frame(
            self.root,
            bg=BG_COLOR
        )

        header.pack(
            fill="x",
            padx=25,
            pady=20
        )

        tk.Label(
            header,
            text="2048",
            font=("Arial", 38, "bold"),
            fg="#776e65",
            bg=BG_COLOR
        ).pack(side="left")

        score_frame = tk.Frame(
            header,
            bg="#bbada0",
            padx=15,
            pady=5
        )

        score_frame.pack(side="right")

        tk.Label(
            score_frame,
            text="PUNTOS",
            font=("Arial", 9, "bold"),
            fg="#eee4da",
            bg="#bbada0"
        ).pack()

        self.score_label = tk.Label(
            score_frame,
            text="0",
            font=("Arial", 17, "bold"),
            fg="white",
            bg="#bbada0"
        )

        self.score_label.pack()

        # Tablero
        self.board_frame = tk.Frame(
            self.root,
            bg=BOARD_COLOR,
            padx=8,
            pady=8
        )

        self.board_frame.pack(
            padx=20,
            pady=10
        )

        self.tiles = []

        for row in range(BOARD_SIZE):

            tile_row = []

            for col in range(BOARD_SIZE):

                label = tk.Label(
                    self.board_frame,
                    text="",
                    width=5,
                    height=2,
                    font=("Arial", 24, "bold")
                )

                label.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5
                )

                tile_row.append(label)

            self.tiles.append(tile_row)

        # Botones
        buttons = tk.Frame(
            self.root,
            bg=BG_COLOR
        )

        buttons.pack(pady=15)

        tk.Button(
            buttons,
            text="Nueva partida",
            font=("Arial", 11, "bold"),
            bg="#8f7a66",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.new_game
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            buttons,
            text="Menú",
            font=("Arial", 11),
            relief="flat",
            cursor="hand2",
            command=self.go_to_menu
        ).pack(
            side="left",
            padx=5
        )

        tk.Label(
            self.root,
            text="Flechas o W A S D",
            font=("Arial", 10),
            fg="#776e65",
            bg=BG_COLOR
        ).pack()

    # ========================================================
    # ACTUALIZAR
    # ========================================================

    def update_board(self):

        for row in range(BOARD_SIZE):

            for col in range(BOARD_SIZE):

                value = self.game.board[row][col]

                background, foreground = TILE_COLORS.get(
                    value,
                    ("#3c3a32", "#f9f6f2")
                )

                text = "" if value == 0 else str(value)

                if value >= 1000:
                    font = ("Arial", 18, "bold")
                elif value >= 100:
                    font = ("Arial", 21, "bold")
                else:
                    font = ("Arial", 24, "bold")

                self.tiles[row][col].configure(
                    text=text,
                    bg=background,
                    fg=foreground,
                    font=font
                )

        self.score_label.configure(
            text=str(self.game.score)
        )

        if self.game.won:
            self.show_message(
                "¡2048!",
                "¡Has conseguido la ficha 2048!"
            )

            self.game.won = False

        elif self.game.game_over:
            self.show_message(
                "Game Over",
                f"Puntuación: {self.game.score}"
            )

    # ========================================================
    # MENSAJE
    # ========================================================

    def show_message(self, title, message):

        popup = tk.Toplevel(self.root)

        popup.title(title)
        popup.geometry("300x200")

        popup.resizable(False, False)

        popup.configure(
            bg="#776e65"
        )

        popup.transient(self.root)
        popup.grab_set()

        tk.Label(
            popup,
            text=title,
            font=("Arial", 26, "bold"),
            fg="white",
            bg="#776e65"
        ).pack(pady=25)

        tk.Label(
            popup,
            text=message,
            font=("Arial", 12),
            fg="white",
            bg="#776e65"
        ).pack()

        tk.Button(
            popup,
            text="Continuar",
            command=popup.destroy,
            bg="#edc22e",
            fg="white",
            relief="flat",
            cursor="hand2"
        ).pack(pady=20)

    # ========================================================
    # TECLADO
    # ========================================================

    def handle_key(self, event):

        key = event.keysym.lower()

        directions = {
            "left": "left",
            "a": "left",

            "right": "right",
            "d": "right",

            "up": "up",
            "w": "up",

            "down": "down",
            "s": "down"
        }

        if key in directions:

            self.game.move(
                directions[key]
            )

            self.update_board()

    # ========================================================
    # NUEVA PARTIDA
    # ========================================================

    def new_game(self):

        self.game.reset()

        self.update_board()

        self.root.focus_force()

    # ========================================================
    # VOLVER AL MENÚ
    # ========================================================

    def go_to_menu(self):

        self.root.unbind("<Key>")

        self.back_to_menu()
