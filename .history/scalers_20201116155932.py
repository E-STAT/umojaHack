from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

def standard(train, test):

    sc = StandardScaler()

    train_sc = sc.fit_transform(train)
    test_sc = sc.fit_transform(test)

    return train_sc, test_sc

def MinMaxScaler(train, test):

    mx = MinMaxScaler()

    train_mx = mx.fit_transform(train)
    test_mx = mx.fit

