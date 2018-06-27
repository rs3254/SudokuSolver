from random import randint

class NumberClass:
	
	def genRows(self, arr):
		arrCorrectFormat = list(map(int, arr))
		for i in range(0, len(arrCorrectFormat)):
			x = randint(1, 9)
			if arrCorrectFormat[i] != 0:
				continue
			elif arrCorrectFormat[i] == 0:
				while x in arrCorrectFormat:
					x = randint(1, 9)
				arrCorrectFormat[i] = x
			

		print(arrCorrectFormat)


