# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast


temperature = []
with open('MDloop\\Run_0.001.txt', 'U') as f:
	data = f.read() 
	righe = data.split('\n') #divide per riga in una lista di stringhe
	for riga in righe:
		#print riga
		valori = riga.split('\t')
		temperatura = float(valori[1])
		#print energia
		temperature.append(temperatura)


ascissa = [0]*len(temperature)
for indice in range(len(ascissa)):
	ascissa[indice] = 0.001 * indice


# Create a dataset:
df=pd.DataFrame({'iterazioni': np.array(ascissa), 'energie': np.array(temperature)})

# plot
plt.plot('iterazioni', 'energie', data=df, linestyle='-', linewidth=0.5, marker='', color ='black')
plt.xlabel('tempo')
plt.ylabel('energia per particella')
plt.show()