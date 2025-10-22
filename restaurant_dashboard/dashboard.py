import pandas as pd
import streamlit as st
import plotly.express as px

#Cargar datos: pd.read_csv() lee un archivo CSV y lo guarda como un objeto DataFrame, que es una tabla en memoria (df es el nombre de esa tabla).
df = pd.read_csv("data/restaurants.csv")

#Título del dashboard: muestra un título grande en la parte superior.
st.title("Dashboard de Restaurantes en Madrid")

# --- FILTROS ---

# Lista de ciudades y cocinas con "Todas" al inicio
cities = ["Todas"] + list(df['City'].unique())
cuisines = ["Todas"] + list(df['Cuisine'].unique())

# Selección de ciudad y cocina
city_selected = st.selectbox("Ciudad", cities)
cuisine_selected = st.multiselect("Tipo de comida", cuisines, default=["Todas"])

# Aplicar filtros
if city_selected == "Todas" and "Todas" in cuisine_selected:
    filtered = df  # No filtramos nada, todo
elif city_selected == "Todas":
    filtered = df[df['Cuisine'].isin(cuisine_selected)]
elif "Todas" in cuisine_selected:
    filtered = df[df['City'] == city_selected]
else:
    filtered = df[(df['City'] == city_selected) & (df['Cuisine'].isin(cuisine_selected))]

#-df['City'] == city → devuelve solo las filas donde la ciudad coincide con la seleccionada.
#-df['Cuisine'].isin(cuisine) → devuelve las filas cuya cocina está en la lista elegida por el usuario.



#Estadísticas rápidas
st.write("Número de restaurantes:", len(filtered))
st.write("Rating promedio:", round(filtered['Rating'].mean(),2))

#Gráfico interactivo
fig = px.scatter(filtered, x='Reviews', y='Rating', size='PriceRange',
                 color='Cuisine', hover_data=['Name'])
st.plotly_chart(fig)


#px.scatter() crea un gráfico de dispersión (puntos).
#filtered los datos que se van a graficar.
#x='Reviews' eje horizontal = número de reseñas.
#y='Rating' eje vertical = puntuación.
#size='PriceRange' el tamaño de cada burbuja depende del rango de precios (1-3).
#color='Cuisine' el color representa el tipo de comida.
#hover_data=['Name'] al pasar el ratón, muestra el nombre del restaurante.
#st.plotly_chart(fig) muestra el gráfico dentro del dashboard.

#Top 10 restaurantes
top10 = filtered.sort_values(by='Rating', ascending=False).head(10)
st.write("Top 10 restaurantes:")
st.dataframe(top10[['Name', 'Cuisine', 'Rating', 'Reviews', 'PriceRange']])
