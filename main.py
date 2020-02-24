# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:48:47 2020

@author: Leslie
"""

# Import libraries
import numpy as np
import sklearn.decomposition

# Customer ID, Name_char1, Name_char2, Name_char3, Age, Salary
X = np.array([[1, 2, 15, 2, 30, 15000], [2, 20, 15, 13, 24, 12000], [3, 1, 14, 14, 44, 23000]])

# Function to encrypt numerical data set
def sencrypt(X):
    mu = np.mean(X, axis=0)
    pca = sklearn.decomposition.PCA()
    pca.fit(X)
    encrypted_X = pca.transform(X)
    key = pca.components_
    return encrypted_X, key, mu

# Function to decrypt data set
def sdecrypt(encrypted_X, key, mu, nc):
    decrypted_X = np.dot(encrypted_X[:,:nc], key[:nc,:])
    decrypted_X += mu
    return decrypted_X