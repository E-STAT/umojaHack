from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import category_encoders as ce


class Encoding(self, train, test, columns = None, target):

    '''
    This class will perform Label Encoding, One hot encoding and target encoding
    '''

    self.train = train
    self.test = test
    self.columns = columns
    self.target = target

    def Label_encode(self, train, test):

        # lb = LabelEncoder()
        # y = train[target]
        # X = train.drop(target, axis = 1)
        train = ce.OrdinalEncoder(train)
        test = ce.OrdinalEncoder(test)
        return train, test

    def One_hot(self, train, test):

        train = ce.OneHotEncoder(train)
        test = ce.OneHotEncoder(test)

        return train, test

    def target



