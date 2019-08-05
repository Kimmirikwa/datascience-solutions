import csv

def clean_data(row):
	'''
		cleans the data by removing the first and the last characters in some properties of the row
	'''
	row['Network'] = row.get('Network')[1:-1]
	row['Product'] = row.get('Product')[1:-1]
	row['Date'] = row.get('Date')[1:-1]

	return row

with open('data/input.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	for row in csv_reader:
		row = clean_data(row)
