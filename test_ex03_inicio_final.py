# -*- coding: utf-8 -*-
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# C. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
#  a-inicio + b-inicio + a-final + b-final
def inicio_final(a, b):
  return

def test_ex03():
  print ('inicio_final')
  assert inicio_final('abcd', 'xy') == 'abxcdy'
  assert inicio_final('abcde', 'xyz') == 'abcxydez'
  assert inicio_final('Kitten', 'Donut') == 'KitDontenut'

