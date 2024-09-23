
import os
os.system('pip install pandas seaborn matplotlib')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')

plt.title('Preço da Gasolina em São Paulo (1 a 10 de Julho de 2021)')
plt.xlabel('Dia')
plt.ylabel('Preço de Venda (R$)')
plt.grid()

plt.savefig('gasolina.png')

plt.show()
