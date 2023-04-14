import numpy

data = numpy.array([[44410., 5712., 37123., 0., 25757.], [2003., 1991., 1990., 2019., 2006.]])
print("array")
print(data)

print("shape")
print(data.shape)  # (2, 5) two lines five columns
print("ndim")
print(data.ndim)  # dimension number
print("size")
print(data.size)  # total quantity of elements
print("dtype")
print(data.dtype)  # type
print("T")
print(data.T)  # invert lines and columns (is equals to use dados.tranpose())

# METHODS

print("tolist")
print(data.tolist())  # convert array numpy to python list

contador = numpy.arange(10)
print("reshape before")
print(contador)
print("reshape C after")
print(contador.reshape((5, 2), order="C"))
print("reshape F after")
print(contador.reshape((5, 2), order="F"))

