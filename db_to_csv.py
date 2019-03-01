# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 06:50:30 2019

@author: Apram Sachdeva
"""
import dataset
db = dataset.connect("sqlite:///tweets.db")
result = db["tweets"].all()
dataset.freeze(result, format='csv', filename="tweets.csv")