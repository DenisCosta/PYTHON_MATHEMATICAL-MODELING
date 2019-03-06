# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:12:33 2019

@author:  
        Prof. Dr. Denis C. L. Costa

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
        Estratégia de Convolução Aplicada à Análise de Sistemas Lineares


Adaptado do artigo de José Alexandre Nalon: Interpretação da Convolução

"""

# Importa as bibliotecas necessárias

import numpy as np

 
###############################################################################
# Funções auxiliares
 
# Função delta de Kroenecker; Pulso
def delta(n):
    return np.where(n==0, 1.0, 0.0)
 
def x(n):
    return 2*delta(n) + delta(n-1) - delta(n-2)
 
def h(n):
    return delta(n) - delta(n-1)
 
###############################################################################
# Funções do Sistema de Convoluções
    
n = np.arange(-2.0, 6.0)       # Intervalo de análise: -2 <= n <= 5
x0 = 2*delta(n)                # Decomposição de x[n] em impulsos deslocados
x1 = delta(n-1)
x2 = - delta(n-2)
x3 = - delta(n-3)
y = 2*h(n) + h(n-1) - h(n-2)   # Resposta da convolução
 
###############################################################################
# Representação Gráfica

fig = figure(1)
fig.set_size_inches((15.0, 10.0))
 
a = fig.add_subplot(4, 2, 1)
a.stem(n, x0, "k-", "ko", "k-")
a.set_xlim([ -2, 5 ])
a.set_ylim([ -2.1, 2.1 ])
a.set_ylabel("$x[0]\delta[n]$", rotation="horizontal")
a.set_xticks(n)
a.set_xticklabels([])
a.set_yticks([])
 
a = fig.add_subplot(4, 2, 2)
at = a.twinx()
a.stem(n, 2*h(n), "k-", "ko", "k-")
a.set_xlim([ -2, 5 ])
a.set_xticks(n)
a.set_xticklabels([])
a.set_ylim([ -2.1, 2.1 ])
a.set_yticks([])
at.set_ylim([ -2.1, 2.1 ])
at.set_ylabel("$2h[n]$", rotation="horizontal")
at.set_yticks([])
 
a = fig.add_subplot(4, 2, 3)
a.stem(n, x1, "k-", "ko", "k-")
a.set_xlim([ -2, 5 ])
a.set_ylim([ -2.1, 2.1 ])
a.set_ylabel("$x[1]\delta[n-1]$", rotation="horizontal")
a.set_xticks([])
a.set_xticklabels([])
a.set_yticks([])
 
a = fig.add_subplot(4, 2, 4)
at = a.twinx()
a.stem(n, h(n-1), "k-", "ko", "k-")
a.set_xlim([ -2, 5 ])
a.set_xticks(n)
a.set_xticklabels([])
a.set_ylim([ -2.1, 2.1 ])
a.set_yticks([])
at.set_ylim([ -2.1, 2.1 ])
at.set_ylabel("$h[n-1]$", rotation="horizontal")
at.set_yticks([])
 
a = fig.add_subplot(4, 2, 5)
a.stem(n, x2, "k-", "ko", "k-")
a.set_xlim([ -2, 5 ])
a.set_ylim([ -2.1, 2.1 ])
a.set_ylabel("$x[2]\delta[n-2]$", rotation="horizontal")
a.set_xticks([])
a.set_yticks([])
 
a = fig.add_subplot(4, 2, 6)
at = a.twinx()
a.stem(n, -h(n-2), "k-", "ko", "k-")
a.set_xlim([ -2, 5 ])
a.set_xticks(n)
a.set_xticklabels([])
a.set_ylim([ -2.1, 2.1 ])
a.set_yticks([])
at.set_ylim([ -2.1, 2.1 ])
at.set_ylabel("$-h[n-3]$", rotation="horizontal")
at.set_yticks([])

a = fig.add_subplot(4, 2, 7)
a.stem(n, x3, "k-", "ko", "k-")
a.set_xlim([ -2, 5 ])
a.set_ylim([ -2.1, 2.1 ])
a.set_ylabel("$x[3]\delta[n-3]$", rotation="horizontal")
a.set_xticks(n)
a.set_yticks([])

a = fig.add_subplot(4, 2, 8)
at = a.twinx()
a.stem(n, y, "k-", "ko", "k-")
a.set_xlim([ -2, 5 ])
a.set_xticks(n)
a.set_ylim([ -2.1, 2.1 ])
at.set_ylim([ -2.1, 2.1 ])
at.set_ylabel("$y[n]$", rotation="horizontal")
at.set_yticks([])
 
###############################################################################
# Salva a figura.
savefig("ConvolutionShift.png", bbox_inches='tight')

###############################################################################
print(' ')
print(' ===== Fim do Programa convolucao2 ====')