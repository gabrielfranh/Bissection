# -*- coding: utf-8 -*-
# Algoritmo Método da Bisseção

# Gabriel Francisco Habermann  

import math    

def funcao (inicial):

   return pow(inicial,3) - (9 * inicial) + 3    # Definindo a função como x^3 - 9x + 3

a = float(input("Começo do intervalo: "))

b = float(input("Final do intervalo b: "))

precisao = float(input("Precisão: "))

print ('\n')

if (b - a ) < precisao:

   resultado = a

else:

   contador = 1

   F = funcao(a)

   while True:

      x = (a + b)/2

      print "Iteração: %d" % (contador)

      print "Valor de X: %f" % (x)

      print '\n'

      if F * funcao(x) > 0:

         a = x

      else:

         b = x

      if (b - a) <= precisao:

         resultado = (a + b)/2

         break

      contador = contador + 1

      

print 'Valor do resultado: %f' % (resultado)