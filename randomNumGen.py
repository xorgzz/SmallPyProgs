import sys
import random as rd

def getNum():
	rd.seed()
	return rd.randrange(0, 10)

if len(sys.argv) != 2:
	print("\tadd amount of wanted nummbers !!")
	exit()

for i in range(int(sys.argv[1])):
	print(getNum(), end="  ")

print()