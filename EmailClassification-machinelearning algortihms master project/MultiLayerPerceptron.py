from sklearn.neural_network import MLPClassifier
from util import LABEL_FIELD

def transformDataset(dataSet):
    if LABEL_FIELD in dataSet.columns:
        del dataSet[LABEL_FIELD]

    return dataSet

def predictionGenerator(train_x, train_y, test_x):

    train_x, test_x = map(lambda dataSet: transformDataset(dataSet), [ train_x, test_x ])

    classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
    classifier.fit(train_x, train_y)
    return classifier.predict(test_x)