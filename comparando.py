import pandas as pd
import numpy as np

##Local lib


df = pd.read_excel(r"C:\Users\Vladimir\PycharmProjects\comparandoarquivos\comp1central.xlsx")
df1 = pd.read_excel(r"C:\Users\Vladimir\PycharmProjects\comparandoarquivos\comp2syonet.xlsx")


df['Existe Na Central?']=np.where(df['Destino'] == df1['Destino'], 'Existe', 'NãoExiste')

print(df)