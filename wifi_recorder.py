# pip install access_points
# Use > *.txt to dump stdout to a file
from access_points import get_scanner
import time
clientName = 1
wifi_scanner = get_scanner()
while True:
	wifiList = wifi_scanner.get_access_points()
	for wifi in wifiList:
		wifi['time'] = time.clock()
		wifi['client']=clientName
	print wifiList
	time.sleep(1)