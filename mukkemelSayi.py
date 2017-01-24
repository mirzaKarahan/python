sonuc = 0
for b in range(100000):
    sayi = b
    degerler = 0
    for a in range(sayi-1,0,-1):
        if sayi % a == 0:
            degerler += a
            #print(a)
    if degerler == sayi:
        print("Mükemmel Sayıdır :",degerler)
        sonuc +=degerler

print(degerler)
