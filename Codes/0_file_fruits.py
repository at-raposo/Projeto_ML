# %%
import pandas as pd

df = pd.read_excel("C:/Users/akura/OneDrive/Área de Trabalho/Projeto_ML/dados/dados_frutas.xlsx")
df.head()

# %%

from sklearn import tree #tree é o modelo de arvore

arvore = tree.DecisionTreeClassifier(random_state=42) #Algoritmo que vamos usar
#testes aleatorios

# %%
import pandas as pd

resposta_y = df["Fruta"] #target = variável resposta
display(resposta_y)


caracteristicas = ["Arredondada", "Suculenta", "Vermelha", "Doce"]
X = df[caracteristicas] #Nossas caracteristica
display(X)

# %%

#Ensinando a arvore
#ISSO AQUI É MACHINE ******LEARNING******** -> AJUSTE DO MODELO
teste = arvore.fit(X, resposta_y)  #ajustando o modelo, criação de arvore com base nos dados que estamos dando
#(co-variaveis, respostas)
display(teste)

# %%

#Predição

arvore.predict([[0,0,0,0]])

# %%

#desenhar essa arvore

import matplotlib.pyplot as plt

plt.figure(dpi=400)

#GARANTIR QUE SÓ ESTAMOS PEGANDO UMA CLASSE, CLASSES DISTINTAS
tree.plot_tree(arvore, feature_names= caracteristicas,
               class_names= arvore.classes_, 
               filled = True)

#Ele vai escolher a cereja, por ordem alfabetica

# %%

#Nos da a probabilidade de cada uma das nossas classes

proba = arvore.predict_proba([[1,1,1,1]])[0]
pd.Series(proba, index = arvore.classes_)
# %%
