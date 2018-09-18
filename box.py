#!/usr/bin/env python
from mpd import MPDClient
#from readtest import *
import re
from CardList import CardList
from Reader import Reader
import sys
<<<<<<< HEAD
=======
import os
import time
>>>>>>> 16077b7837a611ddccc5d5e187ff931b7ce497af


def connectMPD():
	try:
		client = MPDClient()               # create client object
		client.timeout = 200               # network timeout in seconds (floats allowed), default: None
		client.idletimeout = None
		print "Connecting..."
		client.connect("localhost", 6600)
		print "Connected!"
		return client
	except:
		print 'Could not connect to MPD server'

def playlist(client,plist):
	try:
		plist2 = re.sub('file:','',plist)
		print plist
		for root,dirs,files in os.walk(plist2):
			for filename in files:
				filename = plist + filename
				print filename
				client.add(filename)
		return plist
	except Exception as e:
		print(e)

def play(client, plist):
	try:
		client.stop()
		client.clear()
		if re.search('Card', plist):
			playlist(client,plist)
			client.shuffle()
<<<<<<< HEAD
		if re.search('playlist',plist):			
=======
		if re.search('spotify',plist):
>>>>>>> 16077b7837a611ddccc5d5e187ff931b7ce497af
			client.add(plist)
			print plist
		client.play()
	except:
		print 'Could not play playlist %s' % plist


reader = Reader()
cardList = CardList()
client = None
while not client:
	client = connectMPD()
	if not client:
		time.sleep(2)
play(client, "file:/kartenaenderung/startup/")
time.sleep(5)
client.clear()
client.close()
print 'Ready: place a card on top of the reader'
while True:
	try:
		card = reader.readCard()
		print 'Read card', card
		plist = cardList.getPlaylist(card)
		print 'Playlist', plist
		if plist != '':
			client = connectMPD()
			if plist=='pause':
				client.pause()
			else:
				play(client, plist)
			client.close()
	except KeyboardInterrupt:
		sys.exit(0)
	except:
		pass
