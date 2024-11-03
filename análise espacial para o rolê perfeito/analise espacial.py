#!/usr/bin/env python
# coding: utf-8

# # Análise Espacial para o Rolê Perfeito por Johann Kotaro

# ## Importar Bibliotecas

# In[1]:


import pandas as pd
from geopy.distance import great_circle
import matplotlib.pyplot as plt
import folium


# ## Carregar os Dados

# In[2]:


# Carregar a base de dados
file_path = "Base dados.xlsx"
dados = pd.read_excel(file_path)

# Corrigir os valores e formatação de latitude e longitude, caso seja necessário
dados['Latitude'] = dados['Latitude'].astype(str).str.replace(',', '.').astype(float)
dados['Longitude'] = dados['Longitude'].astype(str).str.replace(',', '.').astype(float)

# Verificar os dados
print(dados)


# ## Calcular o Centro Ideal

# In[3]:


# Função para calcular o Centro Ideal usando médias ponderadas
def calcular_centro_ponderado(dados):
    
    # Soma do Peso Total
    peso_total = dados['Peso'].sum()
    
    # Cálculo das coordenadas ponderadas
    latitude_ponderada = (dados['Latitude'] * dados['Peso']).sum() / peso_total
    longitude_ponderada = (dados['Longitude'] * dados['Peso']).sum() / peso_total
    
    return latitude_ponderada, longitude_ponderada

# Centro Ideal é calcular_centro_ponderado
centro_ideal = calcular_centro_ponderado(dados)

# Visualizar o valor do centro ideal para o rolê 
print(f"O centro ideal para o rolê é: {centro_ideal}")


# ## Calcular Distâncias ao Centro Ideal

# In[4]:


# Calculando as distâncias até o centro ideal
dados['Distancia do Centro'] = dados.apply(lambda row: great_circle((row['Latitude'], row['Longitude']), centro_ideal).kilometers, axis=1)

# Mostra as distâncias de cada amigo do centro ideal classificando a coluna "Distancia do Centro" do maior para o menor
print(dados.sort_values(by='Distancia do Centro', ascending=False)[['Nome', 'Bairro', 'Distancia do Centro']])


# ## Visualização em Gráfico de Linhas

# In[5]:


# Tamanho do Gráfico
plt.figure(figsize=(10, 6))

# Adicionando os amigos
for _, row in dados.iterrows():
    plt.scatter(row['Longitude'], row['Latitude'], label=row['Nome'], s=50)

# Adicionando o centro ideal
plt.scatter(centro_ideal[1], centro_ideal[0], color='red', label='Centro Ideal', s=100, marker='x')

plt.title("Amigos e Centro Ideal")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.grid()
plt.show()


# ## Visualização em Mapa

# In[6]:


# Centralizando o mapa no centro ideal
mapa = folium.Map(location=centro_ideal, zoom_start=12)

# Adicionando os amigos ao mapa
for _, row in dados.iterrows():
    folium.Marker(
        location=(row['Latitude'], row['Longitude']),
        popup=row['Nome'],
        icon=folium.Icon(color='blue')
    ).add_to(mapa)

# Adicionando o centro ideal ao mapa
folium.Marker(
    location=centro_ideal,
    popup='Centro Ideal',
    icon=folium.Icon(color='red')
).add_to(mapa)

# Mostrar o mapa
mapa

