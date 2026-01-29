# %%

import pandas as pd

df = pd.read_excel("C:\\Users\\akura\\OneDrive\\Área de Trabalho\\Projeto_ML\\data\\dados\\dados_cerveja.xlsx")
df.head()
# %%

features = ['temperatura', 'copo', 'espuma', 'cor'] #feature é as caracteristicas
target = 'classe' # queremos aprender isso aqui com as features

X = df[features]
y = df[target]


# %%
#from sklearn import tree

#uma forma de a gente conseguir ajustar essa função para a gente ajustar em um outro conjunto de dados
#model = tree.DecisionTreeClassifier() 

#TEM QUE SER TUDO NUMERO
#model.fit(X=X, y=y)
# %%

#nos vamos mudar oq cada coisa categorica significa
X = X.replace({
    "mud": 1, "pint": 2,
    "sim": 1, "não": 0,
    "escura": 1, "clara": 0
})
# %%
from sklearn import tree

#uma forma de a gente conseguir ajustar essa função para a gente ajustar em um outro conjunto de dados
model = tree.DecisionTreeClassifier() 

#TEM QUE SER TUDO NUMERO
model.fit(X=X, y=y)

# %%
import matplotlib.pyplot as plt
from sklearn import tree

plt.figure(dpi=400)

tree.plot_tree(
    model,
    feature_names=features,
    class_names=model.classes_,
    filled=True
)
# %%
