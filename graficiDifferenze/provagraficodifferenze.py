# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast

energietemp1 = []
with open('MDloop\\Run_0.001.txt', 'U') as f:
	data = f.read()
	righe = data.split('\n') #divide per riga in una lista di stringhe
	for riga in righe[1:]:
		#print riga
		valori = riga.split('\t')
		energia = float(valori[1])
		#print energia
		energietemp1.append(energia)

energie3 = []
with open('MDloop\\Run_0.009.txt', 'U') as f:
	data = f.read()
	righe = data.split('\n') #divide per riga in una lista di stringhe
	for riga in righe[1:]:
		#print riga
		valori = riga.split('\t')
		energia = float(valori[1])
		#print energia
		energie3.append(energia)
#print energie2



energie1 = []
for indice, energia in enumerate(energietemp1):
    indice *= 9
    energie1.append(energia)

differenzaE31 = []
for energia in energie:
    differenzaE21[energia] = energie3[energia] - energie1[energia]

print differenzaE31
