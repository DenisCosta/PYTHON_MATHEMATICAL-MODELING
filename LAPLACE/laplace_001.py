# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:18:17 2019

@author: 
        Prof. Dr. Denis C. L. Costa
        
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Transformada de Laplace
        
Nome do sript: laplace_001

Disponível em:
    https://github.com/DenisCosta/PYTHON_MATHEMATICAL-MODELING/blob/master/
    LAPLACE/laplace_001.py
    
"""
# Biblioteca sympy
# Variáveis envolvidas: t e s
import sympy as sy
t = sy.Symbol('t')
s = sy.Symbol('s')

# Função Definida no Domínio do Tempo
f1 = sy.exp(2*t)

# Aplicando a Transformando a Laplace
T_L = sy.laplace_transform(f1,t,s)

# Dados de Saída
print('===========================')
print('Função Primitiva -->',f1)
print('')
sy.pprint('Função Primitiva: ',f1)
print('\n f(t) = e**(2t) \n')
print('')
print('Tranformada de Laplace -->',T_L)
print('Tranformada de Laplace:')
sy.pprint(T_L)

