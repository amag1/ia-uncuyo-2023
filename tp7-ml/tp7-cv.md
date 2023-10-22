## TP7 - ML

### Create folds

```
reate_folds <- function(df, k){
  shuffled_data= df[sample(1:nrow(df)), ] 
  
   # Calculate the number of rows in each fold
  fold_size <- nrow(shuffled_data) %/% k
  fold_sizes <- rep(fold_size, k)
  
  # Distribute the remaining rows if any
  remaining_rows <- nrow(shuffled_data) %% k
  fold_sizes[1:remaining_rows] <- fold_sizes[1:remaining_rows] + 1
  
  # Split the shuffled dataframe into k folds
  folds <- split(shuffled_data, rep(1:k, fold_sizes))
  
  # Convert the folds to a list
  fold_list <- as.list(folds)

  return(fold_list)
}
```

### Cross-validation

```
cross_validation <- function(df, k, tformula) {
  folded_data <- create_folds(df, k)
  
  result <- data.frame(
      Accuracy = numeric(),
      Precision = numeric(),
      Sensitivity = numeric(),
      Specificity = numeric()
    )
  for (i in 1:length(folded_data)) {
    validation_set <- folded_data[[i]]
    trainings_sets <- folded_data[-i]
    
    training_df <- do.call(rbind, trainings_sets)
    
    tree_model <- rpart(tformula, data = training_df)
    p <- predict(tree_model, validation_set, type="class")
    
    true_labels <- validation_set$inclinacion_peligrosa
    crow <- confusion_matrix_imp(data = p, reference = true_labels) %>% get_metrics()
    result[nrow(result) + 1, ] <- crow
  }
  
  return(result)
}
```

## Resultados

- | Accuracy | Precision | Sensitivity | Specificity
--- | --- | --- | --- | ---
**Media** | 0.89360973 |	1 | 	0.89360973 |	NaN
**Desviación estándar** | 0.01773428 |	0 |	0.01773428 |	NA