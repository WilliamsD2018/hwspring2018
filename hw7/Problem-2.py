#Problem 2
import csv
with open('roster.csv' , 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		print row

