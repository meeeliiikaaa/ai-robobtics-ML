from sklearn.linear_model import LogisticRegression
from util import LABEL_FIELD

def transformDataset(dataSet):
    if LABEL_FIELD in dataSet.columns:
        del dataSet[LABEL_FIELD]

    return dataSet

def predictionGenerator(train_x, train_y, test_x):

    train_x, test_x = map(lambda dataSet: transformDataset(dataSet), [ train_x, test_x ])

    logisticRegression = LogisticRegression(solver='lbfgs', multi_class='multinomial').fit(train_x, train_y)
    return logisticRegression.predict(test_x)