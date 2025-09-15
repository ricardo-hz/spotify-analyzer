import pandas as pd

df = pd.read_json("./spotify-account-data/StreamingHistory_music_0.json")
print("---HEAD---")
print(df.head())
print("---TAIL---")
print(df.tail())
print()
print()

df2 = pd.read_json("./spotify-account-data/StreamingHistory_music_1.json")
print("---HEAD---")
print(df2.head())
print("---TAIL---")
print(df2.tail())
print()
print()

df3 = pd.concat([df, df2])
print("---HEAD---")
print(df3.head())
print("---TAIL---")
print(df3.tail())