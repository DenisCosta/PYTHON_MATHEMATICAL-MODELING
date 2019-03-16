# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:08:22 2019

@author: 
        Prof. Dr. Denis C. L. Costa

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto:
        Cálculo das Coordenadas do Centro de Massa de um corpo Não-Homogêneo
        em função da Densidade Superficial
       
"""

# Bibliotecas
# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
x,y=sy.symbols('x,y')

# Função de Densidade Superficial: rho(x,y)
def ρ(x,y):
#    return x+y
    return x**2+3*y
print('ρ(x,y) = ',ρ(x,y), 'kg/m²')

# Integral dupla de rho(x,y):M(x,y) ---> Massa Total
def M(x,y):
    return sy.integrate(ρ(x,y), (x, 0, 4),(y, 0, 2))
print('Mt =', round(M(x,y),2), 'kg')

# Momentos: Mx e My
def Mx(x,y):
    return sy.integrate(y*ρ(x,y), (x, 0, 4),(y, 0, 2))
print('Mx =', round(Mx(x,y),2), 'kg.m')

def My(x,y):
    return sy.integrate(x*ρ(x,y), (x, 0, 4),(y, 0, 2))
print('My =', round(My(x,y),2), 'kg.m')

# Coordenadas do Centro de Massa: Cx e Cy
def Cx(x,y):
    return My(x,y)/M(x,y)
print('Cx =', round(Cx(x,y),2), 'm')

def Cy(x,y):
    return Mx(x,y)/M(x,y)
print('Cy =', round(Cy(x,y),2), 'm')

print(' ')
print(' ===== Fim do Programa centroide ====')