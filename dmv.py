import requests
import time
import hashlib




def filename_timestamp():
	return time.strftime("%Y%m%d-%H%M%S")

def run_report():
	# set the URL to check
	url = 'https://vadmvappointments.as.me/schedule.php?action=showCalendar&fulldate=1&owner=19444409&template=monthly'

	# record the report start time
	timesuffix = filename_timestamp()

	# run our update requests

	# july
	r1 = requests.post(url, data = {

		'type': '15191541',
		'calendar': '4136541',
		'month': '2020-07-01',
		'skip': 'true',
		'options[numDays]': '5',
		'ignoreAppointment': '',
		'appointmentType': '',
		'calendarID': '4136541'

	})	

	# august
	r2 = requests.post(url, data = {

		'type': '15191541',
		'calendar': '4136541',
		'month': '2020-08-01',
		'skip': 'true',
		'options[numDays]': '5',
		'ignoreAppointment': '',
		'appointmentType': '',
		'calendarID': '4136541'

	})

	# september
	r3 = requests.post(url, data = {

		'type': '15191541',
		'calendar': '4136541',
		'month': '2020-09-01',
		'skip': 'true',
		'options[numDays]': '5',
		'ignoreAppointment': '',
		'appointmentType': '',
		'calendarID': '4136541'

	})	
	# october
	r4 = requests.post(url, data = {

		'type': '15191541',
		'calendar': '4136541',
		'month': '2020-10-01',
		'skip': 'true',
		'options[numDays]': '5',
		'ignoreAppointment': '',
		'appointmentType': '',
		'calendarID': '4136541'

	})

	# compute the hash
	hash_object = hashlib.md5(r1.text.encode() + r2.text.encode() + r3.text.encode() + r4.text.encode())
	myhash = hash_object.hexdigest()


	# log the response
	with open ("dmv-" + timesuffix + "-md5-" + myhash + "-july.txt", "w") as mytext:
		mytext.write(r1.text)

	with open ("dmv-" + timesuffix + "-md5-" + myhash + "-august.txt", "w") as mytext:
		mytext.write(r2.text)
	with open ("dmv-" + timesuffix + "-md5-" + myhash + "-september.txt", "w") as mytext:
		mytext.write(r3.text)
	with open ("dmv-" + timesuffix + "-md5-" + myhash + "-october.txt", "w") as mytext:
		mytext.write(r4.text)


	# generate a hash to return
		
	
	return myhash

if __name__ == '__main__':
	while True:
		print (run_report())
		time.sleep(10)





