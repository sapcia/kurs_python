import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
df['E']=df['A']+df['B']
a = df['E'].sum()
print(df.tail(10))
print(df['A'])
print(df[['A','B','E']])
print('suma to', a)

#df.to_csv('tablica.csv')
#drop first col
df1=pd.read_csv('tablica.csv', index_col=0)
print(df1)

plt.plot(df['A'], df['B'], c = 'b', label = 'Pierwszy wykres', marker = '^')
plt.ylim((0,100))
plt.xlim((0,100))
plt.xlabel('Kolumna A')
plt.ylabel('Kolumna B')
plt.legend()
plt.show()
