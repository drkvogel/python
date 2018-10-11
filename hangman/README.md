
# Hangman

With a switchable UI - you can play from the command line, or with an `ncurses` text user interface (TUI).

To run:

    python hangman.py

or

    chmod u+x hangman.py
    ./hangman.py

## todo

blanked word should be spaced to show how many letters
shouldn't allow non-alphabetic (hyphens? show?)
curses ui
    messes up terminal regardless of finally block or with statement
use with keyword for curses ui
switchable rules?
    e.g. hard rules - already guessed or missed counts as a guess
vscode: Refactor failed. expected string or bytes-like object
i18n

## done

number of lives should be more when word is shorter?-x 8 is the game
game doesn't finish when you get it, now!
title printed twice on cmdline
cmdline: two single hearts before lose - lose() logic?
shouldn't return prompt on cmdline if guessed letter already guessed
should not accept guess if already in guessed or missed?