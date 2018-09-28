#!/usr/bin/env python3

"""
Hangman
"""

import random

board = ["❤️️️️❤️️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️", "❤️️️️"]

class Hangman:
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []
        print("len(board): ", len(board))
    
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True
    
    def over(self):
        # print("len(self.missed): ", len(self.missed_letters), ", len(board): ", len(board))
        return self.won() or len(self.missed_letters) == len(board)

    def won(self):
        if '_' not in self.hide_word():
            return True
        return False

    def hide_word(self):
        rtn = ''
        for letter in self.word:
            # print("letter: ", letter)
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    def print_status(self):
        print(board[len(self.missed_letters)])
        print("Word: " + self.hide_word())
        # print("len(word): ", len(self.word), ", len(hide_word): ", len(self.hide_word()))
        print("Letters missed:  ", end="")
        for letter in self.missed_letters:
            print(letter, end="")
        print()
        print("Letters guessed: ", end="")
        for letter in self.guessed_letters:
            print(letter, end="")
        print()

def rand_word():
    # bank = "one two three four five".split()
    with open("words_alpha.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def main():
    game = Hangman(rand_word())
    while not game.over():
        game.print_status()
        user_input = input("Enter a letter: ")
        game.guess(user_input)

    # game.print_status()
    if game.won():
        print("Congratulations")
    else:
        print("You lost")
    print("The word was " + game.word)

    print("Goodbye")

if __name__ == "__main__":
    main()
