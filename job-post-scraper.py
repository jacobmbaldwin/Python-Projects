import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from datetime import date

URL = "https://www.indeed.com/jobs?q=entry%20level%20programmer&l=Springfield%2C%20MO&vjk=a9e814066cb73dca"
#Opening up connection and getting the data
uClient = uReq(URL)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"job_seen_beacon"})

#Get today's date and convert to string
today = date.today()
today_str = str(today)


#Write the list to csv
extension = ".csv"
filename = "Entry_Level_Programming_Jobs " + today_str + extension
f = open(filename, "w")
headers = "Job_Title, Company_Name, Company_Location\n"

f.write(headers)


#Loop to grab each name and price
for container in containers:
	job = container.findAll("h2",{"class":"jobTitle"})
	company = container.findAll("span",{"class":"companyName"})
	location = container.findAll("div",{"class":"companyLocation"})
	snippet = container.findAll("div",{"class":"job-snippet"})
	
	job_title = job[0].text
	company_name = company[0].text
	company_location = location[0].text
	job_snippet = snippet[0].text
	
	f.write(job_title.replace(",","|") + "," + company_name.replace(",","") + "," + company_location.replace(",","|") + "," + job_snippet.replace(",","|") + "\n")
	
f.close()
