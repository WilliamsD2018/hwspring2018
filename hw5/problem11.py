temperature = float(raw_input('Please input your body temperature: '))

if(temperature <= 96.0):
	print ('Please reply with "Yes" or "No"')
	no1 = raw_input("Aren't you cold? ")
	if(no1 == 'No'):
		print ('Hmph. You must be cold blooded.')
	if(no1 == 'Yes'):
		print ('Try dressing up for the winter to keep warm. ')
if(temperature == 98.6):
	print ("You are a healthy individual. I suggest that you find some friends to hang out with. You never know when you'll drop dead...")
if(temperature >= 99.0):
	print ('Please reply with "Yes" or "No"')
	no2 = raw_input("Aren't you feeling a bit warm? ")
	if(no2 == 'Yes'):
		print ('You may be running a fever.')
	if(no2 == 'No'):
		print ('Hmph. You must be hot-blooded.')
