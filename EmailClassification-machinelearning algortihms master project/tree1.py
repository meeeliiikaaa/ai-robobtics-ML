from sklearn import tree
from util import MAIL_TYPE_FIELD, DATE_FIELD, ORG_FIELD, TLD_FIELD, LABEL_FIELD

def predictionGenerator(train_x, train_y, test_x):


    for dataSet in [ train_x, test_x ]:
        del dataSet[DATE_FIELD]
        del dataSet[ORG_FIELD]
        del dataSet[MAIL_TYPE_FIELD]
        del dataSet[TLD_FIELD]
        if LABEL_FIELD in dataSet.columns:
            del dataSet[LABEL_FIELD]

    classifier = tree.DecisionTreeClassifier()
    classifier.fit(train_x, train_y)
    
    prediction = classifier.predict(test_x)

    return prediction