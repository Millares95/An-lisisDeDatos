import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import statsmodels as sm
pd.options.display.max_columns = 20 
pd.options.display.max_rows = 20 
pd.options.display.max_colwidth = 80 
np.set_printoptions(precision=4, suppress=True)

some_tuples = [(1,2,3), (5,6,7),(8,9,10)]

result= [x for tup in some_tuples for x in tup]
print(result)