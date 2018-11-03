#!/usr/bin/env python3

from datetime import timedelta, datetime

# start = '30/05/18'
# date = datetime.strptime(start, '%d/%m/%y')
# print(date + timedelta(days=30*6))

print(datetime.strptime('30/05/18', '%d/%m/%y') + timedelta(days=30*6))