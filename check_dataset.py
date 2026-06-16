import pandas as pd

df = pd.read_csv(
    "data/training.1600000.processed.noemoticon.csv",
    encoding="latin-1",
    header=None
)

df = df[[0, 5]]
df.columns = ["sentiment", "text"]

df["sentiment"] = df["sentiment"].replace({4: 1})

print(df["sentiment"].value_counts())