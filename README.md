# Polynomial-Regression Overfitting-concept

<a name="readme-top"></a>

### About
This code is designed to demonstrate underfitting and overfitting, by training a polynomial regression model on a synthetic dataset. There are three parameters meant to be configured in order to showcase the performance of the model, under different conditions:
* Number of samples used to train model
* Model complexity
* Regularization
<p align="center">
  <img src="images/demo.gif" alt="Demo" style="width:50%;">
</p>

### Prerequisites

To set up and use this code, ensure that you have the required dependencies installed. You can easily install them by running the following command:
pip install -r requirements.txt

### Usage
* Open the code file and configure the following parameters to experiment with different conditions:

  -DATAPOINTS: The number of samples used to train the model.
  
  -POLYNOMIAL_DEGREE: The complexity of the polynomial function.
  
  -ALPHA: The regularization parameter.
  
  Run the code to perform the polynomial regression experiment and visualize the results.

* The code will generate synthetic data, perform polynomial regression with Ridge regularization, and plot the results to help you gain insights into the concepts of underfitting and overfitting. You can adjust    the parameters to see how different configurations impact the model's performance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
