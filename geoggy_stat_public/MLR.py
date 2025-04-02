from statsmodels.compat import lzip
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd 

data = {
    "Area": [1]*8 + [2]*8 + [3]*8 + [4]*8,
    "Temperature": [
    33.7, 33.7, 32.5, 32.0, 32.4, 34.7, 34.8, 35.5,
    31.0, 30.4, 31.8, 29.1, 31.2, 32.0, 31.6, 31.1,
    32.1, 32.0, 32.0, 30.5, 31.4, 31.4, 30.9, 31.3,
    35.1, 34.2, 33.8, 34.0, 33.7, 33.8, 34.0, 33.7],

    "Windspeed": [
    2.2, 0.8, 2.6, 1.9, 0.2, 0.3, 0.4, 1.2,
    1.3, 1.6, 1.2, 0.6, 3.0, 3.0, 2.5, 1.4,
    0.7, 1.5, 0.8, 0.7, 0.6, 0.9, 2.8, 1.2,
    0.8, 0.4, 0.7, 1.6, 1.2, 0.9, 0.5, 1.0],

    "Albedo":[ 0.482, 0.437, 0.385, 0.426, 0.379, 0.452, 0.450, 0.436,
    0.488, 0.469, 0.449, 0.432, 0.387, 0.453, 0.487, 0.446,
    0.399, 0.357, 0.412, 0.426, 0.412, 0.413, 0.394, 0.450,
    0.494, 0.476, 0.482, 0.479, 0.521, 0.438, 0.320, 0.433],

    "Relative_Humidity":[ 62.0, 57.3, 58.4, 55.3, 55.4, 50.6, 47.3, 46.6,
    59.8, 59.0, 60.0, 63.7, 59.8, 60.2, 56.5, 60.2,
    58.7, 59.2, 57.6, 57.8, 60.0, 59.3, 60.9, 58.2,
    53.5, 54.0, 58.0, 54.6, 57.2, 58.2, 57.5, 58.0],
}


df = pd.DataFrame(data)
X = df[['Albedo', 'Relative_Humidity', 'Windspeed']]  # Independent variables
X = df[['Albedo']]
y = df['Temperature'] 

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

df['Albedo_squared'] = df['Albedo'] ** 2
model = sm.OLS(df['Temperature'], sm.add_constant(df[['Albedo', 'Albedo_squared', 'Relative_Humidity', 'Windspeed']])).fit()
print(model.summary())