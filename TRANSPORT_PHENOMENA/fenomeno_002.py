# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:03:17 2019

@author: 
        Prof. Dr. Denis C. L. Costa

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
       Cálculo da Tensão de Cisalhamento 
       
Disponível em:
    
    
"""

# Bibliotecas

# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
x,y=sy.symbols('x,y')

# Viscosidade Absoluta: Mi

Mi = 0.5

# Perfil de Velocidade: V(x,y)
def V(x,y):
    return 3*x**3*y

###
# Derivadas parcias de V(x,y)  
    
def Vx(x,y):
    return sy.diff(V(x,y), x,1) 
print('Vx(x,y) =',Vx(x,y))


def Vy(x,y):
    return sy.diff(V(x,y), y,1) 
print('Vy(x,y) =',Vy(x,y))

# Valor Numérico das Derivadas Parciais
Vx1 = Vx(x,y).subs(x,1).subs(y,1)
print('Vx1 =',Vx1 )

Vy1 = Vy(x,y).subs(x,1).subs(y,1)
print('Vy1 =',Vy1)

################ 
# Tensão de Cisalhamento: thal(x,y)
def thal(x,y):
    return Mi*(Vx1+Vy1)
print('thal(x,y) =',thal(x,y))



