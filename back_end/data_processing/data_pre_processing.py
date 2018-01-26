# # Importing the libraries
# import pandas as pd
#
# from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
# from sklearn.model_selection import train_test_split
#
# '''
#     Parts of this file were adapted from Machine Learning A-Z.
#     https://www.udemy.com/machinelearning/learn/v4/overview
# '''
#
#
# # TODO: Have a different pipeline for data that has multiple output features.
# # TODO: Have some parameters to determine which line(s) to skip. I.E. first row might be labels that are useless
# # TODO: Same as above with columns, cause could be irrelevant (in this case names)
# # TODO: Ask for user input about which col is the results (default would be last one)
# # TODO: For the webpage, might wanna make a specific layout file to carry style through pages: https://youtu.be/zRwy8gtgJ1A?t=13m32s
# def pre_process_data(file):
#     # Importing the dataset
#     dataset = pd.read_csv('uploads/' + file)
#
#     # import ipdb;
#     # ipdb.set_trace()
#
#     # TODO: RESTART OVER HERE, NEED TO FIGURE OUT HELLA PRE PROCESSING, also figure out the stuff on the front end from above
#
#     X = dataset.iloc[:, :-1].values  # These are the features
#     y = dataset.iloc[:, -1].values  # This is the result
#
#     # In the case of missing data, we can fill it in with the mean of the rest of the data.
#     # I presume that this is because taking the mean of something will not significantly
#     # affect the median, and will have no effect on the mean of the whole data set.
#     # removing the data point is disastrous, doing so could leave out extremely important
#     # information.
#
#     imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
#     imputer = imputer.fit(X[:, :-1])  # upper bound is excluded
#     X[:, :-1] = imputer.transform(X[:, :-1])
#
#     # Since we have multiple types of labels in our dataset, and it would be bad to
#     # have that appear in our machine learning model, we want to definitely change
#     # it to one-hot, this will ensure that we represent each label correctly as a number
#
#     # The reason this labelEncoder is bad is because it gives each label a presumed
#     # weight. This would be ideal if we can compare values that have a defined weight.
#     # Ex: Large (3) > Medium (2) > Small (1). Hence it makes the most sense to do Label Encoding.
#
#     # But we must do this step so that we can one hot encode.
#     labelEncoder_X = LabelEncoder()
#     X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])  # NOTICE THIS IS BAD FOR THE CURRENT EXAMPLE
#
#     # However for this example it would be most ideal to instead use OneHotEncoder, because
#     # We can't compare the countries easily
#     oneHotEncoder = OneHotEncoder(categorical_features=[0])
#     X = oneHotEncoder.fit_transform(X).toarray()
#
#     # don't forget to do it for the purchased boolean col.
#     labelEncoder_y = LabelEncoder()
#     y = labelEncoder_y.fit_transform(y)
#
#     # Ideally we want to split our dataset into a training and a test set,
#     # this is because we don't want our model to learn the correlation of one set too
#     # well. If it does, then we'll have trouble, because then it won't be well adapted
#     # when given a new data set. For this, reason we split it into a training and test set.
#     # accuracy will be roughly the same between both sets
#
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#
#     # Now we want to feature scale, the reason we do this is because if the features
#     # are on different scales, then obviously if one has a much larger range than another
#     # one of the features could be completely off.
#     # We can use two methods to scale the features, standardization and normalization.
#
#     sc_X = StandardScaler()
#     X_train = sc_X.fit_transform(X_train)
#     X_test = sc_X.fit_transform(X_test)
#
#     return X_train, X_test, y_train, y_test

import pandas as pd
from sklearn import preprocessing


def _binaryOneHot(df, attribute_map):
    """
        Takes in map with keys of attributes, and value of a list of the 0 and 1 values
        Ex:
            {
                "school": ["GP", "MS"]
                "sex": ["F","M"]
            }
        :return: New, replaceable dataframe with replaced values
    """
    for key in attribute_map:
        df[key] = df[key].map({attribute_map[key][0]: 0, attribute_map[key][1]: 1})

    return df


def _normalizer(df, attribute_list):
    """
        Takes in list of attributes
        Ex:
            ["age"]
        :return: New, replaceable dataframe with replaced values
    """
    # for normalizing
    min_max_scaler = preprocessing.MinMaxScaler()

    for attribute in attribute_list:
        df_scaled = min_max_scaler.fit_transform(df[attribute].values.reshape(-1, 1))
        df[attribute] = df_scaled

    return df


def _multiOneHot(df, attribute_list):
    """
        Takes in list of attributes
        Ex:
            ["age"]
        :return: New, replaceable dataframe with replaced values
    """
    for attribute in attribute_list:
        one_hot = pd.get_dummies(df[attribute], prefix=attribute)
        df = pd.concat([df, one_hot], axis=1)
        df.drop([attribute], axis=1, inplace=True)

    return df


def getCleanData(file_path, attributes, binary_one_hot_map=None, normalize_list=None, multi_one_hot_list=None,
                 cols_to_drop=None, row_num_to_drop=None):
    """
    :return: Cleaned data
    """
    # read in data
    data = pd.read_csv(file_path, names=attributes)

    # dropping rows we don't need
    if not (row_num_to_drop is None):
        data.drop(data.index[row_num_to_drop], inplace=True)

    # replace binary variables with 1/0
    if not (binary_one_hot_map is None):
        data = _binaryOneHot(data, binary_one_hot_map)

    # normalize values to prevent them from having too much of a weight
    if not (normalize_list is None):
        data = _normalizer(data, normalize_list)

    # one-hot encode multiple categorical values
    if not (multi_one_hot_list is None):
        data = _multiOneHot(data, multi_one_hot_list)

    # drop col_to_drop column
    if not (cols_to_drop is None):
        for col in cols_to_drop:
            data = data.drop(col, axis=1)

    return data


