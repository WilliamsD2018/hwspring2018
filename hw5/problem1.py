
temperature = float(raw_input ("What is your current temperature? "))
if (temperature < 96.0):
	temperature = raw_input ('''Are you feeling cold?
This question you must answer with "yes" or "no" ''')
	if (temperature.lower() == "yes"):
		print ("Try dressing up for the winter to keep your temperature up.")
	elif (temperature.lower() == "no"):
		print ("hmph, you must be cold blooded.")
elif (temperature > 99.0):
	temperature = raw_input ('''Are you feeling hot?
This question you must answer with "yes or "no" ''')
	if (temperature.lower() == "yes"):
		print ("you might have a fever.")
	elif (temperature.lower() == "no"):
		print ("you must be warm blooded.")
elif (temperature == 98.5):
	print ("Congratulations, you are normal and healthy")
else:
	print ("close to normal, you may want to try again later.")
