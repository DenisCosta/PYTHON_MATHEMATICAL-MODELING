# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:40:52 2019

@author: Prof. Dr. Denis C. L. Costa
    
    Instalações Elétricas
        Simulação computacional

Script 01: ode_FE

Disponível em:
    
https://github.com/DenisCosta/PYTHON_MATHEMATICAL-MODELING/blob/master/ELECTRICAL%20INSTALLATIONS/ode_FE.py

"""
# Análise  Temporal das Tensões Elétricas
# Bibliotecas Utilizadas

from numpy import linspace, zeros, exp
import numpy as np
import matplotlib.pyplot as plt
# Tensão Elétrica Real
def ode_FE(f, U_0, dt, T):
    N_t = int(round(float(T)/dt))
    u = zeros(N_t+1)
    t = linspace(0, N_t*dt, len(u))
    u[0] = U_0
    for n in range(N_t):
        u[n+1] = u[n] + dt*f(u[n], t[n])
    return u, t
# Tensão Elétrica Aparente
def Instalacoes_Eletricas():
    """Estudo de Caso: u'=r*u, u(0)=100."""
    def f(u, t):
        return 0.1*u
# Comportamento Gráfico
    u, t = ode_FE(f=f, U_0=18, dt=0.5, T=20)
    plt.plot(t, u, label='Tensão Real')
    plt.plot(t, 10*exp(0.1*t), label='Tensão aparente')
    plt.xlabel('Tempo de Análise (s)')
    plt.ylabel('Valores da Tensão Elétrica (Volt)')
    plt.legend()
    plt.grid(True)
    plt.show()

    U = np.round(u,2)

    print('Valores da Tensão Elétrica = ', U, '(em Volt)')
    U_max = max(U)
    U_min = min(U)
    U_media = np.mean(U)
    print('Tensão Elétrica Máxima =', U_max,'V')
    print('Tensão Elétrica Mínima =', U_min,'V')
    print('Tensão Elétrica Média =', U_media,'V')

if __name__ == '__main__':
    Instalacoes_Eletricas()




