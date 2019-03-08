from sklearn.externals import joblib

class RegressionModel(object):

    def __init__(self):
        self.model = joblib.load('RegressionModel.sav')

    def predict(self,X,feature_names):
        return self.model.predict(X)
