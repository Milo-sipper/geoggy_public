import pandas as pd
import numpy as np
from statsmodels.multivariate.manova import MANOVA
from contextlib import closing



data = {
    "Area": [1]*8 + [2]*8 + [3]*8 + [4]*8,
    "Temperature": [closing(open("temperature.txt")).read().splitlines()],
    "Windspeed": [closing(open("windspeed.txt")).read().splitlines()],
    "Albedo": [closing(open("albedo.txt")).read().splitlines()],
    "Relative_Humidity": [closing(open("humidity.txt")).read().splitlines()]
}

df = pd.DataFrame(data)
print(df)


maov = MANOVA.from_formula("Temperature + Relative_Humidity + Albedo + Windspeed ~ Area", data=df)
results = MANOVA.mv_test(maov)
print(results)
