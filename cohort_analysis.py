#Importing the libraries for data manipulation, visualization and analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

import missingno as msn
from textwrap import wrap


# Load data

trans_data = pd.read_excel('transaction.xlsx')

print(trans_data.head())

# Visualize the fields with missing data
print(msn.bar(trans_data))