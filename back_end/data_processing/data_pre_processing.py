# Importing the libraries
import pandas as pd

from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

'''
    Parts of this file were adapted from Machine Learning A-Z.
    https://www.udemy.com/machinelearning/learn/v4/overview
'''


# TODO: Have a different pipeline for data that has multiple output features.
# TODO: Have some parameters to determine which line(s) to skip. I.E. first row might be labels that are useless
# TODO: Same as above with columns, cause could be irrelevant (in this case names)
# TODO: ask for user input about which col is the results (default would be last one)
def pre_process_data(file):
    # Importing the dataset
    dataset = pd.read_csv('uploads/' + file)

    # import ipdb;
    # ipdb.set_trace()

    # TODO: RESTART OVER HERE, NEED TO FIGURE OUT HELLA PRE PROCESSING, also figure out the stuff on the front end from above

    X = dataset.iloc[:, :-1].values  # These are the features
    y = dataset.iloc[:, -1].values  # This is the result

    # In the case of missing data, we can fill it in with the mean of the rest of the data.
    # I presume that this is because taking the mean of something will not significantly
    # affect the median, and will have no effect on the mean of the whole data set.
    # removing the data point is disastrous, doing so could leave out extremely important
    # information.

    imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
    imputer = imputer.fit(X[:, :-1])  # upper bound is excluded
    X[:, :-1] = imputer.transform(X[:, :-1])

    # Since we have multiple types of labels in our dataset, and it would be bad to
    # have that appear in our machine learning model, we want to definitely change
    # it to one-hot, this will ensure that we represent each label correctly as a number

    # The reason this labelEncoder is bad is because it gives each label a presumed
    # weight. This would be ideal if we can compare values that have a defined weight.
    # Ex: Large (3) > Medium (2) > Small (1). Hence it makes the most sense to do Label Encoding.

    # But we must do this step so that we can one hot encode.
    labelEncoder_X = LabelEncoder()
    X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])  # NOTICE THIS IS BAD FOR THE CURRENT EXAMPLE

    # However for this example it would be most ideal to instead use OneHotEncoder, because
    # We can't compare the countries easily
    oneHotEncoder = OneHotEncoder(categorical_features=[0])
    X = oneHotEncoder.fit_transform(X).toarray()

    # don't forget to do it for the purchased boolean col.
    labelEncoder_y = LabelEncoder()
    y = labelEncoder_y.fit_transform(y)

    # Ideally we want to split our dataset into a training and a test set,
    # this is because we don't want our model to learn the correlation of one set too
    # well. If it does, then we'll have trouble, because then it won't be well adapted
    # when given a new data set. For this, reason we split it into a training and test set.
    # accuracy will be roughly the same between both sets

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Now we want to feature scale, the reason we do this is because if the features
    # are on different scales, then obviously if one has a much larger range than another
    # one of the features could be completely off.
    # We can use two methods to scale the features, standardization and normalization.

    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.fit_transform(X_test)

    return X_train, X_test, y_train, y_test
