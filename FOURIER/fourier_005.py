# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:28:26 2019

@author: 
        Prof. Dr. Denis C. L. Costa
        
Grupode Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
        Representação de Sinais Periódicos em Série de Fourier

"""
# Importando Bibliotecas
from sympy import fourier_series, pi
from sympy.abc import t

# Sistemas Lineares Invariantes no Tempo (LIT)
s = fourier_series(2*t**1, (t, 0, pi))
print(s)

# Deslocamento Temporal
a = s.scale(2).truncate()

# Escalonamento Temporal
b = s.shift(2).truncate()

# Reversão Temporal 
c = s.sigma_approximation(2)
print('Deslocamento Temporal =',a)
print('Escalonamento Temporal =',b)
print('Reversão Temporal = ',c)


##########################################################
print(' ')
print(' ===== Fim do Programa fourier_005 ====')

