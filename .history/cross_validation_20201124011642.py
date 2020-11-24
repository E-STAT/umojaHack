from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score



def five_fold(X, y, model_train = None):

    skf = StratifiedKFold(n_splits=5, shuffle=False)

    for train_index, test_index in skf.split(X,y):
        X_train, X_test = X.loc[train_index], X.loc[test_index]
        y_train, y_test = y.loc[train_index, y.loc[test_index]]

        ###########################Calling Training Function
        model_train(X_train, y_train)

