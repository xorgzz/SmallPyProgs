string = input("tekst: ")
start = int(input("początkowa linijka: "))
start -= 1
maxim = int(input("liczba linijek: "))
updown = True
mainArray = list()


def makeStr(arr):
	fin = str()
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			fin += str(arr[i][j])

	return fin

for i in range(maxim):
	mainArray.append(list())

for i in range(len(string)):
	mainArray[start].append(string[i])
	if(start == 0 and updown == True):
		updown = False
		start += 1
	elif(start == maxim-1 and updown == False):
		updown = True
		start -= 1
	elif(updown == True):
		start-=1
	else:
		start+=1

print(makeStr(mainArray))