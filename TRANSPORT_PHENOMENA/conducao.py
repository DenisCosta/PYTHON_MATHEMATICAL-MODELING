# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:13:21 2019

@author: Prof. Dr. Denis C. L. Costa 
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Fenômenos de Transporte: Transmissão de Calor 
        
Nome do sript: conducao

Disponível em:  
    https://github.com/DenisCosta/PYTHON_MATHEMATICAL-MODELING/blob/master/
    TRANSPORT_PHENOMENA/conducao.py

"""

# Bibliotecas Utilizadas:
# Cálculo Diferencial e Integral: sympy
import sympy as sy
# Cálculo Algébrico: numpy
print('')
print('*****************************************')
print('Cálculo da Taxa de Tranferência de Calor')
print('')
# Coeficiente de Condutividade Térmica: k
k = 4*10**(-2) # w/m.ºC
print('Valor do k =',k,'W/m.ºC')
# Taxa de Tranferência de Calor: q
# Variáveis simbólicas
L = sy.symbols('L')
print('')
# Função de uma Variável: T = f(L)
def f(L):
    return k*(5.303*L**2-1.5*L+20.388)
# (f(L), L, 1) --> (Função, variável, ordem da derivada)
# Derivada 1ª da Função: df(L)
def df(L):
    return sy.diff(f(L), L,1)
print('')
print('=======================================')
print('Função Analisada: T = f(L) =', f(L))
print('Derivada 1ª da Função: q =', df(L))
print('=======================================')
print('')
# Valor Numérico da Taxa de Transmissão de calor: L = L1
L1= 0.5
print('Valor da espessura analisada =', L1,'m')
V_q = df(L).subs(L,L1)
print('Taxa de transferência no ponto L1')
print('V_q =', V_q, 'W/m')
print('')
print('---> Fim do Programa conducao <---')
print('*****************************************')




