import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/dohk/Dropbox/Developer/dataset/practice/data/body.csv')

print(df, end="\n\n")

# df['height'].plot(kind='kde')
# df['height'].plot(kind='kde', bw_method=0.1)
df['height'].plot(kind='kde', bw_method=2)
plt.show()