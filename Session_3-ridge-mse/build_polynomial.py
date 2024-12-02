# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    x = np.array(x)
    res = x
    for d in range(2, degree + 1):
        res = np.concatenate((res, x ** d), axis=-1)
    # print(len(x),degree)
    # print(res)
    res = np.reshape(res, (degree, len(x)))
    res = np.c_[np.ones((len(res.T), 1)),res.T]
    return res
