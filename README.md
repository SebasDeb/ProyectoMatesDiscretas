# Mapa Interactivo UDLAP

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/downloads/)
![GitHub repo size](https://img.shields.io/github/repo-size/tu_usuario/udlap-navegacion)

Sistema de navegación inteligente para el campus de la UDLAP que calcula las rutas óptimas entre cualquier ubicación.


## Características principales ✨

- 🗺️ **Mapa interactivo** con ubicaciones reales del campus
- 📐 **Algoritmo de Dijkstra** para cálculo de rutas óptimas
- 🖥️ Interfaz gráfica moderna con **Tkinter**
- 📊 Visualización con **Matplotlib**
- 📱 **Responsive design** adaptable a diferentes pantallas

## Instalación ⚡

1. Clona el repositorio.
```bash
git clone https://github.com/SebasDeb/ProyectoMatesDiscretas.git
cd udlap-navegacion
```

2. Instala dependencias.
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación.
```bash
python grafos_udlap.py
```

🖥️ Uso del Sistema
Seleccionar ubicaciones:

Usa los menús desplegables para elegir punto de inicio y destino

Calcular ruta:

```python
# Ejemplo de cálculo de ruta
ruta, distancia = calcular_ruta("GC", "BI")  # Gimnasio -> Biblioteca
```
Visualizar resultados:

Ruta resaltada en rojo en el mapa

Distancia total mostrada en metros

Secuencia detallada de nodos
