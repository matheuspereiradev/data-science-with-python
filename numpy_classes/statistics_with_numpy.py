import numpy as np

km = np.loadtxt("../files/carros-km.txt", dtype=int)
years = np.loadtxt("../files/carros-anos.txt")
price = np.loadtxt("../files/carros-valor.txt")

dataset = np.column_stack((years, km, price))
print(dataset.shape)

# this way will return the arithmetic average for all numbers
print("All")
print(np.mean(dataset))

print("By axis")
# this way will return the arithmetic average for lines
print(np.mean(dataset, axis=0))

# this way will return the arithmetic average using all lines and only the column 1
print("By column")
print(np.mean(dataset[:, 1], axis=0))


# this way will return the standar deviation using all lines and only the column 1
print("standar deviation")
print(np.std(dataset[:, 2], axis=0))

# this way will return the sum using all lines
print("sum")
print(dataset.sum(axis=0))
print(np.sum(dataset, axis=0))

