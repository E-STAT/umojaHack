from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

def standard(train, test):

    sc = StandardScaler()

    train_sc = sc.fit_transform(train)
    test_sc = sc.fit_transform(test)

    return train_sc, test_sc

def 

