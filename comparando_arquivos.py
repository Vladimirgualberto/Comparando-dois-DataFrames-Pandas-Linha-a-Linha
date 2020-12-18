import pandas as pd
import numpy as np

##Local lib


dfA = pd.read_excel(r"<Local do Arquivo A>")
dfB = pd.read_excel(r"<Local do Arquivo B>")


dfA['Existe Na Central?']=np.where(dfA['Destino'] == dfB['Destino'], 'Existe', 'NãoExiste')

print(dfA)
