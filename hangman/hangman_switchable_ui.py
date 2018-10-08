#!/usr/bin/env python3

"""
Hangman
"""

import random
import curses
import getpass

board = ["❤️️️️❤️️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️❤️️️️", "❤️️️️❤️️️️", "❤️️️️"]

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
        def getChar():
            if "_func" not in getChar.__dict__:         # figure out which function to use once, and store it in _func
                try:                                    # for Windows-based systems
                    import msvcrt                       # If successful, we are on Windows
                    getChar._func=msvcrt.getch
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
                    getChar._func=_ttyRead
            return getChar._func()

    def print_title(self, title):
        print(title)

    def print_status(self, hidden_word, missed_letters, guessed_letters):
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
        print(board[len(missed_letters)])

class Curses_UI(Hangman_UI):
    YPOS_TITLE = 0
    YPOS_LIVES = 1
    YPOS_WORD = 3
    YPOS_MISSED = 5
    YPOS_GUESSED = 6
    
    def __init__(self):
        # self.scr = scr

        try:
            # set up curses environment
            self.stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.stdscr.keypad(True)

            # play
            # main()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            # raise "Could not intialise Curses UI" # TypeError: exceptions must derive from BaseException
            print("Could not intialise Curses UI")
        finally:
            # restore command line environment
            curses.nocbreak()
            self.stdscr.keypad(False)
            curses.echo()
            curses.endwin()

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
            # print("letter: ", letter)
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    def get_input(self):
        return self.ui.get_input()

    def print_status(self):
        self.ui.print_status(self.word, self.missed_letters, self.guessed_letters)
        # stdscr.addstr(Curses_UI.YPOS_LIVES, 0, rpad(board[len(self.missed_letters)]))
        # # print("Word: " + self.hide_word())
        # stdscr.addstr(Curses_UI.YPOS_WORD, 0, rpad(self.hide_word()))
        # # print("len(word): ", len(self.word), ", len(hide_word): ", len(self.hide_word()))
        # missed = "Letters missed: "
        # for letter in self.missed_letters:
        #     missed += letter
        # stdscr.addstr(Curses_UI.YPOS_MISSED, 0, rpad(missed))
        # # print("Letters guessed: ", end="")
        # guessed = "Letters guessed: "
        # for letter in self.guessed_letters:
        #     guessed += letter
        # stdscr.addstr(Curses_UI.YPOS_TITLE, 0, rpad(guessed))
        # stdscr.refresh()

def rand_word():
    # bank = "one two three four five".split()
    with open("words_alpha.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

# def main():
#     ui = Curses_UI()
#     # ui = Cmdline_UI()
#     game = Hangman(rand_word(), ui)
#     while not game.over():
#         game.print_status()
#         # user_input = input("Enter a letter: ")
#         user_input = game.get_input()
#         game.guess(user_input)

#     # game.print_status()
#     if game.won():
#         print("Congratulations")
#     else:
#         print("You lost")
#     print("The word was " + game.word)

#     print("Goodbye")

if __name__ == "__main__":
    print ("Welcome to Hangman")
    default = getpass.getuser()
    name = input("Enter your name to start [" + default + "]: ")
    if name == "":
        name = default

    while True:
        option =  input("(f)ullscreen, (s)crolling, or (q)uit? ")
        if option == 'f':
            ui = Curses_UI()
            break
        elif option == 's':
            ui = Cmdline_UI()
            break
        elif option == 'q':
            break
    
    game = Hangman(rand_word(), ui)
    
    while not game.over():
        game.print_status()
        user_input = game.get_input()
        game.guess(user_input)

    if game.won():
        print("Congratulations")
    else:
        print("You lost")

    print("The word was " + game.word)
    print("Goodbye")


    # try:
    #     # set up curses environment
    #     stdscr = curses.initscr()
    #     curses.noecho()
    #     curses.cbreak()
    #     stdscr.keypad(True)

    #     # play
    #     main()
    # finally:
    #     # restore command line environment
    #     curses.nocbreak()
    #     stdscr.keypad(False)
    #     curses.echo()
    #     curses.endwin()