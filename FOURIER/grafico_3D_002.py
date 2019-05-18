# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:48:13 2019

INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PÁRA - IFPA ANANINDEUA

@author: 
        Prof. Dr. Denis C. L. Costa
                       
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Representação Gráfica de um Sinal - Parte II

Nome do sript: grafico_3D_002

Disponível em: 
    
"""
# Bibliotecas usadas no programa:
# Cálculo Matemático: numpy
import numpy as np
# Representação Gráfica 2D: matplotlib
import matplotlib.pyplot as plt
# Representação Gráfica 3D: mpl_toolkits.mplot3d
from mpl_toolkits.mplot3d import Axes3D

# Layout do Gráfico 3D:
# Opções de cores: cmap --> escolha a letra correspondente
a =  'Spectral'
b =  'seismic'
c =  'coolwarm'
d =  'PRGn'
e = 'RdYlBu'
f = 'RdGy' 
g = 'RdYlGn'
h = 'hot'

# Gráfico 01
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap= g)

# Gráfico 02
fig = plt.figure()
ax = Axes3D(fig)
X1 = np.arange(-4, 4, 0.25)
Y1 = np.arange(-4, 4, 0.25)
X1, Y1 = np.meshgrid(X1, Y1)
R1 = np.sqrt(X1**2 + Y1**2)
Z1 = np.sin(R1)
ax.plot_surface(X1, Y1, R1, cmap= a)




