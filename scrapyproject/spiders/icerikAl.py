# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3
import csv
import os

exists = os.path.isfile('linkler.txt')
if exists:
    linkfile = open("linkler.txt", "r")
    alinanLinkler = linkfile.read()
    alinanLinkler = alinanLinkler[1:len(alinanLinkler) - 1]
    with open("linkler.txt", "w", encoding="utf-8") as file:
        file.write(str(alinanLinkler))
    file.close()

    import csv

    crimefile = open("linkler.txt", 'r')
    reader = csv.reader(crimefile)
    alinanLinkler = [row for row in reader]


    print(len(alinanLinkler[0]))
    linkDizi=alinanLinkler[0]

else:
    linkDizi=[]

print(linkDizi)


say=0

marka = open("marka.txt", "r")
marka = marka.read()
marka=marka.replace("-", "")

#marka="a101"
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS "+str(marka)+"(sikayet_id TEXT, baslik TEXT, icerik TEXT, kisi TEXT, goruntulenme TEXT, tarih TEXT, link TEXT)")


class MySpider(scrapy.Spider):
    name = "icerik"
    start_urls = linkDizi

    def parse(self, response):
        global say
        with open("linkler.txt", "a", encoding="utf-8") as file:

            for title in response.xpath("//html/body"):
                aciklama= title.xpath('//*[@id="complaint-detail"]/section[2]/div/div[1]/div/div/p//text()').extract()

                aciklama = str(aciklama).replace("', '", "")
                aciklama = aciklama.replace("', ", "+")
                aciklama = aciklama.replace('+"', "")
                aciklama = aciklama.replace('", ', "+")
                aciklama = aciklama.replace("+'", "")
                aciklama = aciklama.replace('["', '')
                aciklama = aciklama.replace('"]', '')
                aciklama = aciklama.replace("['", "")
                aciklama = aciklama.replace("']", "")
                say = say + 1

                sikayet_id = response.xpath('//*[@id="complaint-id"]/text()').extract_first()
                baslik = response.xpath('//*[@id="complaint-detail"]//ul/li//text()').extract()[4]
                kisi = response.xpath('//*[@id="complaint-detail"]/section[2]/div/div[1]/div/div/span/span/text()').extract_first()
                goruntuleme = response.xpath('//*[@id="complaint-detail"]/section[2]/div/div[1]/div//b/text()').extract_first()
                tarih = response.xpath('//*[@id="complaint-detail"]/section/div//div//span/@title').extract_first()
                sitelink = response.xpath('//link//@href').extract_first()

        #print(str(say)+" "+aciklama+"\n\n")
        with open("aciklamalar.txt", "a", encoding="utf-8") as file2:
            file2.write(str(say)+" "+aciklama+"\n\n")

        c.execute('SELECT * FROM '+str(marka)+'')
        c.execute("INSERT INTO "+str(marka)+" VALUES (?,?,?,?,?,?,?)", (str(sikayet_id), str(baslik), str(aciklama), str(kisi), str(goruntuleme), str(tarih), str(sitelink)))
        conn.commit()
    #os.remove("marka.txt") 
