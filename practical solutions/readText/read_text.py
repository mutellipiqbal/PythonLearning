import urllib

def readText():
    quotes= open("D:\\python\\readText\\material.txt")
    contentOfFile = quotes.read()
    #print contentOfFile
    quotes.close()
    checkInternet(contentOfFile)

    
def checkInternet(checkText):
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text=" +checkText)
    output = connection.read()
    print(output+ "\nyou have bad words")
    connection.close()

readText()

