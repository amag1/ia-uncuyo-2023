# Pregunta 2.10: Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.

## a. Can a simple reflex agent be perfectly rational for this environment? Explain.

No, un agente reflexivo simple no podría ser perfectamente racional ya que no tiene memoria para saber si ya pasó por un lugar o no, por lo que podría estar dando vueltas en círculos y perdiendo puntos. Tampoco conoce el estado de todo el entorno, por lo que no puede planificar la mejor ruta para minimizar las penalizaciones

## b. What about a reflex agent with state? Design such an agent.

A menos que supongamos que el entorno es totalmente observable, este agente no podría diseñarse, ya que a pesar de que el agente tenga un estado para no visitar un mismo casillero dos veces, si no conoce todo su entorno no puede calcular la ruta más eficiente, y por lo tanto sería penalizado por moverse de más.

## c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?

Si el agente tuviera información sobre cada casillero del entorno, podría diseñarse un agente reflexivo con estado que fuera perfectamente racional, ya que podría calcular la ruta más eficiente para limpiar todos los casilleros y no pasar dos veces por el mismo. Para diseñar este agente, podríamos utilizar algunas de las estrategias de búsquedas que se presentan en el siguiente capítulo

---

# Pregunta 2.11: Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right .)

## a. Can a simple reflex agent be perfectly rational for this environment? Explain.

Suponiendo que en este caso el agente no incurre en penalizaciones por realizar movimientos de más, un agente reflexivo puede ser perfectamente racional, ya que puede ir limpiando los casilleros a medida que los va visitando. Si bien no conoce el estado inicial del entorno, puede ir limpiando los casilleros que va visitando y eventualmente limpiar todo el entorno.

## b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.

A partir de la experiencia generada en los ejericios **D** y **E**, podemos ver que un agente aleatorio no tiene mejor rendimiento que un agente reflexivo simple. Sin embargo, si solo nos interesa que limpie completamente el entorno y no penalizarlo por los movimientos extra, también podemos considerar a este agente como perfectamente racional.

## c. Can you design an environment in which your randomized agent will perform poorly? Show your results.

Un agente aleatorio puede tener un rendimiento pobre en un entorno en el que la probabilidad de que un casillero esté sucio sea muy baja, y también, como puede verse en los resultados de los ejercicios **D** y **E**, en un entorno que tenga un tamaño extremandamente grande, ya que la probabilidad de que el agente pase por un casillero sucio es muy baja.

## d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?

Sí, un agente con estado puede tener un mejor rendimiento que un agente reflexivo simple, ya que puede recordar los casilleros que ya visitó y no pasar dos veces por el mismo. Sin embargo, si el entorno es muy grande, el agente puede pasar por muchos casilleros sucios antes de limpiarlos, por lo que tampoco es una solución ideal al problema.
