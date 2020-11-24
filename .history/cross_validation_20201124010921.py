from sklearn.model_selection import StratifiedKFold

print(skf) StratifiedKFold(n_splits=2, random_state=None, shuffle=False) for train_index, test_index in skf.split(X, y): ... print("TRAIN:", train_index, "TEST:", test_index) ... X_train, X_test = X[train_index], X[test_index] ... y_train, y_test = y[train_index], y[test_index] TRAIN: [1 3] TEST: [0 2] TRAIN: [0 2] TEST: [1 3]

Notes

def five_fold():

    skf = StratifiedKFold(n_splits=5, shuffle=False)

    for train_index, test_index in 

