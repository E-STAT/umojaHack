from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

def standard(train, test):

    sc = StandardScaler()

    train_sc = sc.fit_transform(train)
    test_sc = sc.fit_transform(test)

    return train_sc, test_sc

def MinMax(train, test):

    mx = MinMaxScaler()

    train_mx = mx.fit_transform(train)
    test_mx = mx.fit_trasform(test)

    return train_mx, test_mx

def Robust(train, test):
    
    rb = RobustScaler()

    train_rb = rb.fit

