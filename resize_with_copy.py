import numpy

data = numpy.array([[44410., 5712., 37123., 0., 25757.], [2003., 1991., 1990., 2019., 2006.]])

print(data)

new_data = data.copy()

new_data.resize((3, 5), refcheck=False)
print(new_data)
new_data[2] = new_data[0] / (2019 - new_data[1])
print(new_data)