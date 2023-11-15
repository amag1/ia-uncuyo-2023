# Introducción

Se observó que en la provincia de Mendoza los árboles podrían llegar a ser muy peligrosos debido a las temporadas de fuertes tormentas y sobre todo a la época del viento zonda. 

El objetivo detrás del presente proyecto es el de predecir aquellos especímenes que tengan un grado de inclinación peligroso a partir de sus características biológicas e información geográfica/administrativa. Para tal fin se cuenta con un conjunto de datos que contiene el censo geo referenciado del arbolado público en la ciudad de Mendoza al año 2012. 

Este desafío está presentado a través de kaggle y se puede encontrar en el siguiente link: https://www.kaggle.com/competitionsarbolado-publico-mendoza-2023/overview. El desafío está dividido en dos partes, una parte pública y otra privada. En la parte pública se realizaba una entrega y esta media el score de la predicción realizada, la cual se podía observar para verificar que tan bueno era nuestro modelo y en la parte privada se realizaba una entrega final (en una fecha estipulada) y se sumaba al score de la parte pública para obtener el score final.

# Marco Teorico

El problema sobre el cual nos encontramos nos lleva a pensar que un modelo de clasificación es el más adecuado para resolverlo. En este caso, se trata de un problema de clasificación binaria, ya que se busca predecir si un árbol es peligroso o no.

Explayando un poco más sobre nuestro dataset, se puede observar que el mismo cuenta con 11 variables:



    id: int

    especie: string

    ultima_modificacion: date

    altura: string

    circ_tronco_cm: int

    diametro_tronco: string

    long: float

    lat: float

    seccion: int

    nombre_seccion: string

    area_seccion: float

Y también cuenta con una variable categórica que es la que se busca predecir:

    inclinacion_peligrosa: int


A su vez se nos brindó un dataset de entrenamiento el cual cuenta con las variables mencionadas previamente, pero no incluye la variable de clasificación, por lo tanto, nuestro modelo de clasificación era el encargado de tomar ese dataset de entrenamiento y predecir los valores sobre si un árbol es peligroso o no.


# Diseño experimental

## Metricas

Para evaluar el modelo de clasificación se utilizó la métrica de AUC ROC, la cual es una métrica que se utiliza para evaluar la calidad de un modelo de clasificación binaria. Esta métrica se basa en el área bajo la curva ROC (Receiver Operating Characteristic) y se utiliza para comparar modelos de clasificación. Trabajando y evaluando con esta métrica nos dimos cuenta de que al trabajar con un área sobre la curva era mucho más eficiente y positivo trabajar con porcentajes de precisión y no con valores absolutos (0 o 1).

En el dataset podemos observar como las clases estaban desbalanceadas (inserte gráfico) por lo tanto, se decidió hacer un oversampling en 3 ocasiones

Realizando testeos sobre las variables, concluimos que lo mejor era utilizar todos los campos, ya que estos aportaban información relevante para la predicción.

Luego de pruebas se decidió trabajar con el modelo de clasificación de Random Forest, ya que fue el que mejor resultados nos dio.

## Herramientas utilizadas

La principal herramienta utilizada fue el lenguaje de programación r junto con su entorno de desarrollo integrado (Rstudio), a su vez se trabajó con la librería ranger (RandomForest).

Como ya se mencionó previamente, este proyecto se realizó a través de la plataforma de kaggle, por lo tanto, se utilizó la herramienta de kaggle para subir los archivos, evaluar el modelo y realizar las entregas.

## Detalle y justificación

# Análisis y discusiones de resultados

# Conclusiones

Posibles mejoras:

    Al momento de la implementación tuvimos inconvenientes con la librería "caret" de r, ya que consideramos que no está lo suficientemente bien implementada como para trabajar sobre diferentes modelos de clasificación. Por lo tanto, hubo muchos modelos y algoritmos que no fuimos capaces de probar debido a estos inconvenientes. De esta forma creemos que se podría hacer un análisis más exhaustivo aplicando otros modelos de clasificación.

    Por otro lado, consideramos que se podría mejorar el modelo de clasificación si se contara con más datos, ya que el conjunto de datos con el que se trabajó es muy pequeño y no se cuenta con la cantidad de datos suficientes como para poder entrenar un modelo de clasificación que sea lo suficientemente bueno.



# Bibliografía