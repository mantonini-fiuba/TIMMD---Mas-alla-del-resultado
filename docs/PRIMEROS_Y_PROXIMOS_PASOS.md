# Primeros y Próximos Pasos

Este documento complementa al README del proyecto **TIMMD 9216 — Más allá del resultado: la historia de un partido en datos**. Cubre dos cosas: (1) el criterio usado para calibrar el modelo de intensidad del partido (Notebook 1) y (2) los próximos pasos y mejoras potenciales del proyecto.

\---

## 1\. Criterio de calibración de la intensidad del partido

### Objetivo

El modelo de intensidad narrativa (mapa emocional) asigna pesos a cada tipo de evento (tiros, faltas, duelos, etc.) y los multiplica por factores contextuales (diferencia de gol, tiempo restante). Esos pesos y multiplicadores no salen de una tabla arbitraria: se calibran contra partidos reales antes de aplicarse a partidos desconocidos.

### Criterio rector

> \*\*El modelo se calibra con partidos que el equipo ya conoce, para poder aplicarse después con confianza a partidos que no conoce.\*\*

La razón de fondo es reducir la subjetividad del análisis:

* Definir los pesos "a ojo" (cuánto vale un tiro vs. una falta, cuánto pesa el minuto 88 vs. el minuto 10) es, en sí mismo, un juicio subjetivo.
* Para evitar que esa subjetividad quede escondida dentro del modelo, se la expone y se la contrasta: se eligen partidos cuya intensidad y momentos clave son de público conocimiento (remontadas, finales recordadas, partidos sin historia), se corre el modelo sobre ellos, y se verifica que la curva de intensidad generada coincida con lo que cualquiera que haya visto ese partido diría.
* Recién cuando el modelo reproduce de forma consistente la intensidad percibida en partidos conocidos, se lo considera válido para analizar partidos donde el equipo **no** tiene una opinión previa formada — que es, en definitiva, el caso de uso real del proyecto.

### Proceso de calibración

1. **Selección de partidos de referencia**: partidos con consenso claro sobre su nivel de intensidad y sus momentos clave (remontadas evidentes, finales ajustadas, partidos "trámite").
2. **Corrida del modelo**: se generan las curvas de intensidad minuto a minuto para esos partidos.
3. **Contraste**: se compara la curva contra la lectura conocida del partido (¿el pico coincide con el momento que todos recuerdan como el más intenso? ¿un partido "aburrido" da una curva plana?).
4. **Ajuste**: se corrigen pesos de eventos y multiplicadores contextuales hasta que el modelo reproduce esa lectura de forma consistente entre partidos distintos.
5. **Congelamiento de parámetros**: una vez calibrado, el modelo se aplica sin ajustes manuales adicionales a partidos nuevos.

### Partidos utilizados como referencia

*(completar con el detalle final del equipo)*

|Partido|Motivo de elección|Momento clave esperado|
|-|-|-|
|Argentina - Francia 2022|Conocimiento de los eventos|Goles e intensidad hacia el final|
|Argentina - Paises Bajos 2022|Conocimiento de los eventos|Enojo e ingreso a la cancha de suplentes|

\---

## 2\. Próximos pasos / mejoras potenciales

Estas son las líneas de trabajo identificadas para llevar el proyecto de notebook académico a herramienta de uso real:

### Ampliación

Escalar el pipeline más allá de un partido o competición puntual: aplicar el mismo criterio y los mismos modelos a múltiples ligas y torneos, sin tener que rehacer el análisis desde cero para cada uno.

### Integración con tiempo real

Pasar de un análisis post-partido a un análisis en vivo: que la intensidad, el estilo de juego y el xG se actualicen minuto a minuto mientras el partido se está jugando, en lugar de calcularse sobre el evento ya cerrado.

### Mejorar la exactitud del modelo de predicción

Seguir afinando el modelo de xG (y, en el futuro, el de intensidad) sumando variables, más partidos de entrenamiento y validación cruzada, para acercar más las probabilidades estimadas al comportamiento real del juego.

\---

*Documento vivo: se actualiza a medida que el proyecto avanza.*

