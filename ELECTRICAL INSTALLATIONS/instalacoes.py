# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:47:12 2019

@author: Prof. Dr. Denis C. L. Costa
    
    Instalações Elétricas
        Simulação computacional

Script 02: instalacoes

Disponível em:


"""

# Análise Temporal das Tensões Elétricas
# Bibliotecas Utilizadas
import numpy as np
from ode_FE import ode_FE
import matplotlib.pyplot as plt

# Considerando variações de Tensão Elétrica

for dt, T in zip((0.5, 20), (60, 100)):
    u, t = ode_FE(f=lambda u, t: 0.1*(1 - u/220.)*u, \
                               U_0=100, dt=dt, T=T)

    plt.figure()  # Modelo para Vários gráficos
    plt.plot(t, u, 'b-', label='Variação de Tensão Elétrica')
    plt.grid(True)
    plt.xlabel('Tempo de Análise (s)')
    plt.ylabel('Valores da Tensão Elétrica (Volt)')
    plt.legend()
    plt.savefig('tmp_%g.png' % dt); plt.savefig('tmp_%g.pdf' % dt)

    U = np.round(u,2)

print('Valores da Tensão Elétrica = ', U, '(em Volt)')
U_max = max(U)
U_min = min(U)
U_media = np.mean(U)
print('Tensão Elétrica Máxima =', U_max,'V')
print('Tensão Elétrica Mínima =', U_min,'V')
print('Tensão Elétrica Média =', U_media,'V')

