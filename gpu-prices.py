import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from datetime import date

URL = "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&Order=4"
#Opening up connection and getting the data
uClient = uReq(URL)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})

#Get today's date and convert to string
today = date.today()
today_str = str(today)

#Write the list to csv
extension = ".csv"
filename = "GPU Prices " + today_str + extension
f = open(filename, "w")
headers = "Product_Name, Product_Price\n"

f.write(headers)

#Loop to grab each name and price
for container in containers:
	name = container.findAll("a",{"class":"item-title"})
	price = container.findAll("li",{"class":"price-current"})
	product_name = name[0].text
	product_price = price[0].text
	print("Product_Name:" + product_name)
	print("Product_Price:" + product_price)
	
	f.write(product_name.replace(",","|") + "," + product_price.replace(",","") + "\n")
	
f.close()
