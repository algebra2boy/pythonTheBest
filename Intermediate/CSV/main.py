# Many ways to read csv
# 1. read the data with "with open"
with open("weather_data.csv", "r") as data_file:
    data = data_file.readlines()
    print(data)

#2 by using the csv library

import csv
with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        # print(row)
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data['temp'])
temp_list = data['temp'].to_list()
print(temp_list)

# the average temperature
print(data['temp'].mean())

# the max temperature
print(data['temp'].max())

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])