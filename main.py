"""This code provides a really simple application of multilinear regression
   in a randomly generated dataset to help build intuition regarding overfitting
   and regularization techniques."""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline


def polynomial_regression(data, target, degree):
    """Perform polynomial regression with Ridge regularization."""

    polynomial_features = PolynomialFeatures(degree=degree)
    model = Ridge(alpha=ALPHA)
    pipeline = make_pipeline(polynomial_features, model)
    pipeline.fit(data, target)
    return pipeline


def create_data(num_data_points):
    """Generate data points for polynomial regression."""

    x = np.linspace(0, 2 * np.pi, num_data_points)
    y = np.sin(x) + np.random.normal(0, 0.2, num_data_points)

    x_range = np.linspace(0, 2 * np.pi, 1000)
    return x_range, x, y


def plot_results(x_range, y_range, y_train, x_train):
    """Plot the results of polynomial regression."""

    sine_wave = np.sin(x_range)

    plt.ylim(-1.5, 1.5)
    plt.plot(x_range, sine_wave, label='Sine Wave', color='blue')
    plt.plot(x_range, y_range, label='Polynomial Function', color='red', linestyle='dashed')
    plt.scatter(x_train, y_train, label='True', color='purple', marker='o', s=100)
    plt.legend()
    plt.show()


def perform_polynomial_regression():
    """Perform polynomial regression and plot the results."""

    x_range, x_train, y_train = create_data(DATAPOINTS)

    model = polynomial_regression(x_train.reshape(-1, 1), y_train, POLYNOMIAL_DEGREE)
    y_range = model.predict(x_range.reshape(-1, 1))

    plot_results(x_range, y_range, y_train, x_train)


# Configure number of data samples, degree of the polynomial function and regularization
DATAPOINTS = 10
POLYNOMIAL_DEGREE = 0
ALPHA = 0

# Run the experiment and plot results
perform_polynomial_regression()
