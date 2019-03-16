# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:48:13 2019

@author: 
        Prof. Dr. Denis C. L. Costa

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
       Representação Gráfica da Distribuição de Densidade  
       
"""

# Bibliotecas

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


#===================================================
fig = plt.figure()
ax = Axes3D(fig)
X1 = np.arange(-5, 5, 0.25)
Y1 = np.arange(-5, 5, 0.25)
X1, Y1 = np.meshgrid(X1, Y1)
R1 = X1**2 + Y1**2
#===================================================
ax.set_xlabel('Valores de x')
ax.set_ylabel('Valores de y')
ax.set_zlabel('Densidade')
ax.set_title('Distribuição de Densidade')
ax.plot_surface(X1, Y1, R1, cmap='seismic')

#===================================================
# cmaps[opções de cores]:
#'PiYG', 'PRGn', 'BrBG', 'PuOr',
# 'RdGy', 'RdBu', 'RdYlBu', 'RdYlGn', 
#'Spectral', 'coolwarm', 'bwr',
# 'seismic'


