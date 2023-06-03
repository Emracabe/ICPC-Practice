""" 
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
	- s = '12:01:00PM'
	Return '12:01:00'.

	- s = '12:01:00AM'
	Return '00:01:00'.
"""

def timeConversion(s):
	hour, minute, second = map(int, oras[:-2].split(":"))
	ampm = s[-2:]

	if ampm == "PM" and hour != 12:
		hour += 12
	elif ampm == "AM" and hour == 12:
		hour = 0

	return "{:02d}:{:02d}:{:02d}".format(hour, minute, second)


s = input()
print(timeConversion(s))
