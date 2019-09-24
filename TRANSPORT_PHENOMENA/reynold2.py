# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:25:32 2019

@author: 
        Prof. Dr. Denis C. L. Costa
                
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Classidica dos escoamentos

Nome do sript: reynold2.py

Disponível em:
    https://github.com/DenisCosta/PYTHON_MATHEMATICAL-MODELING/blob/master/
    TRANSPORT_PHENOMENA/reynold2.py

"""
# Análise do Escoamento
# Variáveis envolvidas

# Grandezas envolvidas:
d = 0.04 # Diâmetro do duto (m)
v = 0.1 # Velocidade do fluido (m/s)
rho = 1000 # Peso específico do fluido (kg/m³)
# Viscosidade do Fluido
mi = 1.0030*10**(-3)
# Número de Reynold
Re = (v*rho*d)/mi
print('==========================')
print('Re = ',round(Re,3))
print('==========================')
print('Classificação:')
# Loop condicional
if (Re < 2000):
    print('Escoamento Laminar')
elif (2000 <= Re < 2400): 
    print('Escoamento em Transição')
elif (Re >= 2400): 
    print('Escoamento Turbulento')
print('==========================')  
print('')
print('Fim do Programa')




