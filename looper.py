import serial
import os

ser = serial.Serial('/dev/tty.usbserial-A501IFHH', 9600, timeout=1)

while 1:

	command = ser.readline().rstrip()
	if command:
		print command

	if command == 'play':
		os.system('osascript play.scpt')

	elif command == 'next':
		os.system('osascript next.scpt')

	elif command == 'previous':
		os.system('osascript previous.scpt')

	elif command == 'vup':
		os.system('osascript vup.scpt')

	elif command == 'vdown':
		os.system('osascript vdown.scpt')

