
# Hangman

With a switchable UI - you can play from the command line, or with an `ncurses` text user interface (TUI).

## todo

curses ui messes up terminal regardless of finally block or with statement
shouldn't return prompt on cmdline if guessed letter already guessed
i18n
use with keyword for curses ui
cmdline: two single hearts before lose - lose() logic?
should not accept guess if already in guessed or missed?
    hard rules - switchable rules?
vscode: Refactor failed. expected string or bytes-like object

## done

number of lives should be more when word is shorter?-x 8 is the game
game doesn't finish when you get it, now!
title printed twice on cmdline