# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:02:01 2019

@author:  
        Prof. Dr. Denis C. L. Costa

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
        Técnica de Convolução Aplicada à Análise de Sistemas Lineares 
    
    
    O script a seguir executa a CONVOLUÇÃO utilizando a linguagem PYTHON. 
A função DELTA representa o IMPULSO unitário, e as funções x e h as 
respectivas sequências. A aplicação é vetorizada, ou seja, pode ser aplicada 
a sequências de números, ao invés de uma variável apenas. Dessa forma, é 
possível definir o domínio, e suas correspondentes sequências, de forma 
independente, semelhante ao equacionamento matemático. 
    
"""

# Importando Biblioteca
# Biblioteca numpy: Matemática de alto Nível

import numpy as np
import matplotlib.pyplot as pyplt

# Vetor e suas sequências:

a = np.convolve([1, 2, 3], [0, 1, 0.5])

print('Vetor a =',a)

# Representação Gráfica da Convolução
pyplt.plot([1, 2, 3], [0, 1, 0.5],'g')
pyplt.grid(True)
pyplt.show()

pyplt.plot([0, 0.5, 1, 2, 3], a,'r')
pyplt.grid(True)
pyplt.show()

##########################################################
print(' ')
print(' ===== Fim do Programa convolucao ====')