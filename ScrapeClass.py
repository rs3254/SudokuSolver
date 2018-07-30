from HandleRequests import get_url
from bs4 import BeautifulSoup

class ScrapeClass:

	def scrape(self):
		raw_html = get_url("https://www.sudokuweb.org")
		html = BeautifulSoup(raw_html, "html.parser")
		nums = html.find_all("span", {"class":["true", "sedy"]})
		numsArr = [z for j in nums for z in j]


		givenNums = html.find_all("span", class_="true")
		numsArrGiven = [z for j in givenNums for z in j]

		return (numsArrGiven, numsArr)



	


	def parseData(self, arr):
		sudokuPuzzle = []
		finishedPuzzle = [] 
		count = 0
		for j in range(0, 81):
			if count > len(arr[0]) -1:
				break
			elif arr[1][j] == arr[0][count]:
				sudokuPuzzle.append(arr[1][j])
				count += 1
			else:
				sudokuPuzzle.append(0)

		arrC = list(map(int, sudokuPuzzle))
		return arrC




	def scrapeUntilSuccess(self):
		arr = self.scrape()
		arrClean = self.parseData(arr)

		while len(arrClean) != 81:
			print(len(arrClean))
			print("Scraping failed trying again")
			arr = self.scrape()
			arrClean = self.parseData(arr)

		if len(arrClean) == 81:
			print("scraping successful")
		


		return arrClean

	
	