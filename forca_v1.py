# -*- coding: utf-8 -*-

# Curso de Python - Lab 03
# Projeto: Jogo da Forca
# Autor: Fabio Araujo

# Imports
import random
import os

# Classe principal do Jogo da FORCA
class Hangman:

    # Construtor da Classe
    def __init__(self, word):
        self.word = word
        self.stage = 0
        self.letters = []
        self.word_print = []

        for l in range(len(self.word)):
            self.word_print.append('_')

    # Método para adivinhar a letra e preencher as lacunas com as letras corretas
    def guess(self):
        print('Letras Digitadas: ' + str(self.letters))
        letter = input('Digite uma letra: ').upper()
        if letter in self.letters:
            print('Você já digitou essa letra')
        else:
            self.letters.append(letter)
            if letter in self.word:
                self.set_word_print(letter)
            else:
                self.stage = self.stage + 1

    def set_word_print(self, letter):
        for l in range(len(self.word)):
            if self.word[l] == letter:
                self.word_print[l] = letter

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.stage > 6

    # Método para verificar se o jogador vendeu
    def hangman_won(self):
        return self.word == self.load_word_print().replace(' ', '')

    def load_word_print(self):
        word = ''
        for w in self.word_print[::]:
            word = word + w + ' '
        return word

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_rest_line(self):
        rest_line_size = 40
        word_size = len(self.word)
        rest_line = self.load_word_print()
        for space in range(rest_line_size - (2 * word_size) - 2):
            rest_line = rest_line + ' '
        return rest_line + '*'

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        self.clear_screen()
        print('***********************************************************************')
        print('*                            Jogo da Forca                            *')
        print('***********************************************************************')
        print('*                                                                     *')
        print('*                                                                     *')
        if (self.stage == 0):
            print('*                            +--------+                               *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                      ------+-------                                 *')
            print('*                                                                     *')
            print('*                      Palavra: ' + self.get_rest_line())
            print('*                                                                     *')
            print('***********************************************************************')
            print('***********************************************************************')
        elif (self.stage == 1):
            print('*                            +--------+                               *')
            print('*                            |        :                               *')
            print('*                            |        O                               *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                      ------+-------                                 *')
            print('*                                                                     *')
            print('*                      Palavra: ' + self.get_rest_line())
            print('*                                                                     *')
            print('***********************************************************************')
            print('***********************************************************************')
        elif (self.stage == 2):
            print('*                            +--------+                               *')
            print('*                            |        :                               *')
            print('*                            |        O                               *')
            print('*                            |        |                               *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                      ------+-------                                 *')
            print('*                                                                     *')
            print('*                      Palavra: ' + self.get_rest_line())
            print('*                                                                     *')
            print('***********************************************************************')
            print('***********************************************************************')
        elif (self.stage == 3):
            print('*                            +--------+                               *')
            print('*                            |        :                               *')
            print('*                            |        O                               *')
            print('*                            |       /|                               *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                      ------+-------                                 *')
            print('*                                                                     *')
            print('*                      Palavra: ' + self.get_rest_line())
            print('*                                                                     *')
            print('***********************************************************************')
            print('***********************************************************************')
        elif (self.stage == 4):
            print('*                            +--------+                               *')
            print('*                            |        :                               *')
            print('*                            |        O                               *')
            print('*                            |       /|\\                              *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                            |                                        *')
            print('*                      ------+-------                                 *')
            print('*                                                                     *')
            print('*                      Palavra: ' + self.get_rest_line())
            print('*                                                                     *')
            print('***********************************************************************')
            print('***********************************************************************')
        elif (self.stage == 5):
            print('*                            +--------+                               *')
            print('*                            |        :                               *')
            print('*                            |        O                               *')
            print('*                            |       /|\\                              *')
            print('*                            |        .                               *')
            print('*                            |       /                                *')
            print('*                            |                                        *')
            print('*                      ------+-------                                 *')
            print('*                                                                     *')
            print('*                      Palavra: ' + self.get_rest_line())
            print('*                                                                     *')
            print('***********************************************************************')
            print('***********************************************************************')
        else:
            print('*                            +--------+                               *')
            print('*                            |        :                               *')
            print('*                            |        O                               *')
            print('*                            |       /|\\                              *')
            print('*                            |        .                               *')
            print('*                            |       / \                              *')
            print('*                            |                                        *')
            print('*                      ------+-------                                 *')
            print('*                                                                     *')
            print('*                      Palavra: ' + self.get_rest_line())
            print('*                                                                     *')
            print('***********************************************************************')
            print('***********************************************************************')


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open('palavras.txt', 'rt') as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank) - 1)].strip()


# Função Inicia o Programa
def main():
    # Objeto Jogo da Forca
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not (game.hangman_won() or game.hangman_over()):
        game.print_game_status()
        game.guess()
    else:
        game.print_game_status()
        # De acordo com o status, imprime mensagem na tela para o usuário
        if game.hangman_won():
            print('Parabéns! Você venceu!!!')
        else:
            print('Game over! Você perdeu!!!')
            print('A palavra era %s' % (game.word))


# Executa a função main()
if __name__ == '__main__':
    main()
