import numpy

csv_data = numpy.loadtxt("data.csv", delimiter=",")
print(csv_data[0][0])
print(csv_data)
