# Anteproyecto Final - IA 1 2023

## Resolviendo el Ajedrez

## Código: Ajedrez

### Alumnos:
- Yeumen Silva
- Andrés Maglione

## Introducción
El ajedrez es un juego de estrategia milenario que ha enamorado a millones de jugadores de todo el mundo a lo largo de la historia. Es un juego de mesa para dos jugadores, cada uno de los cuales controla dieciséis piezas con diferentes capacidades y movimientos. El objetivo del juego es capturar al rey del oponente, manteniendo el propio a salvo.

El tablero de ajedrez se compone de 64 casillas, alternando colores, y las piezas se distribuyen en filas y columnas al comienzo de la partida. Entre su conjunto de piezas, cada jugador posee peones, torres, caballos, alfiles, una reina y un rey. Cada tipo de pieza tiene movimientos específicos, lo que añade complejidad al juego. Los peones avanzan una casilla hacia adelante, pero capturan en diagonal, mientras que las torres se mueven en líneas rectas, los caballos tienen un movimiento en forma de "L", los alfiles se desplazan en diagonal, la reina combina movimientos de torre y alfil, y el rey se mueve una casilla en cualquier dirección.

![movimientos](https://recursos.edu.xunta.gal/sites/default/files/recurso/1615988067/Smart-P-E/chess-4264325_1280.png)
La belleza del ajedrez radica en la cantidad de posibles estados del tablero: según una de las estimaciones más recientes, el número de estados legales para un tablero es de $4.4 \cdot 10^{44}$. Esto significa que los jugadores pueden emplear todo tipo de tácticas y estrategias para conseguir vencer a su rival.

El juego del ajedrez ha sido un campo de estudio y competición durante años, y existen reglas y sistemas de notación construidas con el objetivo de estandarizar el juego en todo el mundo. Como consecuencia de esto, el ajedrez se ha convertido en un verdadero deporte con una escena competitiva extramadamente amplia y popular, que ha contado con jugadores célebres a lo largo de la historia.

Para medir la habilidad de los jugadores de forma objetiva, se utiliza un sistema de puntuación basado en métodos estadísticos llamado **Elo**, que determina la calificación de un jugador en función de sus resultados frente a otros jugadores, a partir de la probabilidad esperada que que dicho jugador gane. Este método es muy popular y actualmente se utiliza como una métrica de la habilidad de jugadores en todo tipo de juegos

La enorme dificultad que trae consigo el ajedrez, junto con la importancia cultural del mismo y el ojo del público sobre los mejores jugadores del mundo, han convertido al ajedrez en uno de los juegos que más desarrollo han impulsado en el campo de la inteligencia artificial. La historia comienza en los años 60, cuando se desarrollaron los primeros programas para poder jugar al ajedrez. El enorme progreso en la computación y en la algoritmia en las décadas siguientes, llevó a que en el año 1997 la supercomputadora Deep Blue venciera al vigente campeón mundial de ajedrez Bobby Fisher, marcando el comienzo de una nueva era no solo para el ajedrez, sino para toda disciplina en la que se creía que la inteligencia humana no sería superada. 

## Nuestro proyecto
Para nuestro proyecto final, elegimos llevar a cabo una inteligencia artificial que sea capaz de jugar al ajedrez. 

### Cómo medirlo

Para comenzar, debemos hallar una métrica que nos permita medir la habilidad de un jugador de ajedrez. Como mencionamos anteriormente, el sistema de puntuación Elo es el más utilizado en el mundo del ajedrez, por lo que decidimos utilizarlo como métrica para nuestro proyecto. 

Existen diversos frameworks que permiten medir el Elo de un motor de ajedrez propio para poder compararlo con otros motores existentes. Las herramientas que nosotros consideramos más importantes son las siguientes:
- **Cutechess:** este conjunto de herramientas está diseñado para trabajar con motores de ajedrez. Entre sus funciones más importantes, se destaca la capacidad de generar "torneos" de ajedrez contra otros motores existentes para evaluar la performance de nuestro algoritmo
- **Lichess API:** Lichess es una de las plataformas de ajedrez líderes a nivel global. Su API permite conectar nuestros bots de ajedrez personalizados para poder jugar contra otros jugadores en línea, de manera que podamos evaluar su performance en un entorno real.

Más adelante, veremos que aún antes de enfrentar a nuestro modelo contra otros motores, podemos obtener algunas métricas interesantes para poder evaluar qué tal evoluciona en su entrenamiento.

### Obtención de datos

Además, otro punto principal es de dónde obtener los datos de entrenamiento. Para esto, existen diversas bases de datos de partidas de ajedrez, que contienen millones de partidas jugadas tanto por jugadores profesionales como amateur. La anteriormente mencionada Lichess contiene una de las bases de datos más populares, y es la que utilizaremos para llevar a cabo este proyecto.

### Alcances y limitaciones

Una vez analizadas las variables anteriores, debemos decidir cuáles son los objetivos que queremos alcanzar. 

Una de nuestras limitaciones principales es la falta de recursos de cómputo. Suponiendo que conseguimos solucionar todos los demás problemas, el entrenamiento de un motor de ajedrez es un proceso sumamente costoso, por lo que tendremos que usar una cantidad de datos limitada para llevar a cabo el proceso de entrenamiento.

### El algoritmo

Luego de investigar la bibliografía existente, encontramos una serie de algortimos

La base del ajedrez algorítmico consiste en una representación del estado actual del tablero, junto con todos los posibles movimientos posteriores en forma de árbol.

La idea, es usar una *best first search* y así evaluar cuál es el mejor movimiento según el beneficio que nos produce.

Para esto se suelen utilizar dos tipos de árboles: los árboles de Montecarlo y el algoritmo Minimax.

La desventaja de Minimax consiste en que debe combinarse con algoritmos de poda para reducir el espacio de búsqueda, y necesita una excelente función de evaluación que muchas veces es difícil de encontrar.

Por esos motivos, elegimos utilizar árboles de búsqueda de Montecarlo para llevar a cabo nuestro desarrollo.

## ¿Por qué usar IA?

El ajedrez resulta un excelente caso de estudio para aplicar algoritmos complejos de IA por un motivo sencillo: la cantidad de posibles estados del tablero es extremadamente grande, por lo que resulta imposible, aún para la computadora más potente, memorizar todos estos estados.

Esto nos permite desarrollar algoritmos que no solo memoricen estados posibles del tablero, sino que aprendan a jugar al ajedrez por sí mismos, y que puedan adaptarse a cualquier situación que se les presente.

## Listado de actividades a desarrollar

1. Investigación en la bibliografía y planteos previos(4 días)
2. Diagramado del algoritmo de evaluación (2 días)
3. Implementación del algoritmo de evaluación (4 días)
4. Entrenamiento inicial (1 día)
5. Integración con distintos frameworks para obtener métricas fieles (3 días)
6. Ajuste de hiperparámetros y entrenamiento final (4 días)
7. Análisis de resultados y obtención de métricas (2 días)
8. Documentación y presentación (2 días)