# TP7 - IA 1

## Respuestas a los ejercicios de la Seccion 2.4

# 1- For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

a. Si n es muy grande y p muy pequeño, se espera que un método inflexible pueda capturar los patrones de los datos de una mejor manera que un método flexible, ya que el segundo podría caer en *overfitting*.

b. Si n es pequeño y p muy grande, esperamos que el método flexible tenga una mejor performance que el método flexible.

c. Si la relación entre los predictores es altamente no-lineal, un método poco flexible (como la regresión lineal) no capturará fácilmente las características de los datos, por lo que sería más efectivo utilizar un método flexible.

d. Si sabemos que el error irreducible es muy alto, no sería conveniente utilizar un método muy flexible ya que este podría realizar *overfitting* sobre los datos

# Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

|     Clasificación o Regresión |  Inferencia o predicción | p | n |
|-------------------------------|--------------------------|---|---|
|R         |I                          |4   |500   |
|C                             |P                          |15   |20   |
|R                               |P                          |4   |52   |

# What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

Las ventajas de un approach más flexible son, entre otras: la posibilidad de capturar relaciones no lineales entre los datos, mejor manejo de datos ruidosos y detección de patrones sutiles.
Preferimos este tipo de modelos cuando nos interesa cualquiera de estos indicadores, mientras que un modelo menos flexible se prefiere si el precio a pagar por el overfitting es alto, la relación entre los datos es sencilla o necesitamos un modelo que no solo sea muy preciso sino que también sea fácil de interpretar.

# Describe the diﬀerences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a nonparametric approach)? What are its disadvantages?

Las diferencias principales son que los modelos paramétricos solo necesitan estimar un pequeño número de parámetros (en ellos suponemos que la función $f$ tiene una forma particular, como las regresiones lineales), mientras que los modelos no paramétricos no asuen nada sobre la forma de la función, lo que aumenta significativamente la cantidad de elementos que debemos estimar. Las ventajas de los modelos paramétricos sobre los no paramétricos son muy similares a las ventajas de los métodos inflexibles por sobre los flexibles.

# The table below provides a training data set containing six observations, three predictors, and one qualitative response variable. Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.

1. Distancia a los demas puntos:
   1. d((0,0,0), 1) = 3
   2. d((0,0,0), 2) = 2
   3. d((0,0,0), 3) = 3.16
   4. d((0,0,0), 4) = 2.23
   5. d((0,0,0), 5) = 1.41
   6. d((0,0,0), 6) = 1.73

2. What is our prediction with K = 1? Why?

La prediccion es igual a la clase del vecino más cercano, es decir, Verde.

3. What is our prediction with K = 3? Why?

La predicción es Rojo, ya que 2/3 de sus vecinos más cercanos tienen esa clase.

4. If the Bayes decision boundary in this problem is highly non-linear, then would we expect the best value for K to  be large or small? Why?

En ese caso, esperamos que el mejor valor de K sea pequeño, ya que la mayor varianza permite darle a la frontera una forma no lineal