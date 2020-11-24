from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score



def strat_fold(X, y, test, num_splits, model_train = None, model_pred = None, model_eval = None):

    '''
    This function will do all kinds of stratified kfold
    input:
    X = features
    y = target
    num_splits = number of fold
    model_train = function for training the model
    model_pred = function for model prediction
    model_eval = function for model evaluation

    output:
    y_pred = predictions list of
    '''

    skf = StratifiedKFold(n_splits=num_splits, shuffle=False)
    y_pred = []
    y_eval = []

    for train_index, test_index in skf.split(X,y):
        X_train, X_test = X.loc[train_index], X.loc[test_index]
        y_train, y_test = y.loc[train_index, y.loc[test_index]]

        ###########################Calling Training Function
        model_train(X_train, y_train)
        y_eval_pred = model_pred(X_test)
        eval_metric = model_eval(y_test, y_eval_pred)
        prediction_y = model_pred(test)

        y_eval.append(eval_metric)
        y_pred.append(prediction_y)

    return y_pred, y_eval


