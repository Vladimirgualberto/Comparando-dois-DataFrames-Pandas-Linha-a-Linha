# Comparando-dois-DataFrames-Pandas-Procv-Execel-
Como comparar dois arquivos Utilizando pandas e numpy?

De uma forma bem simples é possível comparar dois arquivos Usando Pandas e Numpy. A ideia aqui é comparar dois arquivos e verificar se os itens de uma coluna do primeiro arquivo(Arquivo A) é igual a uma coluna de outro arquivo(Arquivo B), o famoso procv do excel. =)

Primeiramente faz-se necessário importar as duas bibliotecas do Python(Pandas e Numpy):

import pandas as pd
import numpy as np

Em seguinda são carregados os dois arquivos copiando os seus respectivos caminhos e armazenando em uma variável, note que eles serão carregados como uma estrutura de dataframe do pandas:

dfA = pd.read_excel(r"<Local do Arquivo A>")
dfB = pd.read_excel(r"<Local do Arquivo B>")

Depois com uma linha simples de comandos conseguimos comparar os dois arquivos(Uma coluna em específico por exemplo):

dfA['Existe Na Central?']=np.where(dfA['Destino'] == dfB['Destino'], 'Existe', 'NãoExiste')

Aqui eu comparo os dois dataframes e defino uma nova coluna para armazena o resultado dessa comparação, no caso escrevo na coluna se existe ou não o número.

Por fim executo um print para verificar o dataframe alterado com a coluna de verificação:

print(dfA)
