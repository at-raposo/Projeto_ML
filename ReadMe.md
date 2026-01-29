# 📞 Previsão de Demanda - Call Center

Projeto de **previsão de volume de chamadas** utilizando modelos de regressão e conceitos de séries temporais, com foco em apoio à tomada de decisão operacional.

---

## 🎯 Objetivo

Prever a quantidade de chamadas recebidas por hora, permitindo:
- Melhor dimensionamento de equipes
- Redução de filas e tempo de espera
- Planejamento operacional

---

## 🧮 Modelo Matemático

Modelo base de regressão polinomial de grau 2:

$$
y_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \varepsilon_t
$$

Onde:
- $y_t$: número de chamadas no tempo $t$
- $t$: tempo (hora)
- $\varepsilon_t$: erro aleatório

---

## 🔧 Metodologia

1. Limpeza e tratamento dos dados  
2. Feature engineering  
3. Treinamento do modelo  
4. Avaliação com métricas:
   - RMSE
   - MAE

---

## 🛠 Tecnologias

- Python  
- Pandas  
- Numpy  
- Scikit-learn  

---

## 📊 Resultados

- **RMSE final:** `123.4`

*(valores ilustrativos)*

---

## 👨‍💻 Autor

**Adrian Raposo**  

