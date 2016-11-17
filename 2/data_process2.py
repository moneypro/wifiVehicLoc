
import json
import matplotlib.pyplot as plt
import numpy as np
clients = ["ch","csw","czj"]
projNum = ["1.1","1.2","1.3","2.1","4.1","4.1.2","4.2","5.1","5.1.2","5.1.3","5.1.4"]
phoneNames = {'cc1':0,'cc2':1,'cc3':2}
color = ['r','b','g']
labelName = ['A','B','C']
data = []
# proj = projNum[3]
for projIndex in range(len(projNum)):
	proj = projNum [projIndex]
	data.append([])
	for client in clients:
		if proj in projNum[4:] and client == 'czj':
			continue
		path = './2/'+client+'/'+proj+'.txt'
		# print client
		with open(path) as f:
		    for line in f:
		    	# print line.replace("Zijian\'s","ZJ").replace("'",'"').replace("\\x","")
		    	line = line.replace("'s ","").replace("'",'"').replace("\\x","").replace("[]","").strip()
		    	if client == 'czj':
		    		line = ''.join([i if ord(i) < 128 else ' ' for i in line])
		    		line = line.replace("), AccessPoint(","'},{'").replace("AccessPoint(","{'").replace("=","':'").replace(", ","', '").replace(")]","'}]").replace("'",'"')
		    	if line == '':
		    		continue
		    	print line
		        data[projIndex].append(json.loads(line))
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
			wifiName = wifiInfo['ssid'].lower()
			if wifiName in phoneNames:
				quality = int (wifiInfo['quality']) # czj has a different quality measure (Using OS X instead of Windows)
				# if client == 3:
				# 	quality = quality / 2
				distance = 10**(((-50-(quality/2)+100))/20)
				dist[distIndex][phoneNames[wifiName]].append(distance)
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
	plt.ylabel('Distance')
	plt.legend()
	plt.show()

	
# with open('./wireless/ch/1.1.txt') as f:
#     for line in f:
#     	print line.replace("'s ","").replace("'",'"').replace("\\x","")
#         # data.append(json.loads(line.replace("Zijian\'s","ZJ").replace("'",'"').replace("\\x","")))
# # print data