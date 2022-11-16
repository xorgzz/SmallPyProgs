import random as rd

bucketAmount = 16

def topBot(array):
	tmpT = 0
	tmpB = 0
	for i in range(len(array)):
		if(tmpT < array[i]):
			tmpT = array[i]
		if(tmpB > array[i]):
			tmpB = array[i]

	return tmpT, tmpB

def bucketSort(array):
	preout = list()
	out = list()

	# tworzenie kubełków
	for i in range(bucketAmount):
		preout.append([])

	# wybieranie najmniejszej i największej liczby w tablicy
	topNum, botNum = topBot(array)

	step = topNum / bucketAmount

	# dzielenie elementów na kubełki
	for i in range(len(array)):
		for j in range(1, bucketAmount+1):
			if(array[i] <= botNum+(step*j)):
				preout[j-1].append(array[i])
				break

	# sortowanie każdego kubełka
	for i in range(bucketAmount):
		preout[i].sort()

	#składanie kubełków w jedną tablicę
	for i in range(bucketAmount):
		for j in range(len(preout[i])):
			out.append(preout[i][j])

	return out

array = list()

# manualne wprowadzenie liczb
# nums = input("numms: ")
# array = nums.split()

# generowanie randomowych liczb
for i in range(512):
	array.append(rd.uniform(0,10))


end = bucketSort(array)

print("ID\tbefore:\t\t\tafter:")
for i in range(len(array)):
	array[i] = float(array[i])
	print(f"{i}.\t{array[i]}", end="")
	if len(str(array[i])) < 16:
		print("\t", end="")
	print(f"\t{end[i]}")
