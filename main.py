from handleRequests import get_url
from bs4 import BeautifulSoup



raw_html = get_url("https://www.sudokuweb.org")
html = BeautifulSoup(raw_html, "html.parser")


{"class":["class1", "class2"]}

nums = html.find_all("span", {"class":["true", "sedy"]})
numsArr = [] 

for j in nums:
	for z in j:
		numsArr.append(z)




givenNums = html.find_all("span", class_="true")
numsArrGiven = [] 

for j in givenNums:
	for z in j:
		numsArrGiven.append(z)




# just used for logic checking 


# for j in range(0, 9):
# 	print(numsArr[j])


# print("\n")	
# for j in range(0, 9):
# 	print(numsArrGiven[j])




sudokuPuzzle = []


count = 0
for j in range(0, 81):
	if count > len(numsArrGiven) -1:
		break
	elif numsArr[j] == numsArrGiven[count]:
		sudokuPuzzle.append(numsArr[j])
		count += 1
	else:
		sudokuPuzzle.append(0)



print(sudokuPuzzle)




# below code checks to see that puzzle created successfully 

# recreateArr = [] 
# for i in range(0, len(sudokuPuzzle)):
# 	if sudokuPuzzle[i] != 0:
# 		recreateArr.append(sudokuPuzzle[i])


# if recreateArr == numsArrGiven:
# 	print("success")






