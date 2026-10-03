import tkinter as tk

from game_2048 import Game2048Screen
from sudoku import SudokuScreen


# ============================================================
# CONFIGURACIÓN
# ============================================================

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 650

BG_COLOR = "#faf8ef"
TEXT_COLOR = "#776e65"
BUTTON_COLOR = "#8f7a66"
BUTTON_HOVER = "#9f8b77"


class MainMenu:
    """Menú principal de la colección de juegos."""

    def __init__(self, root):
        self.root = root

        self.root.title("Mini Juegos")
        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        self.show_menu()

    # ========================================================
    # LIMPIAR PANTALLA
    # ========================================================

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ========================================================
    # MENÚ
    # ========================================================

    def show_menu(self):
        self.clear()

        # Título
        title = tk.Label(
            self.root,
            text="MINI JUEGOS",
            font=("Arial", 38, "bold"),
            fg=TEXT_COLOR,
            bg=BG_COLOR
        )

        title.pack(pady=(80, 10))

        subtitle = tk.Label(
            self.root,
            text="Elige un juego",
            font=("Arial", 16),
            fg=TEXT_COLOR,
            bg=BG_COLOR
        )

        subtitle.pack(pady=(0, 40))

        # Botón 2048
        button_2048 = tk.Button(
            self.root,
            text="🎲  2048",
            font=("Arial", 18, "bold"),
            width=18,
            height=2,
            bg=BUTTON_COLOR,
            fg="white",
            activebackground=BUTTON_HOVER,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.start_2048
        )

        button_2048.pack(pady=10)

        # Botón Sudoku
        button_sudoku = tk.Button(
            self.root,
            text="🔢  SUDOKU",
            font=("Arial", 18, "bold"),
            width=18,
            height=2,
            bg=BUTTON_COLOR,
            fg="white",
            activebackground=BUTTON_HOVER,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.start_sudoku
        )

        button_sudoku.pack(pady=10)

        # Separador
        tk.Label(
            self.root,
            text="",
            bg=BG_COLOR
        ).pack(pady=10)

        # Salir
        exit_button = tk.Button(
            self.root,
            text="SALIR",
            font=("Arial", 14),
            width=18,
            height=2,
            command=self.root.destroy,
            relief="flat",
            cursor="hand2"
        )

        exit_button.pack(pady=10)

        # Información
        info = tk.Label(
            self.root,
            text="Colección de juegos en Python",
            font=("Arial", 10),
            fg="#a09890",
            bg=BG_COLOR
        )

        info.pack(side="bottom", pady=25)

    # ========================================================
    # ABRIR 2048
    # ========================================================

    def start_2048(self):
        Game2048Screen(
            self.root,
            self.show_menu
        )

    # ========================================================
    # ABRIR SUDOKU
    # ========================================================

    def start_sudoku(self):
        SudokuScreen(
            self.root,
            self.show_menu
        )


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    root = tk.Tk()

    MainMenu(root)

    root.mainloop()


if __name__ == "__main__":
    main()
