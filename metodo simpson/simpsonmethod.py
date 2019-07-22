import numpy as np 
from scipy import integrate 
import pandas as pd

#Integración por método númericos.
archivo=pd.read_excel("Masas-I-lab-II_onedrive.xlsx",'Coef. mass transfer liq',index_col=None)
y=archivo['N_oG'].to_numpy()
x=archivo['y_a'].to_numpy()
result=integrate.simps(y,x,even='avg')
print('*************************')
print(archivo)
print('*************************')
print(y)
print('*************************')
print(x)
print('*************************')
print('el resultado de la integracion por metodo simpson es: ',result)