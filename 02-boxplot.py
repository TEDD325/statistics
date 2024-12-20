import pandas as pd
import matplotlib.pyplot as plt

print(pd.__version__)

data_path = '/Users/dohk/Dropbox/Developer/dataset/practice/data/test_school.csv'

try:
    df = pd.read_csv(data_path)
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df['english_score'].describe())
    df['english_score'].plot(kind='box')
    plt.title('Box Plot of English Scores')
    plt.xlabel('Scores')
    plt.ylabel('Frequency')
    plt.show()
except FileNotFoundError:
    print(f"File not found at {data_path}")
except pd.errors.EmptyDataError:
    print(f"No data in file at {data_path}")
except pd.errors.ParserError:
    print(f"Error parsing file at {data_path}")

q1 = df['english_score'].quantile(0.25)
q3 = df['english_score'].quantile(0.75)
iqr = q3 - q1
print(f'Normal range: {q1 - 1.5 * iqr}~{q3 + 1.5 * iqr}')

df.plot(kind='box', subplots=True, layout=(2, 3), figsize=(10, 6))
plt.title('Box Plots of All Columns')
plt.tight_layout()
plt.show()