# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np

def compute_cost_MSE(y, tx, beta):
    """compute the loss by mse."""
    
    e = y - tx.dot(beta)
    mse = e.dot(e) / (2 * len(e))
    return mse

def compute_cost_MAE(y, tx, w):
    y = np.array(y)
    return np.sum(abs(y - np.dot(tx, w))) / y.shape[0]
    
def least_square_mse(y, tx, w):
    return compute_cost_MSE(y, tx, w)

def rmse(y, tx, w):
    return np.sqrt(compute_cost_MSE)

def least_squares(y, tx):
    """calculate the least squares solution."""
    a = tx.T.dot(tx)
    b = tx.T.dot(y)
    return np.linalg.solve(a, b)