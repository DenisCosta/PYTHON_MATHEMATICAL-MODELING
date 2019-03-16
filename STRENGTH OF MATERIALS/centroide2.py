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
        em função da Densidade Volumétrica



       
"""

# Bibliotecas
# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
x,y,z=sy.symbols('x,y,z')
# Função de Densidade Volumétrica: rho(x,y,z)
def ρ(x,y,z):
    return x**2+3*y+z**0.5
print('ρ(x,y,z) = ',ρ(x,y,z), 'kg/m³')

# Integral dupla de rho(x,y):M(x,y) ---> Massa Total
def M(x,y,z):
    return sy.integrate(ρ(x,y,z), (x, 0, 4),(y, 0, 2),(z, 0, 3))
print('Mt =',round(M(x,y,z),2), 'kg')

# Momentos: Mxy, Mxz e Myz
def Mxy(x,y,z):
    return sy.integrate(z*ρ(x,y,z), (x, 0, 4),(y, 0, 2),(z, 0, 3))
print('Mxy =', round(Mxy(x,y,z),2), 'kg.m²')

def Mxz(x,y,z):
    return sy.integrate(y*ρ(x,y,z), (x, 0, 4),(y, 0, 2),(z, 0, 3))
print('Mxz =', round(Mxz(x,y,z),2), 'kg.m²')

def Myz(x,y,z):
    return sy.integrate(x*ρ(x,y,z), (x, 0, 4),(y, 0, 2),(z, 0, 3))
print('Myz =', round(Myz(x,y,z),2), 'kg.m²')

# Coordenadas do Centro de Massa: Cx e Cy
def Cxy(x,y,z):
    return Mxy(x,y,z)/M(x,y,z)
print('Cxy =', round(Cxy(x,y,z),2), 'm')

def Cxz(x,y,z):
    return Mxz(x,y,z)/M(x,y,z)
print('Cxz =', round(Cxz(x,y,z),2), 'm')

def Cyz(x,y,z):
    return Myz(x,y,z)/M(x,y,z)
print('Cyz =', round(Cyz(x,y,z),2), 'm')

print(' ')
print(' ===== Fim do Programa centroide2 ====')