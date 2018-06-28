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



	def createSudokuPlane(self,arr, puzzle):
		block1 = list(self.genBlock(arr, puzzle, 0))
		block2 = list(self.genBlock(arr, puzzle, 27))

		while self.checkBlocks(block1, block2) == False:
			block1 = list(self.genBlock(arr, puzzle, 0))
			block2 = list(self.genBlock(arr, puzzle, 27))




		# arr = block1 + block2 + block2
		# return arr 
		t = block1 + block2

		block3 = self.genLastBlock(t, puzzle)
		finishedPuzzle = block1 + block2 + block3 


		return finishedPuzzle







	# takes rows and recreates them until they form a correct block. arr has rows. 
	#puzzle is sudoku puzzle with zeros for blanks 
	def genBlock(self, arr, puzzle, startInd):
		arr1 = arr[startInd:startInd+9]
		arr2 = arr[startInd+9:startInd+18]
		arr3 = arr[startInd+18:startInd+27]

		while self.checkRows(arr1, arr2) == False:
			arr2 = self.genRows(puzzle[9:18])
			arr1 = self.genRows(puzzle[0:9])

		arr3 = self.genThirdRow(arr1, arr2, arr3)

		mergedArr = arr1 + arr2  + arr3
		return mergedArr






	def genLastBlock(self, arr, puzzle):
		j = 0
		counter = 0 
		completeArr = []
		for j in range(0, 9):
			i = j 
			forbiddenNums = []
			while i < 54:
				forbiddenNums.append(arr[i])
				i += 9

			completeArr.append(forbiddenNums)


		# print(completeArr)
		return self.reformatVerticalArr(self.genForbiddenNums(completeArr, puzzle))


	# misnomer generates last block  
	def genForbiddenNums(self, arr, puzzle):
		x = [] 
		for i in range(0, 9):
			fNums = [] 
			for j in range(0, 6):
				fNums.append(arr[i][j])

			x += self.genCustomRowHelper(list(fNums), puzzle)
			
		return x 
	

	def reformatVerticalArr(self, arr):
		newArr = [] 
		i = 0
		while i < 27:
			newArr.append(arr[i])
			i += 3

		j = 1
		while j < 27:
			newArr.append(arr[j])
			j += 3

		z = 2
		while z < 27:
			newArr.append(arr[z])
			z += 3

		return newArr



	def genThirdRow(self, arr1, arr2, puzzle):
		forbiddenNums1 = arr1[0:3] + arr2[0:3]
		forbiddenNums2 = arr1[3:6] + arr2[3:6]
		forbiddenNums3 = arr1[6:9] + arr2[6:9]


		thirdRow = self.genCustomRowHelper(forbiddenNums1, puzzle) + self.genCustomRowHelper(forbiddenNums2, puzzle) + self.genCustomRowHelper(forbiddenNums3, puzzle)

		return thirdRow



	def genCustomRowHelper(self, arr1, puzzle):
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



	def checkBlocks(self, arr1, arr2):
		for i in range(0, 9):
			if arr1[i] == arr2[i] or arr1[i] == arr2[i+9] or arr1[i] == arr2[i+18]:
				return False
			elif arr1[i+9] == arr2[i] or arr1[i+9] == arr2[i+9] or arr1[i+9] == arr2[i+18]:
				return False
			elif arr1[i+18] == arr2[i] or arr1[i+18] == arr2[i+9] or arr1[i+18] == arr2[i+18]:
				return False


			return True





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



