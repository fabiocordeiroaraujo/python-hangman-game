# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.wrong_letters = []
        self.word_letters = []
        self.board_level = 0

    # Método para adivinhar a letra
    def guess(self, letter):
        upper_letter = letter.upper()
        if upper_letter in self.word and upper_letter not in self.word_letters:
            self.word_letters.append(upper_letter)
        elif upper_letter not in self.word and upper_letter not in self.wrong_letters:
            self.wrong_letters.append(upper_letter)
            self.board_level = self.board_level + 1
        else:
            print("\nLetra já informada!!!")

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or self.board_level == 6

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        return len(self.word) == len(self.word_letters)

    # Método para não mostrar a letra no board
    def hide_word(self):
        word_view = ""
        for letter in self.word:
            if letter in self.word_letters:
                word_view = word_view + letter + " "
            else:
                word_view = word_view + "_ "
        return word_view

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[self.board_level])
        print("Letras erradas: %s" % self.wrong_letters)
        print(self.hide_word())


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra
    # e faz a leitura do caracter
    while(not game.hangman_over()):
        # Verifica o status do jogo
        game.print_game_status()
        letter = input("\nAdivinhe uma letra da palavra mágica: ")
        game.guess(letter)

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        game.print_game_status()
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
