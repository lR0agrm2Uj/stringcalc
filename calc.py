# coding: utf-8

import re

def calc(str):
  str = str.encode('utf-8')

#  if re.match(r'^[0-9()+\-*/]$', str) == None: return False

  str = re.sub(r'[^0-9()+\-*/]', '', str)
  str = re.sub(r'^[*/]+', '', str)
  str = re.sub(r'[+\-*/]+$', '', str)
  str = re.sub(r'(-|\+|\*|\/]){2,}', '', str)
  str = re.sub(r'\(+([0-9]+)', r'(\1', str)
  str = re.sub(r'([0-9]+)\(', r'\1*(', str)

  if str.count('(') != str.count(')') : return None

  return eval(str)

def isExpression(str):
  return True

# Messages
import random

def errorMessages():
  errorMessages = (
    'Error1',
    'Error2',
    'Error3',
    'Error4',
  )
  l = len(errorMessages)
  i = random.randint(1, l) - 1

  return errorMessages[i]

# Main
import sys

if __name__ == '__main__':
  while True:
    tmp = raw_input('Enter expression(Type q quit): ')

    if len(tmp) == 0: continue
    if re.match(r'^[qQ]', tmp) != None: sys.exit(0)

    str = calc(tmp)
    if str == None or str == False : str = errorMessages()
    print str

  sys.exit(0)

# * End of calc.py *
