# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:08:22 2019

@author: 
        Prof. Dr. Denis C. L. Costa

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
       Análise em 2D das Coordenadas do Centro de Massa de um corpo Não-Homogêneo
       
Disponível em:
    
          
"""
# Bibliotecas

# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
x,y=sy.symbols('x,y')

# Função de Densidade Superficial: rho(x,y)
def rho(x,y):
    return 3*x**2*y

# Integral dupla de rho(x,y): M(x,y) --> Massa Total
def M(x,y):
    return sy.integrate(rho(x,y), (x, 0, 2),(y, 0, 1))
print('Mt =',M(x,y))

# Momentos: Mx e My
def Mx(x,y):
    return sy.integrate(y*rho(x,y), (x, 0, 2),(y, 0, 1))
print('Mx =',Mx(x,y))
#####

def My(x,y):
    return sy.integrate(x*rho(x,y), (x, 0, 2),(y, 0, 1))
print('My =',My(x,y))

# Coordenadas do Centro de Massa: Cx e Cy
def Cx(x,y):
    return My(x,y)/M(x,y)
print('Cx =',Cx(x,y))
####

def Cy(x,y):
    return Mx(x,y)/M(x,y)
print('Cy =',Cy(x,y))

##########################################################
print(' ')
print(' ===== Fim do Programa fenomeno_001 ====')