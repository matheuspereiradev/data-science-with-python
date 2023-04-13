import numpy as np

km = np.loadtxt("files/carros-km.txt")
anos = np.loadtxt("files/carros-anos.txt", dtype=int)

km_media = km / (2019 - anos)

print(km_media)