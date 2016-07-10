import urllib2
from bs4 import BeautifulSoup

# Open webpage
webpage = urllib2.urlopen("http://www.inadaybooks.com/justiceleague/")

# Convert to BeautifulSoup
soup = BeautifulSoup(webpage,"html.parser")


#print soup.title

#print soup.body

#Get the contents container div
divContainer = soup.find("div", {"id":"container"})
#print divContainer

divBlock = divContainer.findAll("div", {"class":"block"})
#print divBlock
#print divBlock[3]

#find div w class sep
divSep = divBlock[3].findAll("div", {"class":"separator"})
#print divSep
#print divSep[3]
members = divSep[3].findAll("a")
#print members


# Loop through members
for member in members:
    # Strip <a> tags
    #print member.get_text()
    #print member.get("title")
    #print member.get("href")

    href = member.get("href")
    # Create url to open
    url = "http://www.inadaybooks.com/justiceleague/"+href
    # Open url
    mPage = urllib2.urlopen(url)
    #run, check no errors returned
