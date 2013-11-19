import serial
import os
import subprocess

ser = serial.Serial('/dev/tty.usbserial-A501IFHH', 9600)

play_pause = '''
property lastPaused : "%s"
tell application "iTunes" to set itunesState to (player state as text)
tell application "MPlayerX" to set mplayerxState to ((playstatus) as text)

if itunesState is equal to "playing" then
	tell application "iTunes" to playpause
	set lastPaused to "iTunes"
else if ((itunesState is equal to "paused") and (lastPaused is equal to "iTunes")) then
	tell application "iTunes" to playpause
else if mplayerxState is equal to "Playing" then
	tell application "MPlayerX" to playpause
	set lastPaused to "MPlayerX"
else if ((mplayerxState is equal to "Paused") and (lastPaused is equal to "MPlayerX")) then
	tell application "MPlayerX" to playpause
end if
'''

next = '''
tell application "iTunes" to set itunesState to (player state as text)
tell application "MPlayerX" to set mplayerxState to ((playstatus) as text)
if itunesState is equal to "playing" then
	tell application "iTunes" to next track
else if mplayerxState is equal to "Playing" then
	tell application "MPlayerX" to goto next episode
end if
'''

previous = '''
tell application "iTunes" to set itunesState to (player state as text)
tell application "MPlayerX" to set mplayerxState to ((playstatus) as text)
if itunesState is equal to "playing" then
	tell application "iTunes" to previous track
else if mplayerxState is equal to "Playing" then
	tell application "MPlayerX" to goto previous episode
end if
'''

toggle_fullscreen = '''
activate application "MPlayerX"
tell application "System Events"
keystroke "f"
end tell
'''

toggle_subtitle = '''
activate application "MPlayerX"
tell application "System Events"
keystroke "s"
end tell
'''

lastPaused = ""

while 1:

	command = ser.readline().rstrip()
	if command:
		print command

	if command == 'play':
		cmd = "osascript -e '%s'" % (play_pause % lastPaused)
		lastPaused = os.popen(cmd).read().rstrip()

	elif command == 'next':
		os.system("osascript -e '%s'" % next)

	elif command == 'previous':
		os.system("osascript -e '%s'" % previous)

	elif command == 'vup':
		os.system('osascript vup.scpt')

	elif command == 'vdown':
		os.system('osascript vdown.scpt')

	elif command == 'fullscreen':
		os.system("osascript -e '%s'" % toggle_fullscreen)
		
	elif command == 'subtitle':
		os.system("osascript -e '%s'" % toggle_subtitle)

