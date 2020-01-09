# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:07:32 2020

FEDERAL INSTITUTE OF EDUCATION, SCIENCE AND TECHNOLOGY OF PARÁ - IFPA ANANINDEUA

@authors: 
        Dr. Denis C. L. Costa, Professor
        
        Heictor Alves de Oliveira Costa, Undergraduate Student 
            
        
Search Group: 
                 Mathematical Modeling Gradient and Computer Simulation - GM²SC
                 
Subject Matter:  Cubic interpolation 
        
Script Name: interpolation_001

Available in:
    https://github.com/DenisCosta/PYTHON_MATHEMATICAL-MODELING/blob/master/
    INTERPOLATION%20METHODS/interpolation_001.py
    
"""
# Libraries used
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

print('')
print('=================================================================')
print('')
print('========================= Program Start =========================')
print('')
print('Involved Quantities: Temperature(T) and Density(D) >>> D = f(T)')
print('')

# Temperature Matrix
T = np.array([-10.0, 0.0, 10.0, 20.0, 30.0, 40]);
print('Temperature =', T,'°C')
print('')
D = np.array([0.99815, 0.99987, 0.99973, 0.99823, 0.99567, 0.99230]);
print('Density =', D, 'g/cm³')
print('')

# Cubic Spline Interpolation Function
f = interp1d(T, D)
D1 = interp1d(T, D, kind='cubic',fill_value="extrapolate")
T1 = np.arange(-10.0, 40.0, 1)

# New value for Temperature
print('Temperature Input Data >>>')
T_interpol=input('Enter the value of temperature_interpol (°C) --> ')
print('')
print('Density Output Data >>>')
print('')
D_INTERPOL=abs(D1(T_interpol))
print('INTERPOLATE Density value is (g/cm³) >>>', D_INTERPOL)
print('')
print('Graphic Representation of Cubic Spline')
print('')

# Break time: 10 seconds
sleep (10)
plt.figure(1)
plt.plot(T, D, 'or', T1, f(T1), '--k', T1, D1(T1), '*g')
plt.title(' Density as a function of Temperature ')
plt.xlabel(' Temperature Values (°C)');
plt.ylabel ( 'Density Values (g/cm³)');
plt.legend(["Real Data", "Data Projection", "Interpolated Data"],loc=3)
plt.grid(True)
plt.show()

# Break time: 3 seconds
sleep (3)
print('=======================+= End of Program ========================')
print('')
print('=================================================================')
