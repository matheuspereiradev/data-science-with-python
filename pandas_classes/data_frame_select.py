import pandas as pd

dataset = pd.read_csv("../files/db.csv", sep=";", index_col=0)

print("HEAD")
print(dataset.head())
print("==========================================================")

print("show one column as Series")
print(dataset["Valor"])
print("==========================================================")

print("show one column as Dataframe")
print(dataset[["Valor"]])
print("==========================================================")

print("slice the dataset")
print(dataset[0:3])
print("==========================================================")

print("find the info by Key Series")
print(dataset.loc["Crossfox"])
print("==========================================================")

print("find the info by Key dataframe")
print(dataset.loc[["Crossfox", "Phantom 2013"]])
print("==========================================================")

print("find the info by Key dataframe only columns")
print(dataset.loc[["Crossfox", "Phantom 2013"], ["Motor", "Valor"]])
print("==========================================================")

print("find the info only selected columns")
print(dataset.loc[:, ["Motor", "Valor"]])
print("==========================================================")

print("find the info by index find 1 as series")
print(dataset.iloc[1])
print("==========================================================")

print("find the info by index find 1 as dataframe")
print(dataset.iloc[[1]])

print("find the info by index interval")
print(dataset.iloc[1:4])
print("==========================================================")

print("find the info by index interval with specific columns")
print(dataset.iloc[1:4, [0, 4, 2]])
print("==========================================================")

print("find the all info with specific columns")
print(dataset.iloc[:, [0, 4, 2]])
print("==========================================================")
