from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

rootUrl = "https://batterybro.com/collections/18650-battery/type_18650_battery"
try:
    page = urlopen(rootUrl)
except:
    print("Error opening the URL")
soup = BeautifulSoup(page, 'html.parser')
cellList=soup.find_all(class_="product span3")

with open('cell_csv.csv', 'w') as cell_csv:
	cellDetails = csv.writer(cell_csv, quoting=csv.QUOTE_MINIMAL)
	cellDetails.writerow(['Model Name','Ampere','capacity'])

	for cell in cellList:
		cellName=cell.find(class_="title").text
		if cell.find(class_="sp_amps")==None:
			cellAmps=0
		else: 
			cellAmps=cell.find(class_="sp_amps").text
		cellCapacity=cell.find(class_="sp_capacity").text
		cellUrl=cell.find('a').attrs['href']
		print(cellUrl)
		cellDetailedPageUrl= "https://batterybro.com" + cellUrl

		try:
			detailedPage = urlopen(cellDetailedPageUrl)
			
		except:
		    print("Error opening the URL")
		
		detailedPage=BeautifulSoup(detailedPage, 'html.parser')
		cellSpecifications=detailedPage.find("div",id="content1")
		cellFeatures=cellSpecifications.find_all("li",recursive=True)
		# print(cellFeatures)
		for feature in cellFeatures:
			# print(feature.text)
			if feature.text.__contains__(':'):
				description=feature.text.split(":")
				wholeData=description[1]
				cellDetails.writerow([wholeData])
		# cellDetails.writerow([cellName,cellAmps,cellCapacity,wholeData])
		
		# print(cellName, cellAmps, cellCapacity)
		
				