import tkinter as tk
import random


# ============================================================
# COLORES
# ============================================================

BG_COLOR = "#f4f1ea"
BOARD_COLOR = "#2f3542"

FIXED_COLOR = "#2f3542"
USER_COLOR = "#2563eb"

SELECTED_COLOR = "#dbeafe"
WHITE = "#ffffff"

GRID_LINE_COLOR = "#1f2937"


# ============================================================
# LÓGICA DEL SUDOKU
# ============================================================

class SudokuGame:

    def __init__(self):
        self.new_game()

    def new_game(self):

        self.solution = self.generate_solution()

        self.board = [
            row.copy()
            for row in self.solution
        ]

        self.remove_numbers()

        self.original = [
            row.copy()
            for row in self.board
        ]

        self.errors = 0

    # ========================================================
    # GENERAR SOLUCIÓN
    # ========================================================

    def generate_solution(self):

        board = [
            [0 for _ in range(9)]
            for _ in range(9)
        ]

        self.fill_board(board)

        return board

    def fill_board(self, board):

        empty = self.find_empty(board)

        if empty is None:
            return True

        row, col = empty

        numbers = list(range(1, 10))

        random.shuffle(numbers)

        for number in numbers:

            if self.is_valid(
                board,
                number,
                row,
                col
            ):

                board[row][col] = number

                if self.fill_board(board):
                    return True

                board[row][col] = 0

        return False

    def find_empty(self, board):

        for row in range(9):

            for col in range(9):

                if board[row][col] == 0:
                    return row, col

        return None

    def is_valid(
        self,
        board,
        number,
        row,
        col
    ):

        # Fila
        for c in range(9):

            if board[row][c] == number:
                return False

        # Columna
        for r in range(9):

            if board[r][col] == number:
                return False

        # Cuadrícula 3x3
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for r in range(
            start_row,
            start_row + 3
        ):

            for c in range(
                start_col,
                start_col + 3
            ):

                if board[r][c] == number:
                    return False

        return True

    # ========================================================
    # QUITAR NÚMEROS
    # ========================================================

    def remove_numbers(self):

        # 45 números eliminados
        cells_to_remove = 45

        positions = [
            (row, col)
            for row in range(9)
            for col in range(9)
        ]

        random.shuffle(positions)

        for row, col in positions[:cells_to_remove]:

            self.board[row][col] = 0

    # ========================================================
    # COLOCAR NÚMERO
    # ========================================================

    def set_number(self, row, col, number):

        # Casilla original
        if self.original[row][col] != 0:
            return "fixed"

        # Borrar
        if number == 0:

            self.board[row][col] = 0

            return "deleted"

        # Correcto
        if number == self.solution[row][col]:

            self.board[row][col] = number

            return "correct"

        # Incorrecto
        self.errors += 1

        return "wrong"

    # ========================================================
    # COMPLETADO
    # ========================================================

    def is_complete(self):

        for row in range(9):

            for col in range(9):

                if (
                    self.board[row][col]
                    != self.solution[row][col]
                ):
                    return False

        return True


# ============================================================
# INTERFAZ SUDOKU
# ============================================================

class SudokuScreen:

    def __init__(self, root, back_to_menu):

        self.root = root
        self.back_to_menu = back_to_menu

        self.game = SudokuGame()

        self.selected = None

        self.fullscreen = False

        self.create_screen()

        # Eventos
        self.root.bind(
            "<Key>",
            self.handle_key
        )

        self.root.bind(
            "<F11>",
            self.toggle_fullscreen
        )

        self.root.bind(
            "<Escape>",
            self.exit_fullscreen
        )

        self.root.bind(
            "<Configure>",
            self.on_resize
        )

        self.root.focus_force()

        self.draw_board()

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

        # Contenedor principal
        self.main_frame = tk.Frame(
            self.root,
            bg=BG_COLOR
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # ====================================================
        # ENCABEZADO
        # ====================================================

        self.header = tk.Frame(
            self.main_frame,
            bg=BG_COLOR
        )

        self.header.pack(
            fill="x",
            padx=30,
            pady=(20, 5)
        )

        self.title_label = tk.Label(
            self.header,
            text="SUDOKU",
            font=("Arial", 32, "bold"),
            fg=FIXED_COLOR,
            bg=BG_COLOR
        )

        self.title_label.pack(
            side="left"
        )

        self.error_label = tk.Label(
            self.header,
            text="Errores: 0",
            font=("Arial", 13, "bold"),
            fg="#dc2626",
            bg=BG_COLOR
        )

        self.error_label.pack(
            side="right"
        )

        # ====================================================
        # INSTRUCCIONES
        # ====================================================

        self.instructions = tk.Label(
            self.main_frame,
            text=(
                "Selecciona una casilla y escribe un número "
                "del 1 al 9"
            ),
            font=("Arial", 11),
            fg="#64748b",
            bg=BG_COLOR
        )

        self.instructions.pack(
            pady=5
        )

        # ====================================================
        # CONTENEDOR DEL TABLERO
        # ====================================================

        self.board_container = tk.Frame(
            self.main_frame,
            bg=BG_COLOR
        )

        self.board_container.pack(
            fill="both",
            expand=True
        )

        # Canvas para poder adaptar el tablero
        self.canvas = tk.Canvas(
            self.board_container,
            bg=BG_COLOR,
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        self.canvas.bind(
            "<Configure>",
            self.on_canvas_resize
        )

        # ====================================================
        # BOTONES
        # ====================================================

        self.bottom_frame = tk.Frame(
            self.main_frame,
            bg=BG_COLOR
        )

        self.bottom_frame.pack(
            pady=(5, 20)
        )

        self.new_button = tk.Button(
            self.bottom_frame,
            text="Nueva partida",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.new_game
        )

        self.new_button.pack(
            side="left",
            padx=5
        )

        self.delete_button = tk.Button(
            self.bottom_frame,
            text="Borrar",
            font=("Arial", 11),
            relief="flat",
            cursor="hand2",
            command=self.delete_number
        )

        self.delete_button.pack(
            side="left",
            padx=5
        )

        self.fullscreen_button = tk.Button(
            self.bottom_frame,
            text="Pantalla completa",
            font=("Arial", 11),
            relief="flat",
            cursor="hand2",
            command=self.toggle_fullscreen
        )

        self.fullscreen_button.pack(
            side="left",
            padx=5
        )

        self.menu_button = tk.Button(
            self.bottom_frame,
            text="Menú",
            font=("Arial", 11),
            relief="flat",
            cursor="hand2",
            command=self.go_to_menu
        )

        self.menu_button.pack(
            side="left",
            padx=5
        )

        self.help_label = tk.Label(
            self.main_frame,
            text=(
                "Flechas: mover  •  1-9: colocar  •  "
                "Backspace: borrar  •  F11: pantalla completa"
            ),
            font=("Arial", 9),
            fg="#64748b",
            bg=BG_COLOR
        )

        self.help_label.pack(
            pady=(0, 10)
        )

    # ========================================================
    # DIBUJAR TABLERO
    # ========================================================

    def draw_board(self):

        if not hasattr(self, "canvas"):
            return

        self.canvas.delete("all")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width <= 1 or height <= 1:
            return

        # Dejamos un pequeño margen
        margin = 20

        available_width = width - margin * 2
        available_height = height - margin * 2

        # El tablero siempre será cuadrado
        board_size = min(
            available_width,
            available_height
        )

        if board_size <= 0:
            return

        x0 = (width - board_size) / 2
        y0 = (height - board_size) / 2

        cell_size = board_size / 9

        # ====================================================
        # CASILLAS
        # ====================================================

        for row in range(9):

            for col in range(9):

                left = x0 + col * cell_size
                top = y0 + row * cell_size

                right = left + cell_size
                bottom = top + cell_size

                # Fondo
                if self.selected == (row, col):

                    background = SELECTED_COLOR

                else:

                    background = WHITE

                self.canvas.create_rectangle(
                    left,
                    top,
                    right,
                    bottom,
                    fill=background,
                    outline="#cbd5e1",
                    width=1
                )

                value = self.game.board[row][col]

                if value != 0:

                    if self.game.original[row][col] != 0:
                        color = FIXED_COLOR
                    else:
                        color = USER_COLOR

                    # Tamaño dinámico
                    font_size = max(
                        12,
                        int(cell_size * 0.48)
                    )

                    self.canvas.create_text(
                        (left + right) / 2,
                        (top + bottom) / 2,
                        text=str(value),
                        fill=color,
                        font=(
                            "Arial",
                            font_size,
                            "bold"
                        )
                    )

        # ====================================================
        # LÍNEAS 3x3
        # ====================================================

        for i in range(10):

            # Vertical
            x = x0 + i * cell_size

            line_width = 3 if i % 3 == 0 else 1

            self.canvas.create_line(
                x,
                y0,
                x,
                y0 + board_size,
                fill=GRID_LINE_COLOR,
                width=line_width
            )

            # Horizontal
            y = y0 + i * cell_size

            self.canvas.create_line(
                x0,
                y,
                x0 + board_size,
                y,
                fill=GRID_LINE_COLOR,
                width=line_width
            )

        # ====================================================
        # ACTUALIZAR INFORMACIÓN
        # ====================================================

        self.error_label.configure(
            text=f"Errores: {self.game.errors}"
        )

    # ========================================================
    # CLICK SOBRE EL TABLERO
    # ========================================================

    def on_canvas_click(self, event):

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        margin = 20

        available_width = width - margin * 2
        available_height = height - margin * 2

        board_size = min(
            available_width,
            available_height
        )

        x0 = (width - board_size) / 2
        y0 = (height - board_size) / 2

        # Fuera del tablero
        if (
            event.x < x0
            or event.x > x0 + board_size
            or event.y < y0
            or event.y > y0 + board_size
        ):
            return

        cell_size = board_size / 9

        col = int(
            (event.x - x0) / cell_size
        )

        row = int(
            (event.y - y0) / cell_size
        )

        if 0 <= row < 9 and 0 <= col < 9:

            self.selected = (
                row,
                col
            )

            self.draw_board()

            self.root.focus_force()

    # ========================================================
    # REDIMENSIONAR
    # ========================================================

    def on_resize(self, event):

        self.draw_board()

    def on_canvas_resize(self, event):

        self.draw_board()

    # ========================================================
    # TECLADO
    # ========================================================

    def handle_key(self, event):

        if self.selected is None:
            return

        row, col = self.selected

        key = event.keysym

        # Número
        if key in "123456789":

            number = int(key)

            result = self.game.set_number(
                row,
                col,
                number
            )

            if result == "wrong":

                self.show_wrong_number()

            elif result == "correct":

                if self.game.is_complete():

                    self.show_victory()

        # Borrar
        elif key in (
            "BackSpace",
            "Delete",
            "0"
        ):

            self.game.set_number(
                row,
                col,
                0
            )

        # Movimiento
        elif key in (
            "Left",
            "Right",
            "Up",
            "Down"
        ):

            self.move_selection(key)

        self.draw_board()

    # ========================================================
    # MOVER SELECCIÓN
    # ========================================================

    def move_selection(self, key):

        if self.selected is None:

            self.selected = (0, 0)

            return

        row, col = self.selected

        if key == "Left":
            col = max(0, col - 1)

        elif key == "Right":
            col = min(8, col + 1)

        elif key == "Up":
            row = max(0, row - 1)

        elif key == "Down":
            row = min(8, row + 1)

        self.selected = (
            row,
            col
        )

    # ========================================================
    # BORRAR
    # ========================================================

    def delete_number(self):

        if self.selected is None:
            return

        row, col = self.selected

        self.game.set_number(
            row,
            col,
            0
        )

        self.draw_board()

        self.root.focus_force()

    # ========================================================
    # NÚMERO INCORRECTO
    # ========================================================

    def show_wrong_number(self):

        popup = tk.Toplevel(self.root)

        popup.title("Sudoku")

        popup.geometry(
            "320x170"
        )

        popup.resizable(
            False,
            False
        )

        popup.transient(
            self.root
        )

        popup.grab_set()

        tk.Label(
            popup,
            text="Número incorrecto",
            font=("Arial", 18, "bold"),
            fg="#dc2626"
        ).pack(
            pady=25
        )

        tk.Label(
            popup,
            text=(
                "Ese número no corresponde\n"
                "a esta casilla."
            ),
            font=("Arial", 11)
        ).pack()

        tk.Button(
            popup,
            text="Aceptar",
            command=popup.destroy,
            relief="flat"
        ).pack(
            pady=15
        )

    # ========================================================
    # VICTORIA
    # ========================================================

    def show_victory(self):

        popup = tk.Toplevel(self.root)

        popup.title(
            "¡Sudoku completado!"
        )

        popup.geometry(
            "360x240"
        )

        popup.resizable(
            False,
            False
        )

        popup.transient(
            self.root
        )

        popup.grab_set()

        tk.Label(
            popup,
            text="🎉 ¡Felicidades!",
            font=("Arial", 24, "bold"),
            fg="#2563eb"
        ).pack(
            pady=30
        )

        tk.Label(
            popup,
            text=(
                "Has completado el Sudoku.\n\n"
                f"Errores: {self.game.errors}"
            ),
            font=("Arial", 12)
        ).pack()

        tk.Button(
            popup,
            text="Nueva partida",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            relief="flat",
            command=lambda: [
                popup.destroy(),
                self.new_game()
            ]
        ).pack(
            pady=20
        )

    # ========================================================
    # NUEVA PARTIDA
    # ========================================================

    def new_game(self):

        self.game.new_game()

        self.selected = None

        self.draw_board()

        self.root.focus_force()

    # ========================================================
    # PANTALLA COMPLETA
    # ========================================================

    def toggle_fullscreen(self, event=None):

        self.fullscreen = not self.fullscreen

        self.root.attributes(
            "-fullscreen",
            self.fullscreen
        )

        if self.fullscreen:

            self.fullscreen_button.configure(
                text="Salir de pantalla completa"
            )

        else:

            self.fullscreen_button.configure(
                text="Pantalla completa"
            )

        self.root.after(
            100,
            self.draw_board
        )

    # ========================================================
    # SALIR DE PANTALLA COMPLETA
    # ========================================================

    def exit_fullscreen(self, event=None):

        if self.fullscreen:

            self.fullscreen = False

            self.root.attributes(
                "-fullscreen",
                False
            )

            self.fullscreen_button.configure(
                text="Pantalla completa"
            )

            self.root.after(
                100,
                self.draw_board
            )

    # ========================================================
    # VOLVER AL MENÚ
    # ========================================================

    def go_to_menu(self):

        self.root.unbind("<Key>")
        self.root.unbind("<F11>")
        self.root.unbind("<Escape>")
        self.root.unbind("<Configure>")

        self.back_to_menu()
