--------------------------------------------------
SELDON TECHNOLOGIES DATA ENGINEERING EXERCISE
--------------------------------------------------

INSTRUCTIONS
------------
The goal of this exercise is to assess your engineering skills and reasoning when going from a raw dataset to a deployed machine learning model running on Seldon Core.

The exercise is in two parts:

 - Create a simple machine learning model from the provided data and return predictions from the test set
 - Create a deployment for your model on Seldon Core


PART 1 - Model Creation
-----------------------

You should have 3 files in your possession:
 - X_train.csv
 - y_train.csv
 - X_test.csv

* X_train.csv contains the features on the training set. The columns are an index followed by 20 features. There are 10,000 rows.
* y_train.csv contains the target on the training set. The columns are an index and the target. There are 10,000 rows.
* X_test.csv contains the features on the test set. The format is the same as X_train.csv

For each sample in the test set, you must predict a target variable. The joint probability distributions P(X,y) are identical on the train and test set. You should use the Mean Squared Error as the performance metric for your model.
The format of the file containing your predictions should be identical to y_train.csv: a csv file that contains an index column, a target column, and 10,000 rows.

Example:

index,target
0,1.0
1,0.2
2,0.1

Note:
-----
The focus of this part of the test is to create a working predictive model which will be deployed in PART 2 of the test. You should not spend too much time fine-tuning the model performance as the goal is to have a saved model ready to be deployed.


PART 2 - Deploy Model
---------------------

Create a Jupyter notebook to deploy the model you created in PART 1 on Seldon Core and get predictions back from it.

You can find extensive documentation at https://github.com/SeldonIO/seldon-core

Your notebook should run within a local Minikube Kubernetes Cluster.

Evaluation Metric: A working notebook our team can run through successfully.

Summary
-------

You should email us
  - A csv file with test predictions
  - A Jupyter notebook with model deployment steps
