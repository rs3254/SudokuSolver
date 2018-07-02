from random import randint

class NumberClass:
	
	def genRows(self, arr):
		for i in range(0, len(arr)):
			if arr[i] != 0:
				continue
			elif arr[i] == 0:
				x = randint(1, 9)
				while x in arr:
					x = randint(1, 9)
				arr[i] = x
			
		return arr







	def generateRows(self, arr, v1 = None):
		s = set()
		for i in range(0, len(arr)):
			if arr[i] != 0:
				continue
			else:
				x = randint(1, 9)
				if v1 != None:
					while x in arr or x in self.genRowsHelpers(v1, i):
						y = arr + self.genRowsHelpers(v1, i)
						s  = set(y)
						x = randint(1, 9)
						if len(s) >=9:
							break

					if len(s)>= 9:
						while x in arr:
							x = randint(1, 9)
						arr[i] =  x
					else:
						arr[i] = x
				else:
					while x in arr:
						x = randint(1, 9)
					arr[i] =  x

		return arr 






	def genRowsHelpers(self,arr, j):
		newArr = []
		i = j
		while i < len(arr):
			newArr.append(arr[i])
			i += 9

		return newArr
			


	def createSudokuPlane(self,arr, puzzle):
		block1 = list(self.genBlock(puzzle, 0))
		block2 = list(self.genBlock(puzzle, 27))

		count = 0
		totalCount = 0
		while self.checkBlocks(block1, block2) == False:
			block2 = self.genBlock(puzzle, 27, block1)

			count += 1


			if count > 1000:
				block1 = self.genBlock(puzzle, 0)
				totalCount += 1
				count = 0


			

			if totalCount > 500:
				print("not solved")
				break

	
		t = block1 + block2

		block3 = self.genLastBlock(t, puzzle)
		finishedPuzzle = t + block3 


		return finishedPuzzle





	# takes rows and recreates them until they form a correct block. arr has rows. 
	#puzzle is sudoku puzzle with zeros for blanks 
	def genBlock(self, puzzle, startInd, block1 = None):
		arr1 = self.genRows(puzzle[startInd:startInd+9])		
		arr2 = self.generateRows(puzzle[startInd+9:startInd+18], arr1)
	

		while self.checkRows(arr1, arr2) == False:
			if block1 == None:
				arr1 = self.generateRows(puzzle[0:9])
				arr2 = self.generateRows(puzzle[9:18], arr1)
			else: 
				arr1 = self.generateRows(puzzle[startInd:startInd+9], block1)
				block1 = block1 + arr1 
				arr2 = self.generateRows(puzzle[startInd+9:startInd+18], block1)

		arr3 = self.genThirdRow(arr1, arr2, puzzle)

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


	# misnomer generates last block used in function above 
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
	
			if (arr1[i] == arr2[i] or arr1[i] == arr2[i+9] or arr1[i] == arr2[i+18]):
				return False
			if (arr1[i+9] == arr2[i] or arr1[i+9] == arr2[i+9] or arr1[i+9] == arr2[i+18]):
				return False
			if (arr1[i+18] == arr2[i] or arr1[i+18] == arr2[i+9] or arr1[i+18] == arr2[i+18]):
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



