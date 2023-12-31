# random forest for feature importance on a regression problem
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot
import pandas as pd

# define dataset

dataset = pd.read_csv(r'../../Data/output_lecture_seminar_processed.csv', parse_dates=['date'])

#X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1)
feature_cols = ['week', 'day', 'time_of_day', 'class_type', 'faculty', 'school', 'joint', 'status', 'degree', 'enrollment', 'class_duration']
X = dataset[feature_cols]
y = dataset['normalized_attendance2']

# define the model
model = RandomForestRegressor()
# fit the model
model.fit(X, y)
# get importance
importance = model.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
 print('Feature: %0d, Score: %.5f' % (i,v))
for feature, score in zip(feature_cols, importance):
    print(feature, score)
# plot feature importance
pyplot.bar([x for x in range(len(importance))], importance)
pyplot.show()