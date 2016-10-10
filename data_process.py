import json
clients = ["ch","csw","czj"]
projNum = ["1.1","1.2","1.3","2.1"]
data = [[]*len(projNum)]
proj = projNum[0]
for client in clients:
	path = './wireless/'+client+'/'+proj+'.txt'
	print client
	with open(path) as f:
	    for line in f:
	    	# print line.replace("Zijian\'s","ZJ").replace("'",'"').replace("\\x","")
	    	line = line.replace("'s ","").replace("'",'"').replace("\\x","").replace("[]","").replace(" u","").strip()
	    	if line == '':
	    		continue
	    	# print line
	        data[0].append(json.loads(line))
	
# with open('./wireless/ch/1.1.txt') as f:
#     for line in f:
#     	print line.replace("'s ","").replace("'",'"').replace("\\x","")
#         # data.append(json.loads(line.replace("Zijian\'s","ZJ").replace("'",'"').replace("\\x","")))
# # print data