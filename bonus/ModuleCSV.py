"""
module provides functionality for reading from and writing to CSV (Comma-Separated Values) files
"""
import csv

with open('../files/weather.csv', 'r') as file:
    data = list(csv.reader(file))

city = input("Enter city: ")

for row in data:
    if row[0] == city:
        print(row[1])