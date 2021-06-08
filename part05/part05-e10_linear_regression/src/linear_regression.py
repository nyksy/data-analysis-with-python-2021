#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)

    return float(model.coef_[0]), model.intercept_


def main():

    x = np.linspace(0, 5, 10)
    y = np.linspace(0, 5, 10) + 1*np.random.randn(10)

    params = fit_line(x, y)
    print('Slope:', params[0])
    print('Intercept:', params[1])

    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)

    xfit = np.linspace(0, 5, 100)
    yfit = model.predict(xfit[:, np.newaxis])

    plt.plot(xfit, yfit, color='black')
    plt.plot(x, y, 'o')

    plt.title('Linear Regression')
    plt.show()


if __name__ == "__main__":
    main()
