from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import category_encoders as ce


class Encoding(self, train, test, columns, target):

    '''
    This class will perform Label Encoding, One hot encoding and target encoding
    '''

    self.train = train
    self.test = test
    self.columns = columns
    self.target = target

    def Label_encode(self, train, test):

        lb = LabelEncoder()
        




