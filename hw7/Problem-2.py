#Problem 2
import csv
with open('roster.csv' , 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row , type(row))

#Mr. Gold I know i have to separate the list and then i hve to sort it by the date and gpa.
#I understand what I have to do in the problems but i cant manage to get them to work.

