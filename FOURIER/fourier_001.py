# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:47:27 2019

@author: 
        Prof. Dr. Denis C. L. Costa

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
       Análise de Sinais utilizando o Método de Fourier
    
"""
# Importando Bibliotecas
# Biblioteca numpy: Matemática de alto Nível

import numpy as np

# Biblioteca matplot: Plotagem em 2D
# import matplotlib.pyplot as plt

# Biblioteca sympy: Matemática Simbólica
import sympy as sy

##########################################################
# Variáveis de Controle

T0 = 0                  # Instante Inicial

T1 = 2 #*np.pi         # Instante Final

w = 2*np.pi/(T1-T0)    # Frequência Angular
 
n = 4                  # Número de Harmônicos

print('Número de Harmônicos =',n)

##########################################################
# Declarando a variável simbólica
t = sy.symbols('t') 

# Declarando a Função - Sinal
def f(t):
    return 2*t

# Declarando a amplitude Real do Sinal
def ao(t):
    return sy.integrate(f(t), (t, T0, T1))
print('ao =',ao(t))
# Declarando a amplitude Real do Sinal
def an(t):
    return sy.integrate(f(t)*sy.cos(n*w*t), (t, T0, T1))
print('an =',an(t))
# Declarando a amplitude Complexa do Sinal
def bn(t):
    return sy.integrate(f(t)*sy.sin(n*w*t), (t, T0, T1))
print('bn =',bn(t))
print('=================================================')

##########################################################
# Compondo a Função Resposta do Sinal
def Fn(t):
    return an(t)*sy.cos(n*w*t)+bn(t)*sy.sin(n*w*t)
print('Fn(t) é o Somatório no n-ésimo Harmônico')
print('Fn(t) =',Fn(t))
print('')
def a(t):
    return ao(t)/2
print('a(t)=ao(t)/2')
print('a(t) =',a(t))
print('')
print('S(t)=a(t) + Fn(t)')

##########################################################
print(' ')
print(' ===== Fim do Programa fourier_001 ====')





