# file: example_simple_linear_regression_with_scikit.py
# function: Simple Linear Regression With scikit-learn
# documentation: https://realpython.com/linear-regression-in-python/

# There are five basic steps when you’re implementing linear regression:
#
# 1. Import the packages and classes you need.
# 2. Provide data to work with and eventually do appropriate transformations.
# 3. Create a regression model and fit it with existing data.
# 4. Check the results of model fitting to know whether the model is satisfactory.
# 5. Apply the model for predictions.

# Step 1: Import packages and classes
import numpy as np
from sklearn.linear_model import LinearRegression

# The fundamental data type of NumPy is the array type called numpy.ndarray.
# The rest of this article uses the term array to refer to instances of the
# type numpy.ndarray.
# The class sklearn.linear_model.LinearRegression will be used to perform
# linear and polynomial regression and make predictions accordingly.

# Step 2: Provide data
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])
# As you can see, x has two dimensions, and x.shape is (6, 1),
# while y has a single dimension, and y.shape is (6,).
print("x.shape:", x.shape , "y.shape:",y.shape )

# Step 3: Create a model and fit it
m = LinearRegression()
# This statement creates the variable model as the instance of LinearRegression.
# You can provide several optional parameters to LinearRegression:
#
# fit_intercept     is a Boolean (True by default) that decides whether to calculate
#                   the intercept 𝑏₀ (True) or consider it equal to zero (False).
# normalize         is a Boolean (False by default) that decides whether to normalize
#                   the input variables (True) or not (False).
# copy_X            is a Boolean (True by default) that decides whether to copy (True)
#                   or overwrite the input variables (False).
# n_jobs            is an integer or None (default) and represents the number of jobs
#                   used in parallel computation. None usually means one job and -1 to
#                    use all processors.
#
# This example uses the default values of all parameters.
#
# It’s time to start using the model. First, you need to call .fit() on model:
model = m.fit(x, y)

# Step 4: Get results
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
# coefficient of determination: 0.715875613747954

# When you’re applying .score(), the arguments are also the predictor x and regressor y, and the return value is 𝑅².
#
# The attributes of model are .intercept_, which represents the coefficient, 𝑏₀ and .coef_, which represents 𝑏₁:
print('intercept:', model.intercept_)
# intercept: 5.633333333333329
print('slope:', model.coef_)
# slope: [0.54]

# The code above illustrates how to get 𝑏₀ and 𝑏₁. 
# You can notice that .intercept_ is a scalar, while .coef_ is an array.

# The value 𝑏₀ = 5.63 (approximately) illustrates that your model predicts the response 5.63 when 𝑥 is zero.
# The value 𝑏₁ = 0.54 means that the predicted response rises by 0.54 when 𝑥 is increased by one.

# You should notice that you can provide y as a two-dimensional array as well.
# In this case, you’ll get a similar result. This is how it might look:
new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
print('intercept:', new_model.intercept_)
# intercept: [5.63333333]
print('slope:', new_model.coef_)
# slope: [[0.54]]
# As you can see, this example is very similar to the previous one, but in this case,
# .intercept_ is a one-dimensional array with the single element 𝑏₀, and .coef_ is a
# two-dimensional array with the single element 𝑏₁.

# Step 5: Predict response
# Once there is a satisfactory model, you can use it for predictions with either existing or new data.

# To obtain the predicted response, use .predict():
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')
# predicted response:
# [ 8.33333333 13.73333333 19.13333333 24.53333333 29.93333333 35.33333333]

# When applying .predict(), you pass the regressor as the argument and get the corresponding predicted response.
#
# This is a nearly identical way to predict the response:
y_pred = model.intercept_ + model.coef_ * x
print('predicted response:', y_pred, sep='\n')
# predicted response:
# [[ 8.33333333]
# [13.73333333]
# [19.13333333]
# [24.53333333]
# [29.93333333]
#  [35.33333333]]

# In this case, you multiply each element of x with model.coef_ and add model.intercept_ to the product.
#
# The output here differs from the previous example only in dimensions. The predicted response is now a two-dimensional array, while in the previous case, it had one dimension.
#
# If you reduce the number of dimensions of x to one, these two approaches will yield the same result. You can do this by replacing x with x.reshape(-1), x.flatten(), or x.ravel() when multiplying it with model.coef_.
#
# In practice, regression models are often applied for forecasts. This means that you can use fitted models to calculate the outputs based on some other, new inputs: