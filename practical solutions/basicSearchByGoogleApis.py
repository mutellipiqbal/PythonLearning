import urllib
import json

ara = raw_input("kelime giriniz: ")
encoded = urllib.quote(ara)
 

rawData = urllib.urlopen("https://www.googleapis.com/customsearch/v1?key=AIzaSyAYmDdxOiSO8kjnUR-B01uFQWi62s-3Vxk&cx=017576662512468239146:omuauf_lfve&q=" +encoded).read()

jsonData = json.loads(rawData)
aramaSonucu = jsonData ["items"]


for x in aramaSonucu:
    title = x["title"]
    link = x["link"]

    print title
    print link
