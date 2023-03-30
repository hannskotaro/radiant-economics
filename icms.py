# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

# Importando base e criando um dicionário
dados = pd.read_csv('impostos.csv') 
df = pd.DataFrame(dados)

# Definindo astype das colunas
df['imposto'] = df['imposto'].astype(float)
df['ano'] = df['ano'].astype(str)
df['inflacao'] = df['inflacao'].astype(float)

# Definindo variáveis independentes e dependente
X = dados[['ano', 'inflacao']]
y = dados['imposto']

# Treinar o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Previsão
X_novo = np.array([[2023, 5.79]])
y_novo = modelo.predict(X_novo)
print('Previsão de ICMS arrecadado em 2023:', y_novo[0])

# Métricas
y_pred = modelo.predict(X)
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
print('R2:', r2)
print('MSE:', mse)

# Coeficientes angular e linear para a reta
coef_angular = modelo.coef_[0]
coef_linear = modelo.intercept_
print('coef_angular', coef_angular)
print('coef_angular', coef_linear)

# Gráfico de dispersão com reta de tendência
plt.figure(figsize = (16,8))
plt.scatter(X['ano'], y)
plt.plot(X['ano'], coef_angular*X['ano'].astype(int) + coef_linear, color='red')
plt.scatter('2023', y_novo[0], color='green')
plt.annotate('Previsão 2023', ('2023', y_novo[0]), xytext=('2024', y_novo[0] + 1000000000), fontsize=12, arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlabel('Ano')
plt.ylabel('Imposto')
plt.show()
