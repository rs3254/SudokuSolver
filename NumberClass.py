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
			arr1 = self.genRows(puzzle[0:9])

		arr3 = self.genThirdRow(arr1, arr2, arr3)

		mergedArr = arr1 + arr2  + arr3
		return mergedArr




	def genThirdRow(self, arr1, arr2, puzzle):
		forbiddenNums1 = arr1[0:3] + arr2[0:3]
		forbiddenNums2 = arr1[3:6] + arr2[3:6]
		forbiddenNums3 = arr1[6:9] + arr2[6:9]



		thirdRow = self.genThirdRowHelper(forbiddenNums1, puzzle) + self.genThirdRowHelper(forbiddenNums2, puzzle) + self.genThirdRowHelper(forbiddenNums3, puzzle)
		return thirdRow


	def genThirdRowHelper(self, arr1, puzzle):
		newArr = arr1
		thirdRow = [] 
		x = randint(1, 9)
		count = 0
		j = 0
		while count < 3:
			if puzzle[j] == 0:
				newArr.append(puzzle[j])
				j += 1
			elif x not in arr1:
				thirdRow.append(x)
				newArr.append(x)
				x = randint(1, 9)
				count += 1
				j += 1
			else:
				x = randint(1,9)


		return thirdRow



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



