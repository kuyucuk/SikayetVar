import os
import scrapy



exists = os.path.isfile('marka.txt')
if exists:
    print("marka.txt dosyasını siliniz.")
else:
    with open("marka.txt", "w", encoding="utf-8") as file:
        file.write(input("Marka adını giriniz: "))

os.system("scrapy crawl link")
os.system("scrapy crawl icerik")

