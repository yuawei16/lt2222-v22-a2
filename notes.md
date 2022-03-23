# Details of implementations

## Part 1

### Randomize Text List
To generate a random samples from the corpus, what needed is way to generate an random index for the text list. Use the built-in object to generate random integers which are less than the specified total lines. Then these integers are used to arrange the order of the text list.

## Part 6

### Comparision of Models

After retraining the model using, the followings are the scores:for 2 models. 
There is alos one point to bear is that only verb or non-verb is predicted in this example. The data frame creation function just drops other labels and can be modified to give back all of them.


              precision    recall  f1-score   support

           0       0.82      0.99      0.90      7838
           1       0.48      0.04      0.07      1801

    accuracy                           0.81      9639
   macro avg       0.65      0.51      0.48      9639
weighted avg       0.75      0.81      0.74      9639

              precision    recall  f1-score   support

           0       0.81      1.00      0.90      7838
           1       0.71      0.00      0.01      1801

    accuracy                           0.81      9639
   macro avg       0.76      0.50      0.45      9639
weighted avg       0.79      0.81      0.73      9639

It seems that both models have close scores. Since this task is a binary classification, so it shouldn't matter much. When it comes to multinominal task, the RBF should perform better.
