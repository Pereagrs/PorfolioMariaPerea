# **Dashboard de Restaurantes**

Este proyecto es un dashboard interactivo de restaurantes hecho en Python, utilizando Streamlit, pandas y Plotly.  
Permite explorar restaurantes por ciudad, tipo de comida, ver estadísticas, gráficos y un top 10 de los mejores restaurantes.

----------

## **Características**

-   Filtrado interactivo por:
    
    -   Ciudad (con opción “Todas”)
        
    -   Tipo de comida (con opción “Todas”)
        
-   Estadísticas rápidas:
    
    -   Número de restaurantes mostrados
        
    -   Rating promedio
        
-   Gráfico interactivo:
    
    -   Dispersión de Rating vs Número de Reseñas
        
    -   Tamaño de burbujas según rango de precio
        
    -   Color según tipo de comida
        
-   Top 10 restaurantes según rating
    
-   Todo listo para ejecutar en tu navegador con Streamlit
    

----------

## **Estructura del proyecto**

restaurant_dashboard/  
│  
├─ data/  
│ └─ restaurants.csv # Dataset  
├─ dashboard.py # Código principal del dashboard  
├─ requirements.txt # Librerías necesarias  
└─ README.md 

----------

## **Dataset**

El dataset restaurants.csv contiene estas columnas:

Name → Nombre del restaurante  
City → Ciudad  
Cuisine → Tipo de comida  
Rating → Valoración (1 a 5)  
PriceRange → Rango de precio (1-3)  
Reviews → Número de reseñas

Se incluye un dataset de ejemplo con 50 restaurantes de distintas ciudades y tipos de comida.

----------

## **Instalación**

1.  Clonar el repositorio:
    

		git clone https://github.com/Pereagrs/PorfolioMariaPerea/tree/main/restaurant_dashboard  
		cd restaurant_dashboard

2.  Instalar librerías necesarias:
  
		pip install -r requirements.txt

----------

## **Uso**

Ejecutar el dashboard:

		streamlit run dashboard.py

-   Se abrirá automáticamente en tu navegador.
    
-   Usa los filtros para explorar los restaurantes por ciudad y tipo de comida.
    
-   Explora los gráficos interactivos y consulta el top 10.
    

----------

## **Tecnologías usadas**

-   Python 3.13
    
-   pandas → Manejo y filtrado de datos
    
-   Streamlit → Dashboard web interactivo
    
-   Plotly → Gráficos interactivos