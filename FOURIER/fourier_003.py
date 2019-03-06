# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:48:12 2019

@author: 
        Prof. Dr. Denis C. L. Costa
        
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Aplicações da Tranformada de Fourier 01
        


"""
# Importando Bibliotecas
# Biblioteca numpy: Matemática de alto Nível

import numpy as np

# Biblioteca matplot: Plotagem em 2D
import matplotlib.pyplot as pyplt

##########################################################
# Variáveis de Controle
arr = np.arange (100) 
print(arr)
NDFT = np . fft.fft ( np.sin(arr)) 
print(NDFT)
ffreq = np.fft.fftfreq (arr.shape [-1])
print(ffreq)

##########################################################
# Representação Gráfica da Transformda de Fourier

pyplt.plot(ffreq, NDFT.real, ffreq, NDFT.imag)
pyplt.plot(ffreq, NDFT.real)
pyplt.grid() 

#Legenda para o eixo X
pyplt.xlabel('Intervalo de Análise')

#Legenda para o eixo Y
pyplt.ylabel('Amplitude Transformada')

#Legenda no topo da figura
pyplt.title('Aplicações de Fourie')
pyplt.show (True) 
pyplt.plot(ffreq, NDFT.imag)
pyplt.grid() 

#Legenda para o eixo X
pyplt.xlabel('Intervalo de Análise')

#Legenda para o eixo Y
pyplt.ylabel('Amplitude Simples')

#Legenda no topo da figura
pyplt.title('Aplicações de Fourie')
pyplt.show (True) 

##########################################################
print(' ')
print(' ===== Fim do Programa fourier_003 ====')
