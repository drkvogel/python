#!/usr/bin/env python3

"""
Hangman
"""

import random
import curses
import getpass

board = ["❤️️️️❤️️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️", "❤️️️️"]

# class Hangman_UI:
#     def __init__(self,):
#         pass
    

#     def print_status(self):
#         pass

# class Cmdline_UI(Hangman_UI):
#     def __init__(self):
#         pass
#     def print_status(self, status):
#         pass
# class Curses_UI(Hangman_UI):
class Curses_UI():
    YPOS_TITLE = 0
    YPOS_LIVES = 1
    YPOS_WORD = 3
    YPOS_MISSED = 5
    YPOS_GUESSED = 6
    # def __init__(self,  scr):
    #     self.scr = scr
    # def print_title(self, title):
    #     stdscr.addstr(Curses_UI.YPOS_TITLE, 0, rpad(title))
    #     stdscr.refresh()

    # def print_status(self):
    #     stdscr.addstr(Curses_UI.YPOS_LIVES, 0, rpad(board[len(self.missed_letters)]))
    #     stdscr.addstr(Curses_UI.YPOS_WORD, 0, rpad(self.hide_word()))
    #     missed = "Letters missed: "
    #     for letter in self.missed_letters:
    #         missed += letter
    #     stdscr.addstr(Curses_UI.YPOS_MISSED, 0, rpad(missed))
    #     guessed = "Letters guessed: "
    #     for letter in self.guessed_letters:
    #         guessed += letter
    #     stdscr.addstr(Curses_UI.YPOS_TITLE, 0, rpad(guessed))
    #     stdscr.refresh()


def rpad(string, width=80):
    num = width - len(string)
    return string + ' '*num

class Hangman:
    def __init__(self, word, ui):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []
        self.ui = ui
        ui.print_title("Hangman by Chris Bird (chrisjbird@gmail.com")
    
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
        # print(board[len(self.missed_letters)])
        # print("Word: " + self.hide_word())
        # # print("len(word): ", len(self.word), ", len(hide_word): ", len(self.hide_word()))
        # print("Letters missed:  ", end="")
        # for letter in self.missed_letters:
        #     print(letter, end="")
        # print()
        # print("Letters guessed: ", end="")
        # for letter in self.guessed_letters:
        #     print(letter, end="")
        # print()
        # print(board[len(self.missed_letters)])
        stdscr.addstr(Curses_UI.YPOS_LIVES, 0, rpad(board[len(self.missed_letters)]))
        # print("Word: " + self.hide_word())
        stdscr.addstr(Curses_UI.YPOS_WORD, 0, rpad(self.hide_word()))
        # print("len(word): ", len(self.word), ", len(hide_word): ", len(self.hide_word()))
        missed = "Letters missed: "
        for letter in self.missed_letters:
            missed += letter
        stdscr.addstr(Curses_UI.YPOS_MISSED, 0, rpad(missed))
        # print("Letters guessed: ", end="")
        guessed = "Letters guessed: "
        for letter in self.guessed_letters:
            guessed += letter
        stdscr.addstr(Curses_UI.YPOS_TITLE, 0, rpad(guessed))
        stdscr.refresh()

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
    print ("Welcome to Hangman")
    default = getpass.getuser()
    name = input("Enter your name to start [" + default + "]: ")
    if name == "":
        name = default
    try:
        # set up curses environment
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        # play
        # play(name)
        main()
    finally:
        # restore command line environment
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()