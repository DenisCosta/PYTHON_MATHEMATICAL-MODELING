# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:16:47 2019

@author: 
        Prof. Dr. Denis C. L. Costa

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
        Representação Gráfica de Sinais utilizando o Método de Fourier
    
"""
# Importando Bibliotecas
# Biblioteca numpy: Matemática de alto Nível
import numpy as np

# Biblioteca matplot: Gráficos
import matplotlib.pyplot as plt

##########################################################
# Variáveis de Controle

T0 = 0                       # Instante Inicial

T1 = 2*np.pi                 # Instante Final

t = np.linspace(T0,T1,100)   # Intervalo de análise

# Representação Algébrica do Sinal

S = 2 + -1.27323954473516*np.sin(3.14159265358979*t) - 3.05311331771918e-16*np.cos(3.14159265358979*t)+\
    -0.636619772367581*np.sin(6.28318530717959*t) - 3.12250225675825e-16*np.cos(6.28318530717959*t)+\
    -0.424413181578388*np.sin(9.42477796076938*t) - 3.12250225675825e-16*np.cos(9.42477796076938*t)+\
    -0.318309886183791*np.sin(12.5663706143592*t) - 3.12250225675825e-16*np.cos(12.5663706143592*t)

# Representação Gráfica do Sinal

plt.plot(t,S)
plt.xlabel('Tempo')
plt.ylabel('Frequência')
plt.grid(True)
plt.show() 

##########################################################
print(' ')
print(' ===== Fim do Programa fourier_002 ====')