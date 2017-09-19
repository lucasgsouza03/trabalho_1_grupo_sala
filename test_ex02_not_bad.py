# -*- coding: utf-8 -*-
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# B. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
def not_bad(s):
  return

def test_ex02():
  print ('not_bad')
  assert not_bad('This movie is not so bad') == 'This movie is good'
  assert not_bad('This dinner is not that bad!') == 'This dinner is good!'
  assert not_bad('This tea is not hot') == 'This tea is not hot'
  assert not_bad("It's bad yet not") == "It's bad yet not"

