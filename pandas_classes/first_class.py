import pandas as pd

dataset = pd.read_csv("../files/db.csv", sep=";")
print("DATATYPES")
print(dataset.dtypes)
print("DESCIBE")
print(dataset[["Quilometragem", "Valor"]].describe())
print("INFO")
print(dataset.info())

