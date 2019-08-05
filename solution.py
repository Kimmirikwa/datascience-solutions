import csv

def clean_data(row):
	'''
		cleans the data by removing the first and the last characters in some properties of the row,
		which are single quotes i.e "'"
	'''
	row['Network'] = row.get('Network')[1:-1]
	row['Product'] = row.get('Product')[1:-1]
	row['Date'] = row.get('Date')[1:-1]

	return row

def get_month(date):
	return date[3:]

def get_agg_key(row):
	'''
		Gets the key of a group to be aggregated.
		Since we group by Network, Product and Month, we construct the key from these values
		This key will be used in a dictionary to identify a group uniquely
		We extract the month information from the date
		params:
			- row: the cleaned row data
		returns:
			- network, product and month e.g "Network 1,Loan Product 1,Mar-2016"
	'''
	network = row.get('Network')
	product = row.get('Product')
	month = get_month(row.get('Date'))

	return ','.join([network, product, month])

aggregate_data = {}
with open('data/input.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	for row in csv_reader:
		row = clean_data(row)
		amount = float(row.get('Amount'))
		agg_key = get_agg_key(row)

		aggregate_data.setdefault(agg_key, {'Total loan': 0, 'Loans count': 0})
        aggregate_data[agg_key]['Total loan'] += amount
        aggregate_data[agg_key]['Loans count'] += 1
        aggregate_data[agg_key]['Average loan'] = aggregate_data[agg_key]['Total loan'] / aggregate_data[agg_key]['Loans count']
