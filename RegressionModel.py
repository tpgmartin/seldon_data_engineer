from sklearn.externals import joblib

class RegressionModel(object):

    def __init__(self):
        self.model = joblib.load('RegressionModel.sav')

    def predict(self,X):
        return self.model.predict(X)
