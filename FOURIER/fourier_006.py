# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:22:58 2019

@author: 
       Prof. Dr. Denis C. L. Costa
       
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
        Representação Gráfica de Sinais Periódicos em Série de Fourier
    
"""
# Importando Bibliotecas
import matplotlib.pyplot as pyplt
import numpy as np
from sympy import pi


# Representação Gráfica das Operações Combinadas

t = np.linspace(0*np.pi, 2*np.pi,20)
DT = 8*np.sin(t) - 4*np.sin(2*t) + 8*np.sin(3*t)/3
ET = 4*np.sin(t) - 2*np.sin(2*t) + 2
RT = 8*np.sin(t)/np.pi

pyplt.plot(t,DT,'r',t,ET,'b',t,RT,'k')
pyplt.grid(True)
pyplt.legend(["DT","ET","RT"],loc=2)
pyplt.show()

# Análise do Efeito do Pulso

n = np.linspace(0, 2,200)
y = (-pi*np.cos(2*n*np.pi)/n + np.sin(2*n*np.pi)/(2*n**2))
pyplt.plot(n,y,'g')
pyplt.grid(True)
pyplt.show()

##########################################################
print(' ')
print(' ===== Fim do Programa fourier_006 ====')