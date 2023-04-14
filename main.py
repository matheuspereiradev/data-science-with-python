import numpy as np
from numpy import arange

km = np.loadtxt(fname="files/carros-km.txt", dtype=int)
anos = np.loadtxt("files/carros-anos.txt", dtype=int)

km_media = km / (2019 - anos)

print(km_media)

print(arange(10))
#traz as linhas da dimenção
print(km.shape)

km_media_dimensional = np.array([km, anos])

km_media_in_multidimension = km_media_dimensional[0] / (2019 - km_media_dimensional[1])
