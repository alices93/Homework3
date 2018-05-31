# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast


energie = []
with open('energiaK.txt', 'U') as f: #apre file
	data=f.read() #copia in una stringa tutto il documento
	#data=data.split('\n') #divide per riga in una lista di stringhe
	#for numero in data[:-1]:
		#print numero
		#energie.append(float(numero))
	energie = ast.literal_eval(data)

# Create a dataset:
#df=pd.DataFrame({'k': range(1,101), 'sigma': np.random.randn(100)*15+range(1,101) })
df=pd.DataFrame({'iterazioni': range(0,500), 'energie': np.array(energie)})

# plot
plt.plot('iterazioni', 'energie', data=df, linestyle='-', linewidth=0.5, marker='', color ='black')
plt.xlabel('Numero iterazioni')
plt.ylabel('Energia per particella')
plt.show()
