
# cruft

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



    # bank = "one two three four five".split()


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

        # char = self.ui.get_input()
        # # print("char: ", char, ", ord: ", ord(char))
        # # print("os.linesep: ", os.linesep, ", ord: ", ord(os.linesep))
        # # if char not in "\n":
        # # if char not in os.linesep:
        # if char != os.linesep:
        #     return char

