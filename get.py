'''
Fetches all the videos in a youtube playlist.

usage: python get.py PLAYLIST_ID

Retrieves the best quality version available into the working dir.

Thomas Parks
20/08/2014
'''

import urllib
import sys
from bs4 import BeautifulSoup as BS
import subprocess

playlisturl = sys.argv[1]

#The Google youtube api, returns a large text file with all the playlist info
playlistapi = 'http://gdata.youtube.com/feeds/api/playlists/{0}'
rawplaylist = urllib.urlopen(playlistapi.format(playlisturl))

#Turns the file into a bs4 tree
playlist = BS(rawplaylist)

#media:player tags contain links to the real videos.
links = [link.get('url') for link in playlist.find_all('media:player')]

for link in links:
    subprocess.call(['quvi', 'get', '-s best', link])
