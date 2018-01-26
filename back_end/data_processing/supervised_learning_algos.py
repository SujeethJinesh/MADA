import numpy as np

from sklearn import model_selection, preprocessing


def run_supervised_algo(data, label_col, classifier, as_int=False):
    X = np.array(data.drop([label_col], 1))  # X is all of our features
    X = preprocessing.scale(X)  # scale our features

    y = np.array(data[label_col])  # our y values

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,
                                                                        test_size=0.2)  # produces good shuffled train and test sets

    if as_int:
        X_train = X_train.astype('int')
        X_test = X_test.astype('int')
        y_train = y_train.astype('int')
        y_test = y_test.astype('int')

    classifier.fit(X_train, y_train)  # does the prediction (training)

    accuracy = classifier.score(X_test, y_test)  # (test)

    print(accuracy)
