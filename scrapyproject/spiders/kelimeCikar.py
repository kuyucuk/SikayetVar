import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

toplam = open("turktelekom6ayicerik.txt", "r")
icerik = toplam.read()

icerik = str(icerik).replace("i̇̇", "i")
icerik = str(icerik).replace("İ", "i")
icerik = str(icerik).replace("I", "ı")
icerik = str(icerik).replace("Ö", "ö")
icerik = str(icerik).replace("Ü", "ü")
icerik = str(icerik).replace("Ç", "ç")
icerik = str(icerik).replace("Ş", "ş")
icerik = icerik.lower()

icerik = str(icerik).replace("1", "")
icerik = str(icerik).replace("2", "")
icerik = str(icerik).replace("3", "")
icerik = str(icerik).replace("4", "")
icerik = str(icerik).replace("5", "")
icerik = str(icerik).replace("6", "")
icerik = str(icerik).replace("7", "")
icerik = str(icerik).replace("8", "")
icerik = str(icerik).replace("9", "")
icerik = str(icerik).replace("0", "")

icerik = str(icerik).replace(".", "")
icerik = str(icerik).replace('"', "")
icerik = str(icerik).replace(":", "")
icerik = str(icerik).replace(";", "")
icerik = str(icerik).replace("'", "")
icerik = str(icerik).replace("-", "")
icerik = str(icerik).replace("!", "")
icerik = str(icerik).replace('%', "")
icerik = str(icerik).replace("(", "")
icerik = str(icerik).replace(")", "")
icerik = str(icerik).replace("*", "")
icerik = str(icerik).replace("/", "")
icerik = str(icerik).replace('?', "")
icerik = str(icerik).replace("’", "")
icerik = str(icerik).replace("”", "")
icerik = str(icerik).replace("“", "")
icerik = str(icerik).replace('"', "")
icerik = str(icerik).replace(",", "")
icerik = str(icerik).replace("+", "")
icerik = str(icerik).replace("=", "")

icerik = str(icerik).replace(" bir ", " ")
icerik = str(icerik).replace(" ve ", " ")
icerik = str(icerik).replace(" veya ", " ")
icerik = str(icerik).replace(" bu ", " ")
icerik = str(icerik).replace(" için ", " ")
icerik = str(icerik).replace(" de ", " ")
icerik = str(icerik).replace(" da ", " ")
icerik = str(icerik).replace(" ile ", " ")
icerik = str(icerik).replace(" ne ", " ")
icerik = str(icerik).replace(" bana ", " ")
icerik = str(icerik).replace(" ama ", " ")
icerik = str(icerik).replace(" hiç ", " ")
icerik = str(icerik).replace(" rağmen ", " ")
icerik = str(icerik).replace(" olarak ", " ")
icerik = str(icerik).replace(" diye ", " ")
icerik = str(icerik).replace(" gibi ", " ")
icerik = str(icerik).replace("hakkında", "")
icerik = str(icerik).replace(" bu ", " ")
icerik = str(icerik).replace(" şu ", " ")
icerik = str(icerik).replace(' o ', " ")
icerik = str(icerik).replace(" ki ", " ")
icerik = str(icerik).replace("Bu", "bu")
icerik = str(icerik).replace(" beni ", " ben ")
icerik = str(icerik).replace(" ben ", " ")
icerik = str(icerik).replace(" en ", " ")
icerik = str(icerik).replace(" ya ", " ")
icerik = str(icerik).replace(" ise ", " ")
icerik = str(icerik).replace(" ın ", " ")
icerik = str(icerik).replace(" in ", " ")
icerik = str(icerik).replace(" ini ", " ")
icerik = str(icerik).replace(" ını ", " ")
icerik = str(icerik).replace(" mı ", " ")
icerik = str(icerik).replace(" mi ", " ")
icerik = str(icerik).replace("ler", " ")
icerik = str(icerik).replace("lar", " ")

icerik = str(icerik).replace("tllik", " tl ")
icerik = str(icerik).replace("tlye", " tl ")
icerik = str(icerik).replace("tlden", " tl ")
icerik = str(icerik).replace(" tl ", " türk_lirası ")
icerik = str(icerik).replace("türk telekom", "türk_telekom ")
icerik = str(icerik).replace("müşteri hizmet", "müşteri_hizmetleri ")
icerik = str(icerik).replace("türkcell", "turkcell")
icerik = str(icerik).replace("türksel", "turkcell")
icerik = str(icerik).replace(" ini ", " ")


icerik = str(icerik).replace(" a ", " ")
icerik = str(icerik).replace(" b ", " ")
icerik = str(icerik).replace(" c ", " ")
icerik = str(icerik).replace(" ç ", " ")
icerik = str(icerik).replace(" d ", " ")
icerik = str(icerik).replace(' e ', " ")
icerik = str(icerik).replace(" f ", " ")
icerik = str(icerik).replace(" g ", " ")
icerik = str(icerik).replace(" ğ ", " ")
icerik = str(icerik).replace(" h ", " ")
icerik = str(icerik).replace(" ı ", " ")
icerik = str(icerik).replace(" i ", " ")
icerik = str(icerik).replace(" j ", " ")
icerik = str(icerik).replace(' k ', " ")
icerik = str(icerik).replace(" l ", " ")
icerik = str(icerik).replace(" m ", " ")
icerik = str(icerik).replace(" n ", " ")
icerik = str(icerik).replace(" o ", " ")
icerik = str(icerik).replace(" ö ", " ")
icerik = str(icerik).replace(" p ", " ")
icerik = str(icerik).replace(" r ", " ")
icerik = str(icerik).replace(' s ', " ")
icerik = str(icerik).replace(" ş ", " ")
icerik = str(icerik).replace(" t ", " ")
icerik = str(icerik).replace(" u ", " ")
icerik = str(icerik).replace(" ü ", " ")
icerik = str(icerik).replace(" v ", " ")
icerik = str(icerik).replace(" y ", " ")
icerik = str(icerik).replace(" z ", " ")
icerik = str(icerik).replace(' x ', " ")
icerik = str(icerik).replace(" w ", " ")
icerik = str(icerik).replace(" q ", " ")



wordcount={}
for word in icerik.split():

    if "ücret" in word:
        word = str(word).replace(word, "ücret")

    if "abone" in word:
        word = str(word).replace(word, "abone")

    if "turkcell" in word:
        word = str(word).replace(word, "turkcell")

    if "hattı" in word:
        word = str(word).replace(word, "hat")

    if "tarih" in word:
        word = str(word).replace(word, "tarih")

    if "internet" in word:
        word = str(word).replace(word, "internet")

    if "para" in word:
        word = str(word).replace(word, "para")

    if "paket" in word:
        word = str(word).replace(word, "paket")

    if "fatura" in word:
        word = str(word).replace(word, "fatura")

    if "şikayet" in word:
        word = str(word).replace(word, "şikayet")

    if "operatör" in word:
        word = str(word).replace(word, "operatör")

    if "üslup" in word:
        word = str(word).replace(word, "üslup")

    if "üslub" in word:
        word = str(word).replace(word, "üslup")

    if "taahhüd" in word:
        word = str(word).replace(word, "taahhüt")

    if "haks" in word:
        word = str(word).replace(word, "haksızlık")

    if "iphone" in word:
        word = str(word).replace(word, "apple")

    if "sorun" in word:
        word = str(word).replace(word, "sorun")

    if "uygulama" in word:
        word = str(word).replace(word, "uygulama")

    if "kampanya" in word:
        word = str(word).replace(word, "kampanya")

    if "paket" in word:
        word = str(word).replace(word, "paket")

    if "numara" in word:
        word = str(word).replace(word, "numara")

    if "pişman" in word:
        word = str(word).replace(word, "pişman")

    if "işlem" in word:
        word = str(word).replace(word, "işlem")

    if "kontör" in word:
        word = str(word).replace(word, "kontör")

    if "sözleşme" in word:
        word = str(word).replace(word, "sözleşme")

    if "insan" in word:
        word = str(word).replace(word, "insan")

    if "temsilci" in word:
        word = str(word).replace(word, "temsilci")

    if "fiyat" in word:
        word = str(word).replace(word, "fiyat")

    if "şebeke" in word:
        word = str(word).replace(word, "şebeke")

    if "telefon" in word:
        word = str(word).replace(word, "telefon")

    if "cihaz" in word:
        word = str(word).replace(word, "cihaz")

    if "iletişim" in word:
        word = str(word).replace(word, "iletişim")

    if "iade" in word:
        word = str(word).replace(word, "iade")

    if "sistem" in word:
        word = str(word).replace(word, "sistem")

    if "apple" in word:
        word = str(word).replace(word, "apple")

    if "samsung" in word:
        word = str(word).replace(word, "samsung")

    if "huawei" in word:
        word = str(word).replace(word, "huawei")

    if "istanbul" in word:
        word = str(word).replace(word, "istanbul")

    if "ankara" in word:
        word = str(word).replace(word, "ankara")

    if "izmir" in word:
        word = str(word).replace(word, "izmir")

    if "bursa" in word:
        word = str(word).replace(word, "bursa")

    if "sakarya" in word:
        word = str(word).replace(word, "sakarya")

    if "kocaeli" in word:
        word = str(word).replace(word, "kocaeli")

    if "izmit" in word:
        word = str(word).replace(word, "kocaeli")

    if "antalya" in word:
        word = str(word).replace(word, "antalya")

    if "vodafone" in word:
        word = str(word).replace(word, "vodafone")

    if "müşteri" in word:
        if "müşteri_" not in word:
            word = str(word).replace(word, "müşteri")

    if "hizmet" in word:
        if "_hizmet" not in word:
            word = str(word).replace(word, "hizmet")


    if "telekom" in word:
        if "_telekom" not in word:
            word = str(word).replace(word, "telekom")

    if "öde" in word:
        if "ödev" not in word:
            if "ödem " not in word:
                word = str(word).replace(word, "ödeme")

    if "çekm" in word:
        if "çekmeköy" not in word:
            if "çekmekoy" not in word:
                if "çekmece" not in word:
                    word = str(word).replace(word, "çekim")





    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
n=-1
for key in wordcount.keys():
    #print ("%s %s " %(wordcount[key] , key))
    #print(str((wordcount[key])) + " ---- " + key)
    sheet1.write(n+1, 0, str((wordcount[key])))
    sheet1.write(n+1, 1, key)
    wb.save('sonuç.xls')
    n=n+1

"""
  with open("sonuç.txt", "a", encoding="utf-8") as file:
      file.write("%s %s \n" %(wordcount[key] , key))
"""






