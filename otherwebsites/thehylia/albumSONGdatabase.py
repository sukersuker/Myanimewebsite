#THIS FILE IS TO GENERATE A LOCAL DATA BASE FROM HTTPS://ANIME.THEHYLIA.COM
#ARGUMENT SHOULD BE A ALBUM_URL eg : https://anime.thehylia.com/soundtracks/album/hunter-x-hunter-2011-ed-single-just-awake/

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import sqlite3 , time , re 

thehylia = "https://anime.thehylia.com/"
music = "https://anime.thehylia.com/soundtracks/browse/all"
animusic = "https://anime.thehylia.com/downloads/browse/all"

import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)


for x in arguments:
   # print("x is :", x)
    uclient = ureq(x)
    soup_html = uclient.read()
    uclient.close()
    htmlsoup = soup(soup_html , "html.parser")

    content = htmlsoup.findAll("tr")
    for c in content:
        cor = c.findAll("a")
        for ass in cor:
            if "soundtracks" in ass['href']:
                print("NAME||",str(ass.text))
                print("URL||",str(ass['href']))
    #content = content.find("table")
    #print('\n'*25)
    #print(content)
    #print(cor)
    #content = content.findAll("tr")
    #for item in content:
    #    for val in item.findAll("td"):
    #        #print(val.text)
    #        if val.a != None:
    #            print(val.a["href"])
        #print("\n")    

    #with open('./database.db', 'w') as currfile:
    #    for link in content:
    #        currfile.write(str(link["href"]) + "||" + str(link.text) + "\n")
    #print(str(content))

