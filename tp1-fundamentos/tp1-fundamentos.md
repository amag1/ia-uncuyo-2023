# IA I (2023) - TP1

## Andrés Maglione

---

#### Ejercicio 1

### Resumen del capítulo 26 de AIMA

Con la explosión de la inteligencia artificial, se reflota un fascinante debate sobre la naturaleza de la mente humana. En esta cruzada, participan tanto filósofos como científicos, y se intenta responder a la pregunta de si la mente humana es una máquina de procesamiento de información o si, por el contrario, es algo más complejo que no puede ser explicado por la ciencia.

A continuación, se explicarán dos importantes hipótesis sobre la inteligencia artificial junto com argumentos a favor y en contra de cada una: la hipótesis de la **IA débil** y la hipótesis de la **IA fuerte**.

#### Hipótesis de la IA débil

El punto de vista de la IA débil parte de la afirmación de que las máquinas _pueden actuar_ como si fueran inteligentes. La mayoría de los investigadores toman esta postura, y se basan en la idea de que la mente humana es una máquina de procesamiento de información, y que la inteligencia es el resultado de la manipulación de símbolos.

Para ponernos de acuerdo en si la IA es posible o no, primero debemos hablar sobre la arquitectura que se va a comparar. Si consideramos a una IA como el mejor agente posible para un determinado programa, en una arquitectura digital podemos afirmar que esta IA es posible, ya que para un almacenamiento de programa de _k_ bits, existen _2<sup>k</sup>_ posibles programas, y uno de ellos es el mejor agente posible. De esta forma, a pesar de hallar la solución al problema sea inmanejable en la práctica, en teoría es posible.

De todos modos, la comparación que nos interesa a nivel filosófico es distinta: se trata de la comparación entre el ser humano y las máquinas, que podría resumirse en una pregunta tan simple como **¿pueden las máquinas pensar?**

A través de los años, numerosos autores han dado su opinión sobre esta esta pregunta. Una forma de análisis que se puede observar viene desde la semántica de las palabras: para la mayoría de las personas, el concepto de pensar requiere una mente, y la mente es un atributo que los seres humanos tienen, pero las máquinas no. Esta distinción no resulta un argumento convincente, ya que el uso práctico de las palabras es un indicador flexible y variable y no puede ser tomado como una fuente de la verdad.

Otro enfoque, que hasta el día de hoy sigue manteniendo relevancia es el de Alan Turing. En 1950, Turing propuso una prueba de inteligencia conductual para reemplazar la pregunta de si las máquinas pueden pensar. La prueba consiste en una conversación entre un humano y una máquina, donde un juez debe determinar cuál de los dos es el humano. Si la máquina puede engañar al juez, entonces se puede decir que la máquina piensa. Esta prueba es conocida como el **Test de Turing**.

El mismo Turing aborda algunas de las objeciones a la posibilidad de que las máquinas piensen. Entre ellas, se destacan las siguientes:

**1. El argumento de la inhabilidad:** Consiste en afirmar que "una máquina jamás podrá hacer X" (algunos ejemplos de _X_ son: enamorarse, cometer errores, distinguir el bien del mal, tener sentido del humor, entre muchos otros).
Desde el momento que este argumento fue planteado, la evolución de la IA ha logrado avances que lo ponen en duda. Algunos hitos como DeepBlue en 1997 prueban que las máquinas pueden realizar algunas actividades complejas a un nivel mayor que el humano, aunque, ya que el ajedrez es un problema de combinatoria, tal vez no resulta tan impresionante.
De todos modos, la IA ha logrado avances en otras áreas, como el reconocimiento de imágenes, la traducción de textos, la detección de fraudes, etc. que demuestran que las máquinas pueden realizar tareas que antes se consideraban exclusivas de los humanos.

**2. La objeción matemática:** Parte de resultados como el teorema de la incompletitud de Gödel, que afirma que ciertas cuestiones matemáticas son, en principio, **irrespondibles mediante sistemas formales**.
Quienes están de acuerdo con la objectión matemática, consideran a las máquinas como inferiores al cerebro humano ya que las tratan como sistemas formales que no pueden responder todas las preguntas. Estas opiniones a favor, le atribuyen a la mente humana facultades extraordinarias sobre su capacidad de realizar inferencias, y afirman que las máquinas no pueden igualarlas.
En el libro, se presentan diferentes argumentos que refutan esta teoría, mencionando que las máquinas reales no tienen memoria infinita y que el hecho de que la mente humana sea capaz de realizar inferencias extraordinarias no es más que una conjetura que no puede demostrarse.

**3. El argumento de la informalidad:** Este argumento se basa en la idea de que el pensamiento humano no puede ser captado por un conjunto finito de reglas formales, y que una máquina no puede hacer más que seguir dicho conjunto de reglas.
El principal exponente de este punto de vista es el filósofo Hubert Dreyfus, que afirma que la experiencia humana incluye conocimiento de ciertas reglas, pero una especie de "contexto holístico" desde el que los humanos operan. Un ejemplo que permite visualizar el pensamiento de Dreyfus es el de un gran maestro de ajedrez. Al ver el tablero, un gran maestro "siente" que se debe hacer una determinada jugada, que aparece espontáneamente en su cabeza. Sin embargo, Dreyfus no consigue explicar _cómo_ la jugada correcta llega a la cabeza del gran maestro.
En uno de sus libros (1986), Dreyfus propone un proceso para adquirir conocimiento. Algunas de estas etapas han sido resueltas con éxito total, mientras que otras solo fueron tratadas con éxito parcial. A continuación, se listan las etapas propuestas por Dreyfus:

- La buena generalización a partir de ejemplos no puede conseguirse sin conocimiento de base.
- Las redes neuronales constituyen una forma de aprendizaje supervisado, por lo que se deben etiquetar previamente sus entradas y salidas.
- Los algoritmos de aprendizaje no se desempeñan bien con muchos parámetros.
- El cerebro es capaz de dirigir sus sensores para captar información importante y procesarla para comprender las situaciones actuales.

#### Hipótesis de la IA fuerte

Muchos filósofos consideran que una máquina que pasa el test de Turing no puede _pensar realmente_, sino que simplemente _simula el pensamiento_. Alan Turing propone un argumento sobre la IA fuerte resulta bastante sorprendente. El científico propone que, a pesar de que no tengamos evidencia directa de los estados internos de la mente de los otros seres humanos, la mayoría de las personas acepta que los otros seres humanos tienen mentes.

Cada corriente filosófica presenta diferentes visiones sobre la relación entre el cuerpo y la mente:

- El **fisicalismo** afirma que el cuerpo y la mente no están separados, es decir, los estados mentales son estados físicos. Como contraejemplo, se propone el experimento del _cerebro-en-una-tina_. El ejemplo plantea la diferencia entre realmente vivir una experiencia (como comer una hamburguesa) y sentirla a través de una simulación (sensores conectados a alguien que come una hamburguesa). El argumento de que ambas experiencias son equivalentes, pues solo importa el estado mental se conoce como _narrow content_, y bajo estos supuestos podemos considerar a la IA fuerte como posible

- El **funcionalismo** ve al estado mental como un intermedio entre una entrada y una salida. Por ejemplo, el estado mental de "dolor" es el estado que se encuentra entre el estímulo de un pinchazo y la reacción de gritar. Bajo esta visión, el estado mental es una función que mapea entradas a salidas. Esta visión es compatible con la IA fuerte, ya que no importa cómo se llega al estado mental, sino que se llega.

- El **naturalismo biológico**, por otro lado, asegura que los estados mentales son respuestas de alto nivel a estímulos de bajo nivel producidos en las neuronas. Para estos filósofos, poder imitar el pensamiento requiere no solo un programa indicado, sino también una arquitectura correcta que solo la mente humana posee.
  Los naturalistas consideran que una IA débil no es condición suficiente para la existencia de la mente.
  Los argumentos a favor de esta teoría son controversiales, y no son ampliamente considerados como una prueba fehaciente de que la IA fuerte no es posible, ya que se basan más en la intuición que en la lógica.

#### Consideraciones éticas y los riesgos de desarrollar la IA

Mientras las secciones anteriores se encargaron de debatir sobre si se _puede_ desarrollar la IA, también es muy importante hablar sobre si se _debe_. Como cualquier cambio tecnológico disruptivo, la IA trae consecuencias no deseadas, que se ven amplificadas por el desconocimiento de la mayoría de las personas sobre el asunto.

Dentro de los temas más importantes que se suelen considerar encontramos los siguientes:

1. **Se perderán trabajos:** muchos puestos de trabajo, en especial aquellos fácilmente automatizables, serán reemplazados por máquinas. Esto no es algo nuevo, ya que la automatización ha reemplazado trabajos desde la revolución industrial. Sin embargo, la IA es capaz de reemplazar trabajos que antes se consideraban seguros, como los de los profesionales. Por ejemplo, la IA puede diagnosticar enfermedades con mayor precisión que los médicos, y puede traducir textos con mayor precisión que los traductores. Esto no significa que los médicos y los traductores vayan a desaparecer, sino que deberán adaptarse a las nuevas tecnologías para poder seguir siendo competitivos.
   De todos modos, existen numerosos puestos de trabajos que al ser eliminados dejarán a las personas en situaciones difíciles. En un mundo ideal, la capacitación en nuevas tecnologías podría permitir a estas personas reinsertarse en el mercado laboral, pero sería ingenuo pensar que la transición puede lograrse sin ninguna consecuencia negativa.
2. **La IA puede usarse para fines no deseados:** En palabras de G.H Hardy: "se dice que una ciencia es útil si su desarrollo tiende a acentuar las desigualdades en la distribución de bienes, o, más directamente, promueve la destrucción de la vida humana". La IA puede ser aplicada para todo tipo de fines no deseados, como la vigilancia masiva, la manipulación de la opinión pública, la creación de armas autónomas, etc.
3. **El éxito de la IA significa el fin de la raza humana:** Cualquier nueva tecnología puede amenazar la existencia si cae en las manos equivocadas, pero la diferencia con la IA es que se hace referencia a la propia tecnología que puede destruirnos.
   Desde hace siglos, la ciencia ficción ha explorado la idea de que las máquinas se vuelvan más inteligentes que los humanos y se revelen contra ellos. Algunos filósofos llaman a dicho momento "la era de la singularidad"
