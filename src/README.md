
Sberbank Housing Data
292 variables
30471 rows



Progress
1. Trying to run a normal linear regression without any data preprocessing
2. Had to remove columns of dtype = "O", of which there were around 15 columns. Will come back to these later
3. Came across NaN values. For now, just removed all the rows that NaN values. This led to removal of 80% of the data
4. Just learnt that the the columns that you removed from the training data because they had NA values have to be removed from the test dataset as well4. Just learnt that the the columns that you removed from the training data because they had NA values have to be removed from the test dataset as well4. Just learnt that the the columns that you removed from the training data because they had NA values have to be removed from the test dataset as well4. Just learnt that the the columns that you removed from the training data because they had NA values have to be removed from the test dataset as well


Ideas
1. Convert the "O" dtype columns to as.numeric() and remove the ones that cannot be convered to numeric
