from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

def standard(train, test):

    sc = StandardScaler()

    train = sc.fit_transform(train)
    test = sc.fit_transform(test)

