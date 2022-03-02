# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import board
import os

clear = lambda: os.system('clear')

# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word, language):
        self.word = word
        self.wrong_letters = []
        self.word_letters = []
        self.language = language
        self.board_level = 0

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or self.board_level == 6

    # Método para adivinhar a letra
    def guess(self, letter):
        upper_letter = letter.upper()
        if upper_letter in self.word and upper_letter not in self.word_letters:
            self.word_letters.append(upper_letter)
        elif upper_letter not in self.word and upper_letter not in self.wrong_letters:
            self.wrong_letters.append(upper_letter)
            self.board_level = self.board_level + 1
        else:
            letter_already_informed = ['\nLetter already informed!!!', '\nLetras ya informadas!!!', '\nLetra já informada!!!']           
            print(letter_already_informed[(int(self.language)) - 1])    

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        return "_" not in self.hide_word()

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
        clear()
        print(board.board[self.board_level])
        wrong_letters = ['Wrong letters: %s', 'Letras equivocadas: %s', 'Letras erradas: %s']                   
        print(wrong_letters[(int(self.language)) - 1] % self.wrong_letters)
        print(self.hide_word())


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word(language):
    if language == "1":
        with open("words/en.txt", "rt") as f:
            bank = f.readlines()
    elif language == "2":
        with open("words/es.txt", "rt") as f:
            bank = f.readlines()
    else:
        with open("words/pt-br.txt", "rt") as f:
            bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

# Função para selecionar o idioma preferido do jogador
def select_language():   
    print('\n')
    print('-----------------------------------------------------------------------------------------------------------')
    print('- Select the language -------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------------')    
    language = input('- English: 1 ----------------------------------------------------------------------------------------------\n- Spanish: 2 ----------------------------------------------------------------------------------------------\n- Portugues: 3 --------------------------------------------------------------------------------------------\n-----------------------------------------------------------------------------------------------------------\n-----------------------------------------------------------------------------------------------------------\n\n')
    return language

# Função Main - Execução do Programa
def main():

    # Limpa o console
    clear()    
    # Configura o idioma
    language = select_language()
    # Recupera a palavra secreta
    word = rand_word(language)
    # Cria o jogo
    game = Hangman(word, language)

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra
    # e faz a leitura do caracter
    while(not game.hangman_over()):
        # Verifica o status do jogo
        game.print_game_status()
        guess_a_letter = ['\nGuess a letter of the magic word: ', '\nAdivina una letra de la palabra mágica: ', '\nAdivinhe uma letra da palavra mágica: ']           
        letter = input(guess_a_letter[(int(language)) - 1])
        game.guess(letter)

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        game.print_game_status()
        congratulations = ['\nCongratulations! You won!', '\n¡Felicidades! ¡Ganaste!', '\nParabéns! Você venceu!']           
        print(congratulations[(int(language)) - 1])
    else:
        game_over = ['\nGame over! You lost!', '\n¡Juego terminado! ¡Tú perdiste!', '\nGame over! Você perdeu!']           
        print(game_over[(int(language)) - 1])       
        the_word_was = ['The word was ', 'La palabra era ', 'A palavra era ']           
        print(the_word_was[(int(language)) - 1] + game.word)


# Executa o programa
if __name__ == "__main__":
    main()
