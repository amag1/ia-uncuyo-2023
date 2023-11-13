## TP7 - IA 2023

### Reporte arbolado público

#### A. Descripción del proceso de preprocesamiento

En esta etapa, comenzamos con el análisis exploratorio de los datos que nos arrojó resultados interesantes.

Algunas variables estaban muy correlacionadas, por lo que se decidió quitarlas (por ejemplo, el nombre de la sección, la latitud y la longitud).

También intentamos, en diferentes instancias, eliminar aquellas variables que parecían tener menor importancia y crear nuevas variables categóricas (por ejemplo, para el diámetro del tronco), aunque finalmente desisitimos de esta estrategia porque la mejora en performance no era significativa.

#### B. Resultados sobre el conjunto de validación

Al ejecutar el algoritmo sobre el conjunto de validación, observamos una excelente performance. Utilizamos la métrica _ROC_ y conseguimos un valor superior al 90%.

#### C. Resultados obtenidos en Kaggle

En Kaggle, obtuvimos un score público de 0.77 y un score privado de 0.78

#### D. Descripción del algoritmo utilizado

El algoritmo que utilizamos puede resumirse de la siguiente manera:

1. Comenzamos extrayendo las variables importantes, como se menciona en el inciso A.
2. Luego, realizamos _oversampling_ para balancear las clases. Este proceso fue hecho manualmente: triplicamos las entradas que pertenecían a la clase minoritaria.
3. En tercer lugar, entrenamos el modelo. Utilizamos _random forest_ a través del paquete Ranger. Luego de múltiples pruebas, determinamos que alrededor de 250 árboles se obtenía el mejor resultado.
4. No se dividió el conjunto de datos en train y test, ya que queríamos obtener la mejor performance posible en el desafío de Kaggle, y al entrenar con todos los datos, nuestro modelo respondía de mejor manera.
