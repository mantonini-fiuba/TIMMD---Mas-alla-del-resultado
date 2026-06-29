# TIMMD---Mas-alla-del-resultado
🎯 Análisis de partidos de fútbol con datos StatsBomb — mapas emocionales, estilos de juego, modelos xG y simulaciones contrafácticas. FIUBA · TIMMD · 2026.


## Descripción

Este proyecto explora el fútbol desde una perspectiva de Ciencia de Datos, utilizando eventos registrados por StatsBomb para reconstruir partidos, analizar estilos de juego y modelizar situaciones de gol.

La idea principal es estudiar **qué ocurrió, por qué ocurrió y qué podría haber ocurrido**, utilizando información de distintos torneos internacionales y modelos de aprendizaje automático.

El repositorio incluye notebooks desarrollados en Google Colab que permiten:

- Explorar la estructura de los datos de un partido.
- Visualizar mapas de pases, tiros y acciones.
- Construir modelos de **Expected Goals (xG)**.
- Analizar escenarios contrafácticos (*¿Qué hubiera pasado si...?*).
- Comparar estilos de juego y patrones tácticos entre equipos y competiciones.

---

# Estructura del proyecto

```text
TIMMD/
│
├── data/                     # Partidos descargados automáticamente
├── versiones viejas/         # Versiones anteriores de notebooks
├── __pycache__/              # Archivos temporales
│
├── 00 -- CARGA DE DATOS.ipynb
├── 01 -- MAPA EMOCIONAL.ipynb
├── 02 -- ESTILO DE JUEGO.ipynb
├── 03 -- MODELO DE PROB.ipynb
├── 04 -- Y QUE SI.ipynb
│
└── colores_equipos.py        # Paleta de colores utilizada en las visualizaciones
```

Los notebooks están diseñados para ser independientes, compartiendo la misma estructura de datos.

---

# Configuración inicial

## 1. Acceso a Google Drive

Los notebooks están pensados para ejecutarse en **Google Colab**.

Antes de comenzar:

1. Abrir el enlace compartido de la carpeta **TIMMD**.
2. Crear un **Acceso directo** dentro de **Mi unidad** de Google Drive.
3. **No modificar el nombre de la carpeta.**

Una vez realizado este paso, todos los notebooks podrán encontrar automáticamente los archivos necesarios.

---

## 2. Descarga automática de partidos

La primera vez que se ejecuta un notebook, los archivos correspondientes al partido seleccionado se descargarán automáticamente dentro de:

```text
TIMMD/data/
```

---

# Orden recomendado

## Paso obligatorio

Ejecutar primero:

```text
00 -- CARGA DE DATOS.ipynb
```

Este notebook configura el entorno de trabajo y descarga los datos necesarios.

---

## Análisis posteriores

Una vez ejecutado el notebook de carga, cualquiera de los siguientes puede utilizarse de forma independiente:

- **01** — Mapa Emocional del partido
- **02** — Estilo de Juego de cada equipo
- **03** — Modelos de Probabilidad (xG)
- **04** — ¿Y qué si...? (escenarios contrafácticos)

> **Importante:** No modificar `MATCH_ID` dentro del notebook **04**.

Para analizar un partido diferente únicamente es necesario modificar el valor de `MATCH_ID` definido al comienzo de los notebooks **01**, **02** y **03**.

---

# Objetivos del proyecto

El proyecto busca responder preguntas como:

- ¿Qué características distinguen a distintos estilos de juego?
- ¿Qué variables explican la probabilidad de gol de una acción?
- ¿Cómo cambian las probabilidades de victoria ante un evento específico?
- ¿Qué similitudes y diferencias existen entre torneos, selecciones y equipos?

Más que predecir un resultado, el objetivo es **comprender la historia de un partido a partir de los datos**.

---

# Tecnologías utilizadas

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- StatsBomb Open Data

---

# Futuras mejoras

- Incorporación de nuevos torneos y competiciones.
- Modelos de xG más complejos.
- Clustering de estilos de juego.
- Simulaciones Monte Carlo de partidos completos.
- Dashboard interactivo para explorar partidos y jugadores.

---

# Autores

Proyecto desarrollado para explorar aplicaciones de Ciencia de Datos y Aprendizaje Automático sobre datos abiertos de fútbol, con foco en la interpretación y el análisis cuantitativo del juego.

Proyecto realizado para la materia **TIMMD** de la Facultad de Ingeniería de la Universidad de Buenos Aires.

**Julio 2026**

**Joaquín Azpiazu** (110578)  
**Máximo Antonini** (110516)

---

# MÁS ALLÁ DEL RESULTADO

### *La historia de un partido en datos*
