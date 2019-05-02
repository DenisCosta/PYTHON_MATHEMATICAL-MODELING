# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:35:11 2019

@author: 
        Prof. Dr. Denis C. L. Costa
        
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Diagrama de Bode: Função de Transferência
        
Nome do sript: laplace_002

Disponível em:
    
"""
# Bibliotecas
from scipy import signal
import matplotlib.pyplot as plt

# Função de Tranferência: H(s) = 1000/(s + 1000)
sl= signal.lti([1000], [1 ,1000])
# Variáveis de Controle: 
# w (Frequência Angular), mag (Magnitude) e phase(Fase)
w, mag, phase = signal.bode(sl)

# Gráfico 01: mag = f(w)
plt.figure()
plt.semilogx(w,mag,'b')
plt.xlabel('Frequência (rad/s)')
plt.ylabel('Magnitude (dB)')
plt.title('Diagrama de Ganho')
plt.grid(which = 'both', axis = 'both')
plt.grid(True)
plt.margins(0, 0.1)
plt.show

print('========================================')

# Gráfico 02: phase = f(w)
plt.figure()
plt.semilogx(w,phase)
plt.xlabel('Frequência Angular (°/s)')
plt.ylabel('Fase (°)')
plt.title('Diagrama de Fase')
plt.grid(which = 'both', axis = 'both')
plt.grid(True)
plt.margins(0, 0.1)
plt.show

