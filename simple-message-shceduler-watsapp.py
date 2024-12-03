#This code sends message to friend on scheduled time

import pywhatkit as kit
import datetime

now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1
phone_number = '+123456789'
message = 'Hello! This is a scheduled message.'

kit.sendwhatmsg(phone_number, message, hour, minute)