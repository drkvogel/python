#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inquirer
import re # needed?
import pprint

# text
questions = [
  inquirer.Text('name', message="What's your name"),
  inquirer.Text('surname', message="What's your surname"),
  inquirer.Text('phone', message="What's your phone number",
                # validate=lambda _, x: re.match('\+?\d[\d ]+\d', x), # none of these return True
                # validate=lambda x: re.match('\+?\d[\d ]+\d', x),
                # validate=lambda _, x: re.match('.*', x),
                # validate=True,  # this works...
                validate=lambda x, _: re.match('^.*$', x), # nope
                # validate=lambda x, _: re.match('\+?\d[\d ]+\d', x), # no
                # validate=lambda x, _: re.match('\d+', x), # no
                )
]
answers = inquirer.prompt(questions)
pprint.pprint(answers)

# lists
questions = [
  inquirer.List('size',
                message="What size do you need?",
                choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
            ),
]
answers = inquirer.prompt(questions)
pprint.pprint(answers)

# checkbox
questions = [
  inquirer.Checkbox('interests',
                    message="What are you interested in?",
                    choices=['Computers', 'Books', 'Science', 'Nature', 'Fantasy', 'History'],
                    ),
]
answers = inquirer.prompt(questions)
pprint.pprint(answers)

# path
questions = [
  inquirer.Path('log_file',
                 message="Where logs should be located?",
                 path_type=inquirer.Path.DIRECTORY, # requires trailing slash for dirs
                ),
]
answers = inquirer.prompt(questions)
pprint.pprint(answers)

