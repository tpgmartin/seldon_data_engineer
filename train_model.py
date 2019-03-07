import pandas as pd
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression

def main():
    regr = LinearRegression()
    print('Training model...')
    regr.fit(X_train, y_train)
    print('Model trained!')

    filename = 'RegressionModel.sav'
    print('Saving model in %s' % filename)
    joblib.dump(regr, filename)
    print('Model saved!')
    
if __name__ == "__main__":
    X_train = pd.read_csv('./data/X_train.csv', index_col='index')
    y_train = pd.read_csv('./data/y_train.csv', index_col='index')
    X_test = pd.read_csv('./data/X_test.csv', index_col='index')
    main()