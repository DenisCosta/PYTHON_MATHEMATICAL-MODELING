# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:29:15 2019

INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PÁRA - IFPA ANANINDEUA

@author: 
        Prof. Dr. Denis C. L. Costa
                       
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Representação Gráfica de um Sinal - Parte I

Nome do sript: grafico_3D_001

Disponível em: 
    
"""
# Bibliotecas usadas no programa:
# Cálculo Matemático: numpy
import numpy as np 
# Representação Gráfica: matplotlib
import matplotlib.pyplot as plt

# Representação algébrica do Sinal
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) *\
            np.exp(-x ** 2 - y ** 2)
            
    #return np.sin(x)**2+np.cos(y)**2

# Parâmetros
n = 15 # Número de Harmônicos
# Vetor do eixo x
x = np.linspace(-3, 3, 4 * n)
# Vetor do eixo y
y = np.linspace(-3, 3, 3 * n)
# Matriz da Energia do Sinal
X, Y = np.meshgrid(x, y)
# Representação Gráfica da Matriz da Energia do Sinal
plt.imshow(f(X, Y))