import pandas as pd

# the index_col was choose the index column and remove incremental index
dataset = pd.read_csv("../files/db.csv", sep=";", index_col=0)
print(dataset)

print("------------------------------")

dt = {'Crossfox': {'km': 35000, 'ano': 2005, 'km_media': 2500.0},
      'DS5': {'km': 17000, 'ano': 2015, 'km_media': 4250.0},
      'Fusca': {'km': 130000, 'ano': 1979, 'km_media': 3250.0},
      'Jetta': {'km': 56000, 'ano': 2011, 'km_media': 7000.0},
      'Passat': {'km': 62000, 'ano': 1999, 'km_media': 3100.0}}

print(pd.DataFrame(dt).T)
