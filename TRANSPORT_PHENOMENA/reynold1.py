# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:26:39 2019

@author: 
        Prof. Dr. Denis C. L. Costa
                
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
           
Assunto: 
        Análise dos escoamentos

Nome do sript: reynold1.py

Disponível em:
    
    
"""
# Assunto: Comportamento de um Fluido
# Importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt
# Grandezas envolvidas:
d = 0.5 # Diâmetro do duto (m)
v = 0.8 # Velocidade do fluido (m/s)
rho = 0.04 # Peso específico
# Vetor Viscosidade
mi = np.linspace(40*10**-6,2*10**-6,10)
# Número de Reynold
Re = (v*rho*d)/mi
plt.plot(mi,Re,'ob')
plt.xlabel('Viscosidade')
plt.ylabel('Coeficiente de Reynold')
plt.title('Análise do Escoamento')
plt.grid(True)
plt.show()
print('')
print('Fim do Programa')










