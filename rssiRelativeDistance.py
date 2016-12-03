def calcDistance(txPower,rsuToLane,r1, r2):
	'''
	Calculate the distance between r1 and r2 when they are on the same lane going to the same direction.
	@param r1, r2: rssi of both access points
	d = 10 ^ ((TxPower - RSSI) / (10 * 2))
	'''
	d1 = 10**((txPower-r1)/(10*2))
	d2 = 10**((txPower-r2)/(10*2))
	if d1<rsuToLane or d2<rsuToLane:
		return -1
	return abs((d1**2- rsuToLane**2)**0.5-(d2**2- rsuToLane**2)**0.5)