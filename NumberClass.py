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
			

		return arrCorrectFormat


	def genBlock(self, arr, puzzle):
		arr1 = arr[0:9]
		arr2 = arr[9:18]
		arr3 = arr[18:27]

		while self.checkRows(arr1, arr2) == False:
			arr2 = self.genRows(puzzle[9:18])


		# while self.checkRows(arr2, arr3) == False or self.checkRows(arr1, arr3) == False:
		# 	arr3 = self.genRows(puzzle[18:27])


		mergedArr = arr1 + arr2  
		return mergedArr



	def checkRows(self, row1, row2):
		for i in range(0, 3):
			for j in range(0, 3):
				if row1[i]  == row2[j]:
					return False

		for i in range(3, 6):
			for j in range(3, 6):
				if row1[i]  == row2[j]:
					return False

		
		for i in range(6, 9):
			for j in range(6, 9):
				if row1[i]  == row2[j]:
					return False


		return True



