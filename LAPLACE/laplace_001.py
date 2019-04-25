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
    
"""
import sympy as sy
t = sy.Symbol('t')
s = sy.Symbol('s')

# Domínio do Tempo
f1 = sy.exp(2*t)



# Transformando a Laplace
T_L = sy.laplace_transform(f1,t,s)


# Output
print('===========================')
print('Função Primitiva -->',f1)
print('')
sy.pprint('Função Primitiva: ',f1)
print('\n f(t) = e**(2t) \n')
print('')
print('Tranformada de Laplace -->',T_L)
print('Tranformada de Laplace:')
sy.pprint(T_L)

