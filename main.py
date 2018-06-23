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



# print(len(numsArrGiven))



sudokuPuzzle = []
for j in range(0, 9):
	print(numsArr[j])


print("\n")	
for j in range(0, 9):
	print(numsArrGiven[j])



