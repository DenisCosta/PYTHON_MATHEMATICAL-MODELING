# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:27:04 2019

@author: 
        Prof. Dr. Denis C. L. Costa

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
       Análise Numérica de Escoamentos
       
Disponível em:
    
"""

# Variáveis de Controle

# Peso específico do fluido (kg/m³): rho
ρ = 0.4 
print('ρ =',ρ,'kg/m³')

# Velocidade do fluido (m/s): V
V = 200 
print('V =',V,'m/s')

# Viscosidade do fluido (Pa.s ou 1cP = 10**−3Pa.s): μ
μ = 0.7
print('μ =',μ,'Pa.s')

# Diâmetro da tubulação (m): d 
d = 10
print('d =',d,'m')

# Cálculo do número de Reynolds: Re
Re = V*ρ*d/μ 
 
print('Re =',Re)
