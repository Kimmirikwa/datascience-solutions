import csv

with open('data/input.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)