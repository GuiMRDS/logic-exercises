import random
import os


class TicTacToe:
    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.done = ""

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_board(self):
        print("\n")

        for i in range(3):
            print(f" {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} ")

            if i < 2:
                print("-----------")

        print("\n")

    def check_win_or_draw(self):
        # Verificar vitória do X e O
        for symbol in ["X", "O"]:

            # Linhas
            for i in range(3):
                if (
                    self.board[i][0] == symbol and
                    self.board[i][1] == symbol and
                    self.board[i][2] == symbol
                ):
                    self.done = symbol
                    print(f"{symbol} venceu!")
                    return

            # Colunas
            for j in range(3):
                if (
                    self.board[0][j] == symbol and
                    self.board[1][j] == symbol and
                    self.board[2][j] == symbol
                ):
                    self.done = symbol
                    print(f"{symbol} venceu!")
                    return

            # Diagonal principal
            if (
                self.board[0][0] == symbol and
                self.board[1][1] == symbol and
                self.board[2][2] == symbol
            ):
                self.done = symbol
                print(f"{symbol} venceu!")
                return

            # Diagonal secundária
            if (
                self.board[0][2] == symbol and
                self.board[1][1] == symbol and
                self.board[2][0] == symbol
            ):
                self.done = symbol
                print(f"{symbol} venceu!")
                return

        # Verificar empate
        filled_spaces = 0

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != " ":
                    filled_spaces += 1

        if filled_spaces == 9:
            self.done = "draw"
            print("Empate!")

    def get_player_move(self):
        while True:
            try:
                print("Digite a linha (0, 1 ou 2):")
                x = int(input())

                print("Digite a coluna (0, 1 ou 2):")
                y = int(input())

                # Validar coordenadas
                if x < 0 or x > 2 or y < 0 or y > 2:
                    print("Coordenadas inválidas!\n")
                    continue

                # Validar posição ocupada
                if self.board[x][y] != " ":
                    print("Essa posição já está ocupada!\n")
                    continue

                self.board[x][y] = "X"
                break

            except ValueError:
                print("Digite apenas números inteiros!\n")

    def get_computer_move(self):
        available_moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    available_moves.append((i, j))

        if len(available_moves) > 0:
            x, y = random.choice(available_moves)
            self.board[x][y] = "O"


# =========================
# EXECUÇÃO DO JOGO
# =========================

game = TicTacToe()

while True:
    game.clear_screen()
    game.print_board()

    while game.done == "":
        # Jogador
        game.get_player_move()

        game.clear_screen()
        game.print_board()

        game.check_win_or_draw()

        if game.done != "":
            break

        # Computador
        print("Computador jogando...\n")

        game.get_computer_move()

        game.clear_screen()
        game.print_board()

        game.check_win_or_draw()

    print("\nDigite 1 para sair")
    print("Digite qualquer outra coisa para jogar novamente")

    option = input()

    if option == "1":
        print("Encerrando jogo...")
        break

    game.reset_board()