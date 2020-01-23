# Auto Desktop Background Updater V1.0
# Code by Darryl Polo (https://darrylpolo.tech)
# Will grab a random 4K desktop wallpaper from https://www.ultrahdwallpaper.art every X seconds.
# Change timeloop variable in seconds to change time in between refreshes
# Enjoy!

import requests
import os
import struct
import ctypes
import time

import time
timeloop = 3600.0
starttime=time.time()

download_path = os.path.join(os.path.expandvars("%userprofile%"),"Downloads", "UltraHDWallpaper.ART")
if not os.path.exists(download_path):
	os.makedirs(download_path)
	
while True:
	
	url = 'https://ultrahdwallpaper.art/random_download.php'
	myfile = requests.get(url)
	
	
	open(download_path + '\CurrentDesktopBG.png', 'wb').write(myfile.content)
	PATH = download_path + '\CurrentDesktopBG.png'

	SPI_SETDESKWALLPAPER = 20

	print(PATH)

	def is_64bit_windows():
		"""Check if 64 bit Windows OS"""
		return struct.calcsize('P') * 8 == 64

	def changeBG(path):
		"""Change background depending on bit size"""
		if is_64bit_windows():
			ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
		else:
			ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)

	changeBG(PATH)
	print('Updating Background')
	time.sleep(timeloop - ((time.time() - starttime) % timeloop))
	os.remove(download_path + '\CurrentDesktopBG.png')
