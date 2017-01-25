tauSayilari = 0
for sayi in range(1,1000):
    adet = 0

    for i in range(sayi,0,-1):
        if sayi % i == 0:
            adet += 1
    if sayi % adet == 0:
        print(sayi,"Sayısı Bir Tau sayısıdr")
        tauSayilari += 1
    else:
        print("!",sayi,"Sayısı Bir Tau Sayısı Değildir !")

print(tauSayilari)
