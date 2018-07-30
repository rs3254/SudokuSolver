from ScrapeClass import ScrapeClass
from NumberClass import NumberClass







# misnomer has array that will eventually be finishedPuzzle
finishedPuzzle = [] 


scrapeObj = ScrapeClass()
arrC = scrapeObj.scrapeUntilSuccess()



rowArr = [] 
x = 9
y = 0

numObj = NumberClass()

for i in range(0, 9):
	finishedPuzzle += numObj.genRows(arrC[y:x])
	y = x 
	x += 9





finishedPuzzle = numObj.createSudokuPlane(finishedPuzzle, arrC)


i = 0
while i <= 72:
	print(finishedPuzzle[i:i+9])
	i += 9







# below code checks to see that puzzle created successfully 

# recreateArr = [] 
# for i in range(0, len(sudokuPuzzle)):
# 	if sudokuPuzzle[i] != 0:
# 		recreateArr.append(sudokuPuzzle[i])


# if recreateArr == numsArrGiven:
# 	print("success")






