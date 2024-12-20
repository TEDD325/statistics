import pandas as pd
print(pd.__version__)

data_path = '/Users/dohk/Dropbox/Developer/dataset/practice/data/test.csv'

df = pd.read_csv(data_path)

print(df, end="\n\n")
print(df.columns, end="\n\n")
print(df.info(), end="\n\n")
print(df.head(), end="\n\n")
print(df.describe(), end="\n\n")
print(df.describe(include='all'), end="\n\n")
print(df.describe(include='object'), end="\n\n")
print(df.describe(include='number'), end="\n\n")
print(df.describe(include='all', percentiles=[0.25, 0.5, 0.75]), end="\n\n")
print(df.describe(include='all', percentiles=[0.25, 0.5, 0.75, 0.95]), end="\n\n")
print(df.describe(include='all', percentiles=[0.25, 0.5, 0.75, 0.95, 0.99]), end="\n\n")
print(df.describe(include='all', percentiles=[0.25, 0.5, 0.75, 0.95, 0.99, 1]), end="\n\n")
