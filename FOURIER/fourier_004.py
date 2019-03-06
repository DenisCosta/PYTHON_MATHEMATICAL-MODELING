# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:38:09 2019

@author: 
        Prof. Dr. Denis C. L. Costa
        
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Aplicações da Tranformada de Fourier 02

"""
# Importando Bibliotecas
import numpy as np

from numpy.fft import fft
import math
import matplotlib.pyplot as pyplt

               
# Definindo uma Função Trigonométrica de período T
n = 1               # Número de Harmônicos
T = 2.0            #Período de análise do sinal
w0 = 2*math.pi/T    # Frequência Angular

def sinal(t):
    return 2 + -1.27323954473516*np.sin(3.14159265358979*t) - 3.05311331771918e-16*np.cos(3.14159265358979*t)+\
    -0.636619772367581*np.sin(6.28318530717959*t) - 3.12250225675825e-16*np.cos(6.28318530717959*t)+\
    -0.424413181578388*np.sin(9.42477796076938*t) - 3.12250225675825e-16*np.cos(9.42477796076938*t)+\
    -0.318309886183791*np.sin(12.5663706143592*t) - 3.12250225675825e-16*np.cos(12.5663706143592*t)
    
    # return 1.0+2.0*np.cos(n*w0*t)+0.5*np.cos(2*n*w0*t)\
    # +1.0*np.sin(3*n*w0*t)+0.2*np.cos(10*n*w0*t)
    
fe = 50.0  # Frequência
te = 1/fe  # Instante de tempo
tempo = np.arange(start=0.0,stop=T,step=te)
amostras = sinal(tempo)
                
# Representação Gráfica

pyplt.figure(figsize=(8,4))
pyplt.plot(tempo,amostras,'r')
pyplt.xlabel('Tempo')
pyplt.ylabel('Sinal')
pyplt.title('Tranformada de Fourie')
pyplt.grid() 
pyplt.show (True) 

#######################################

N = tempo.size
tfd = fft(amostras)/N
freq = np.zeros(N)

for k in range(N): 
    freq[k] = k*1.0/T

spectro = np.absolute(tfd)
pyplt.figure(figsize=(10,4))
pyplt.vlines(freq,[0],spectro,'r')
pyplt.xlabel('f')
pyplt.ylabel('S')
pyplt.axis([-1,fe,0,spectro.max()])
pyplt.grid()
pyplt.show (True) 


#####################################

def tracerSpectro(function,fe):
    t = np.arange(start=0.0,stop=1.0,step=1.0/fe)
    amostras = t.copy()
    for k in range(t.size):
        amostras[k] = function(t[k])
    N = amostras.size
    tfd = fft(amostras)/N
    spectro = np.absolute(tfd)
    freq = np.arange(N)
    pyplt.figure(figsize=(10,4))
    pyplt.vlines(freq,[0],spectro,'r')
    pyplt.xlabel('f')
    pyplt.ylabel('S')
    pyplt.axis([-1,fe,0,spectro.max()])
    pyplt.grid()
    return tfd


tracerSpectro(sinal,22)
# tracerSpectre(signal,15)


#################################################

def sinal(t):
    if t < 0.5:
        return 1.0
    else:
        return -1.0
tfd = tracerSpectro(sinal,100)

#################################################
        
# Relatório
pmax = 20            
relatorio = np.zeros(pmax)
for p in range(pmax):
    relatorio[p] = abs(tfd[1])/abs(tfd[2*p+1])/(2*p+1)
            
print('Relatório :')
print('')
print(relatorio)

#################################################

tfd = tracerSpectro(sinal,500)
pmax = 20            
relatorio2 = np.zeros(pmax)
for p in range(pmax):
    relatorio2[p] = abs(tfd[1])/abs(tfd[2*p+1])/(2*p+1)
    
print('Relatório 2:')
print('')
print(relatorio2)

##########################################################
print(' ')
print(' ===== Fim do Programa fourier_004 ====')