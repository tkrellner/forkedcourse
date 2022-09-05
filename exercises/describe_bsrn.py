import pandas as pd

bsrn = pd.read_csv('../data/BSRN_GOB_2019-10.csv')
print(bsrn.describe())