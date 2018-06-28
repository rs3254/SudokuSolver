from HandleRequests import get_url
from bs4 import BeautifulSoup
from NumberClass import NumberClass



# raw_html = get_url("https://www.sudokuweb.org")
# html = BeautifulSoup(raw_html, "html.parser")


# {"class":["class1", "class2"]}

# nums = html.find_all("span", {"class":["true", "sedy"]})
# numsArr = [] 

# for j in nums:
# 	for z in j:
# 		numsArr.append(z)




# givenNums = html.find_all("span", class_="true")
# numsArrGiven = [] 

# for j in givenNums:
# 	for z in j:
# 		numsArrGiven.append(z)



# sudokuPuzzle = []
# finishedPuzzle = [] 

# count = 0
# for j in range(0, 81):
# 	if count > len(numsArrGiven) -1:
# 		break
# 	elif numsArr[j] == numsArrGiven[count]:
# 		sudokuPuzzle.append(numsArr[j])
# 		count += 1
# 	else:
# 		sudokuPuzzle.append(0)



# print(sudokuPuzzle)





# misnomer has array that will eventually be finishedPuzzle
finishedPuzzle = [] 

puzzleT = ['4', 0, '1', 0, 0, '3', '9', 0, '5', 0, 0, 0, '7', '1', '4', '8', '3', 0, 0, '7', '3', '9', 0, 0, '1', 0, '4', '7', '1', 0, '3', '2', 0, '5', '8', '9', '8', '3', '9', '5', 0, '7', 0, 0, '2', 0, '6', 0, 0, 0, '1', '3', 0, 0, 0, '2', '6', '4', '3', 0, '7', 0, '8', 0, '5', 0, '1', '7', '2', '4', '6', 0, 0, 0, 0, 0, 0, 0, '2', 0, '1']
arrC = list(map(int, puzzleT))

# print(len(arrC))
# print(arrC)


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

	





















# print(finishedPuzzle[18:27])


	











# below code checks to see that puzzle created successfully 

# recreateArr = [] 
# for i in range(0, len(sudokuPuzzle)):
# 	if sudokuPuzzle[i] != 0:
# 		recreateArr.append(sudokuPuzzle[i])


# if recreateArr == numsArrGiven:
# 	print("success")






