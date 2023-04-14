import numpy

km = [25000, 7500, 0, 8420]
year = [2021, 2015, 2022, 2000]

info_cars = km + year
print("===========")
data_num_array_c = numpy.array(info_cars).reshape((2,4))
print(data_num_array_c)
print("===========")
data_num_array_f = numpy.array(info_cars).reshape((4,2), order="F")
print(data_num_array_f)
