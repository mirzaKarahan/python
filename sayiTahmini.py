from random import randint
isim = input("Merhaba ismini alabilirmiyim\n->")
if not isim:
    print("Lütfen İsmini Gir")
    isim = input("İsim :")
else:
    print("Merhaba ",isim," şimdi sen bir sayı tutacaksın ve bende bu sayıyı bilicem")
    tuttunmu = input("Tuttunmu Sayıyı(Evet/ Hayır)\n->")
    if tuttunmu == "Hayır":
        tuttunmu= input("Tutmanı bekliyorum\n->")
    elif tuttunmu != "Evet":
        print("Ne diyon aq ")
    else:
        bilindi = False
        minm = 0
        maks = 100
        adim = 1
        while bilindi != True:
            tahmin = randint(minm,maks)
            print(adim,". Tahminim", tahmin," ",isim," Doğrumu (E/H)")
            adim+=1
            cevap = input("->")
            if cevap == "E":
                bilindi = True
            elif cevap != "H":
                print("Ne diyonsun lan aq")
            else:
                print(isim," Aşağımı Yukarımı (A/Y)")
                cevap = input("->")
                if cevap == "A":
                    maks = tahmin
                elif cevap == "Y":
                    minm = tahmin
                else:
                    print("Vereceğin cevabın aq")
        adim-=1
        if adim > 10:
            derece = "ne kadar zor bir sayı tutmussun"
        elif adim >= 6 and adim <= 9:
            derece = "zar zor buldum"
        elif adim >= 3 and adim <= 5:
            derece = "fena değilim :)"
        elif adim >= 1 and adim <= 2:
            derece = "Vayy çok iyiyim"
        else:
            derece = "dicek Bir şeyim yok"

        print("Oh be sonunda",isim, derece,sep=" ")
