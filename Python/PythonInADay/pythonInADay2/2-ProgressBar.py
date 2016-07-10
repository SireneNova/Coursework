import urllib2, progressbar
from bs4 import BeautifulSoup

def extractMData(webpage):
    soup = BeautifulSoup(webpage, "html.parser")
    #print soup.title

    # find all the div blocks
    divBlock = soup.findAll("div", {"class":"block"})
    #print divBlock[3]
    
    info = divBlock[3]
    # Extract info_left and in_right divs
    getLeft = info.findAll("div", {"class":"info_left"})
    getRight = info.findAll("div", {"class":"info_right"})
    #print getLeft
    #print getRight

    for i in range(0,len(getLeft)):
        textLeft = getLeft[i].get_text()
        textRight = getRight[i].get_text()
        print textLeft + ": " + textRight

    print ""

# Open webpage
webpage = urllib2.urlopen("http://www.inadaybooks.com/justiceleague/")

# Convert to BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Get the contents container div
divContainer = soup.find("div", {"id":"container"})
divBlock = divContainer.findAll("div", {"class":"block"})
divSep = divBlock[3].findAll("div", {"class":"separator"})
members = divSep[3].findAll("a")

nMembers = len(members)
bar = progressbar.ProgressBar(nMembers)

count = 0

# Loop through members
for member in members:
    # Strip <a> tags
    href = member.get("href")
    # Create url to open
    url = "http://www.inadaybooks.com/justiceleague/"+href
    # Open url
    mPage = urllib2.urlopen(url)
    #run, check no errors returned
    
    extractMData(mPage) #see top def

    count+=1 # Increment count
    
    bar.update(count) # Update progress bar

