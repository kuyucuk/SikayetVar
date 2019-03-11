# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3
import csv
import os

say=0

sitelink= "www.sikayetvar.com"
sitelink = str(sitelink).replace("https://", "")
sitelink = sitelink.replace(".com/", ".com")

marka = open("marka.txt", "r")
marka = marka.read()
print(marka)


class MySpider(scrapy.Spider):
    name = "link"
    start_urls = [
    "https://"+sitelink+"/"+marka+""
    ]

    marka = marka.replace("-", "")
    with open("marka.txt", "w", encoding="utf-8") as file:
        file.write(marka)

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS " + str(
        marka) + "(sikayet_id TEXT, baslik TEXT, icerik TEXT, kisi TEXT, goruntulenme TEXT, tarih TEXT, link TEXT)")

    def parse(self, response):
        with open("linkler.txt", "a", encoding="utf-8") as file:

            liste = response.xpath('//*[@id="gridListView"]/div/div/div[1]/div/h2/a/@href').extract()
            liste = str(liste).replace("'/", "'https://"+sitelink+"/")
            liste = str(liste).replace("', '", ",")
            liste = str(liste).replace("']", "")
            liste = str(liste).replace("['", ",")

            file.write(str(liste))


        if response.xpath("/html/body/div[1]/div/a["+str(len(response.xpath('/html/body/div[1]/div/a/@href').extract()))+"]/@class").extract() != []:
            next_url = "https://" + sitelink + response.xpath("/html/body/div[1]/div/a["+str(len(response.xpath('/html/body/div[1]/div/a/@href').extract()))+"]/@href").extract()[0]
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
        else:
            print("son")
            liste = open("linkler.txt", "r")
            liste = liste.read()
            liste = str(liste).replace("', '", ",")
            liste = str(liste).replace("']", "")
            liste = str(liste).replace("https", ",https")
            liste = str(liste).replace(",,", ",")


            print(liste)

            with open("linkler.txt", "w", encoding="utf-8") as file:
                file.write(str(liste))

            return 0


