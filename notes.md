# Details of implementations

## Part 1

### Randomize Text List
To generate a random samples from the corpus, what needed is way to generate an random index for the text list. Use the built-in object to generate random integers which are less than the specified total lines. Then these integers are used to arrange the order of the text list.

## Part 6

### Comparision of Models

The text "/scratch/UN-english.txt.gz" is not found when forked the repo, so a mini text is comipiled for just demo. 
There is alos one point to bear is that only verb or non-verb is predicted in this example. The data frame creation function just drops other labels and can be modified to give back all of them.


              precision    recall  f1-score   support

           0       0.82      0.85      0.84       218
           1       0.38      0.33      0.36        60

    accuracy                           0.74       278
   macro avg       0.60      0.59      0.60       278
weighted avg       0.73      0.74      0.73       278


              precision    recall  f1-score   support

           0       0.78      1.00      0.88       218
           1       0.00      0.00      0.00        60

    accuracy                           0.78       278
   macro avg       0.39      0.50      0.44       278
weighted avg       0.61      0.78      0.69       278

For the caculation of the scores for RBF model an error occurd whcih did not produce the scores for the positive label. But we can see that the linear model is better than the RBF for all 3 scores. 
One of the reason that RBF did not produce any good scores is that the parameters of creating RBF may not be set properly.