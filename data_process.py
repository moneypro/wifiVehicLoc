import json
import matplotlib.pyplot as plt
import numpy as np
clients = ["ch","csw","czj"]
projNum = ["1.1","1.2","1.3","2.1","2.2","2.3","3.1"]
phoneNames = {'iPhone':0,'csw iphone':1,'ZijianiPhone':2}
color = ['r','b','g']
labelName = ['A','B','C']

def dataToDist(data):
	dist=[]
	for i in range(3):
		dist.append([[],[],[]])
	for scanList in data[projIndex]:
		for wifiInfo in scanList:
			# print wifiInfo
			if 'client' not in wifiInfo.keys():	# ... There is a wireless printer interfering our scanning results
				continue
			client = int(wifiInfo['client'])
			distIndex = client - 1
			if wifiInfo['ssid'] in phoneNames:
				quality = int (wifiInfo['quality']) # czj has a different quality measure (Using OS X instead of Windows)
				if client == 3:
					quality = quality / 2
				dist[distIndex][phoneNames[wifiInfo['ssid']]].append(quality)
	return dist

def plotData(dist):
	marker = ''
	for i in range(3):
		for j in range(3):
			if i==j:
				continue
			x = np.linspace(0,100,num=len(dist[i][j]))
			label = labelName[i]+"-"+labelName[j]
			if marker == 'o':
				marker = '+'
			else:
				marker = 'o'
			plt.plot(x,dist[i][j],label = label,color=color[i+j-1],marker = marker,linewidth=2.0)
	plt.title(proj)
	plt.xlabel('Time')
	plt.ylabel('Wifi Quality')
	plt.legend()
	plt.show()

# def dataToCsv(projNum, dist):
# 	path = './'+proj+'.csv'
# 	myfile = open(..., 'wb')
# 	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# 	for i in 
# 	wr.writerow(mylist)

data = []
# proj = projNum[3]
for projIndex in range(len(projNum)):
	proj = projNum [projIndex]
	data.append([])
	for client in clients:
		if proj in projNum[4:] and client == 'czj':
			continue
		path = './'+client+'/'+proj+'.txt'
		# print client
		with open(path) as f:
		    for line in f:
		    	# print line.replace("Zijian\'s","ZJ").replace("'",'"').replace("\\x","")
		    	line = line.replace("'s ","").replace("'",'"').replace("\\x","").replace("[]","").replace(" u","").strip()
		    	if line == '':
		    		continue
		    	# print line
		        data[projIndex].append(json.loads(line))
	dist=dataToDist(data)
	plotData(proj,dist)

	
# with open('./wireless/ch/1.1.txt') as f:
#     for line in f:
#     	print line.replace("'s ","").replace("'",'"').replace("\\x","")
#         # data.append(json.loads(line.replace("Zijian\'s","ZJ").replace("'",'"').replace("\\x","")))
# # print data