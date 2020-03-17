from sklearn.datasets import load_iris

# 1 - Import the data / 2 - data already cleaned
iris = load_iris()

# Capital X == input data
X = iris.data
# lowaer case y == targeted result
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

# 3 - Split data in Training Set/Test Set
# train_test_split == splits arrays in random train and test subsets
from sklearn.model_selection import train_test_split
# create train and test variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# 4 - Import a Model -> closest neigbor -> KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
# give the model the training data
knn.fit(X_train, y_train)

# 5 - Check the output
y_pred = knn.predict(X_test)

from sklearn import metrics
# compare the y_pred (predicted data) to the test data
print(metrics.accuracy_score(y_test, y_pred))

# 6 - Improve
# Using better algorithm
# Larget Datasets
# Better devision between train/ test data

from sklearn.tree import DecisionTreeClassifier
knn = DecisionTreeClassifier()
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred))

# create own sample
sample = [[3,5,4,2], [2,3,5,4]]
predictions = knn.predict(sample)
pred_spiecies = [iris.target_names[p] for p in predictions]
print("predictions: ", pred_spiecies)

# We don't have to run the ML model every time once it's accurate we can save it with joblib to save resources
from sklearn.externals import joblib
joblib.dump(knn, 'mlbrain.joblib')


model = joblib.load('mlbrain.joblib')
model.predict(X_test)
sample = [[3,5,4,2], [2,3,5,4]]
predictions = knn.predict(sample)
pred_spiecies = [iris.target_names[p] for p in predictions]
print("predictions: ", pred_spiecies)