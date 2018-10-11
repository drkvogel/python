#!/usr/bin/env python3

"""
Hangman
"""

import os
import random
import curses
import getpass
import backtrace

# nicer looking (and more informative?) backtraces
backtrace.hook(reverse=False, align=False, strip_path=False, enable_on_envvar_only=False, on_tty=False, conservative=False, styles={})

# 8 lives in hangman? https://en.wikipedia.org/wiki/Hangman_(game)
board = ["❤️️️️❤️️️️❤️️️️❤️️️️❤️️️️❤️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️❤️️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️", "❤️️️️"]
DICTIONARY_FILE = "words_alpha.txt"

class Hangman_UI:
    # how to make abstract?
    def __init__(self,):
        pass

    def print_title(self, title):
        pass

    def print_status(self, hidden_word, missed_letters, guessed_letters):
        pass

    def get_char(self):
        pass

class Cmdline_UI(Hangman_UI):
    def print_title(self, title):
        print(title)

    def print_status(self, hidden_word, missed_letters, guessed_letters):
        print()
        print(board[len(missed_letters)])

        print("Word: " + hidden_word)

        print("Correct:   ", end="")
        for letter in guessed_letters:
            print(letter, end="")
        print()

        print("Incorrect: ", end="")
        for letter in missed_letters:
            print(letter, end="")
        print()
    
    def get_letter(self, ignore=""):
        print()
        print("Guess a letter: ", end="")
        while True:
            char = get_char()
            if char != os.linesep and char not in ignore and char.isalpha():
                print(char)
                return char

class Curses_UI(Hangman_UI):
    RULESET_EASY, RULESET_HARD = range(2)   # https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python

    YPOS_TITLE = 0
    YPOS_LIVES = 1
    YPOS_WORD = 3
    YPOS_MISSED = 5
    YPOS_GUESSED = 6
    
    def __enter__(self):
        # ?
        pass

    def __exit__(self, type, value, traceback):
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        self.stdscr.keypad(False)

    def __init__(self):
        try:
            # set up curses environment
            self.stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.stdscr.keypad(True)
        except:
            print("Error: ", sys.exc_info()[0])
            print("Could not intialise Curses UI")
            # raise "Could not intialise Curses UI" # TypeError: exceptions must derive from BaseException
        finally:
            # restore command line environment
            curses.nocbreak()
            curses.echo()
            curses.endwin()
            self.stdscr.keypad(False)

    def print_title(self, title):
        self.stdscr.addstr(Curses_UI.YPOS_TITLE, 0, rpad(title))
        self.stdscr.refresh()

    def print_status(self, hidden_word, missed_letters, guessed_letters):
        self.stdscr.addstr(Curses_UI.YPOS_LIVES, 0, rpad(board[len(missed_letters)]))
        self.stdscr.addstr(Curses_UI.YPOS_WORD, 0, rpad(hidden_word))
        
        guessed = "Correct: "
        for letter in guessed_letters:
            guessed += letter
        self.stdscr.addstr(Curses_UI.YPOS_GUESSED, 0, rpad(guessed))

        missed = "Incorrect: "
        for letter in missed_letters:
            missed += letter
        self.stdscr.addstr(Curses_UI.YPOS_MISSED, 0, rpad(missed))
    
        self.stdscr.refresh()

    def get_char(self):
        return self.stdscr.getch()

def rpad(string, width=80):
    num = width - len(string)
    return string + ' '*num

class Hangman:
    def __init__(self, word, ui):
        self.word = word
        self.missed_letters = []
        self.ui = ui    # ??
        self.guessed_letters = []
        self.ui.print_title("Hangman by Chris Bird (chrisjbird@gmail.com)")

    def guess(self, letter):
        if letter not in [None, os.linesep]:
            if letter in self.word and letter not in self.guessed_letters:
                self.guessed_letters.append(letter)
            elif letter not in self.word and letter not in self.missed_letters:
                self.missed_letters.append(letter)
            else:
                return False
        return True
    
    def over(self):
        return self.won() or len(self.missed_letters) == len(board)

    def won(self):
        if '_' not in self.hide_word():
            return True
        return False

    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    def get_letter(self):
        return self.ui.get_letter(self.missed_letters + self.guessed_letters)

    def print_status(self):
        self.ui.print_status(self.hide_word(), self.missed_letters, self.guessed_letters)

def rand_word():
    with open(DICTIONARY_FILE, "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def get_char():                                 # there must(?) be a slight overhead to doing this, but it works
    if "_func" not in get_char.__dict__:        # figure out which function to use once, and store it in _func
        try:                                    # for Windows-based systems
            import msvcrt                       # If successful, we are on Windows
            get_char._func=msvcrt.getch
        except ImportError:                     # for POSIX-based systems (with termios & tty support)
            import tty, sys, termios            # raises ImportError if unsupported
            def _ttyRead():
                fd = sys.stdin.fileno()
                oldSettings = termios.tcgetattr(fd)
                try:
                    tty.setcbreak(fd)
                    answer = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)
                return answer
            get_char._func=_ttyRead
    return get_char._func()

if __name__ == "__main__":
    print ("Welcome to Hangman")

    default = getpass.getuser()
    name = input("Enter your name to start (default is your system username: " + default + "): ")
    if name == "":
        name = default

    print("(f)ullscreen, (s)crolling, or (q)uit? ")
    while True:
        option = get_char()
        if option == 'f':
            with Curses_UI() as ui:
                game = Hangman(rand_word(), ui)
            break
        elif option == 's':
            ui = Cmdline_UI()
            game = Hangman(rand_word(), ui)
            break
        elif option == 'q':
            import sys
            sys.exit(0)     # what about cleaning up the ui? There is no ui if we're here
    
    while not game.over():
        game.print_status()
        while True:
            letter = game.get_letter()
            if letter != None and game.guess(letter):   # first clause unnecessary now??
                break
    
    print() # ??
    if game.won():
        print("Congratulations")
    else:
        print("You lost")
    
    print("The word was " + game.word)
    print("Goodbye")
