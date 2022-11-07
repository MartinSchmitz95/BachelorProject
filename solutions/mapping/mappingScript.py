
mappingDict = {}

with open("./solutions/mapping/ali.sam", "r") as handler, open("./solutions/mapping/output.txt", "w") as output:
	i = 0
	start = ["@HD", "@SQ", "@RG", "@PG", "@CO"]
	
	for read in handler:
		currentRead = read.split('\t')
			
		if currentRead[0] not in start:
			if currentRead[2] != "*":
				if currentRead[0] in mappingDict:
					mappingDict[currentRead[0]][0] += 1
					mappingDict[currentRead[0]][1].append(int(currentRead[3]))
					mappingDict[currentRead[0]][2].append(int(currentRead[4]))
				else:
					mappingDict[currentRead[0]] =  [1, [int(currentRead[3])], [int(currentRead[4])]]
			
	for key in mappingDict:
		startPositions = ""
		for i in range(mappingDict[key][0]):
			if i != 0:
				startPositions += ", "
			startPositions += str(mappingDict[key][1][i])
		
		sumQuality = 0
		for i in range(mappingDict[key][0]):
			sumQuality += mappingDict[key][2][i]

		line = key + "\t" + str(mappingDict[key][0]) + "\t" + startPositions + "\t" + str(sumQuality/ mappingDict[key][0]) + "\n"
		
		output.write(line)
		


