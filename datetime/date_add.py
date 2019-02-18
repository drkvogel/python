#!/usr/bin/env python3

import sys
from datetime import timedelta, datetime

# start = '30/05/18'
# date = datetime.strptime(start, '%d/%m/%y')
# print(date + timedelta(days=30*6))

# for idx, arg in enumerate(sys.argv):
#     print(idx, arg)

def usage():
    print('Usage: %s <datestring> <days>' % sys.argv[0])
    print('<datestring>: string in format dd/mm/yy')
    exit(0)

if len(sys.argv) != 3:
    usage()

date = sys.argv[1]
days = sys.argv[2]

# print(datetime.strptime('30/05/18', '%d/%m/%y') + timedelta(days=30*6))
try:
    print(datetime.strptime(date, '%d/%m/%y') + timedelta(days=int(days)))
except ValueError:
    usage()

