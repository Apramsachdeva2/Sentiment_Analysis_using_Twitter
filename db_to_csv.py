# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 06:50:30 2019

@author: Apram Sachdeva
"""
import dataset
db = dataset.connect(settings.connection_URL)
result = db[settings.table_name].all()
dataset.freeze(result, format='csv', filename=settings.csv_file)
