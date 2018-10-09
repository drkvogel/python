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

class Hangman_UI:
    # how to make abstract?
    def __init__(self,):
        pass

    def print_title(self, title):
        pass

    def print_status(self, hidden_word, missed_letters, guessed_letters):
        pass

    def get_input(self):
        pass

class Cmdline_UI(Hangman_UI):
    def __init__(self):
        pass    # ??

    def print_title(self, title):
        print(title)

    def print_status(self, hidden_word, missed_letters, guessed_letters):
        print()
        print(board[len(missed_letters)])

        print("Word: " + hidden_word)

        print("Letters missed:  ", end="")
        for letter in missed_letters:
            print(letter, end="")
        print()

        print("Letters guessed: ", end="")
        for letter in guessed_letters:
            print(letter, end="")
        print()
    
    def get_input(self):
        print()
        print("Guess a letter: ", end="")
        return get_char()

class Curses_UI(Hangman_UI):
    YPOS_TITLE = 0
    YPOS_LIVES = 1
    YPOS_WORD = 3
    YPOS_MISSED = 5
    YPOS_GUESSED = 6
    
    # def __enter__(self):
    #     # ?
    #     pass

    # def __exit__(self, type, value, traceback):
    #     curses.nocbreak()
    #     curses.echo()
    #     curses.endwin()
    #     self.stdscr.keypad(False)

    def __init__(self):
        try:
            # set up curses environment
            self.stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.stdscr.keypad(True)
        except:
            print("Unexpected error:", sys.exc_info()[0])
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
        
        missed = "Letters missed: "
        for letter in missed_letters:
            missed += letter
        self.stdscr.addstr(Curses_UI.YPOS_MISSED, 0, rpad(missed))
        
        guessed = "Letters guessed: "
        for letter in guessed_letters:
            guessed += letter
        
        self.stdscr.addstr(Curses_UI.YPOS_GUESSED, 0, rpad(guessed))
        self.stdscr.refresh()

    def get_input(self):
        return self.stdscr.getch()

def rpad(string, width=80):
    num = width - len(string)
    return string + ' '*num

class Hangman:
    def __init__(self, word, ui):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []
        self.ui = ui
        self.ui.print_title("Hangman by Chris Bird (chrisjbird@gmail.com")
    
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
            return
        return False

    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    def get_input(self):
        return self.ui.get_input()

    def print_status(self):
        self.ui.print_status(self.hide_word(), self.missed_letters, self.guessed_letters)

def rand_word():
    with open("words_alpha.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def get_char():
    if "_func" not in get_char.__dict__:         # figure out which function to use once, and store it in _func
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
    name = input("Enter your name to start [" + default + "]: ")
    if name == "":
        name = default

    print("(f)ullscreen, (s)crolling, or (q)uit? ")
    while True:
        option = get_char()
        if option == 'f':
            # with Curses_UI as ui:
                # ui = Curses_UI()
            ui = Curses_UI()
            game = Hangman(rand_word(), ui)
            break
        elif option == 's':
            ui = Cmdline_UI()
            game = Hangman(rand_word(), ui)
            break
        elif option == 'q':
            import sys
            sys.exit(0)     # what about cleaning up the ui?
    
    game = Hangman(rand_word(), ui)
    
    while not game.over():
        game.print_status()
        while True:
            user_input = game.get_input()
            if user_input not in [None, os.linesep]:    # don't make the ui check this - but the game maybe should
                break
        game.guess(user_input)
    
    print()
    print()
    if game.won():
        print("Congratulations")
    else:
        print("You lost")
        print("The word was " + game.word)

    print("Goodbye")
