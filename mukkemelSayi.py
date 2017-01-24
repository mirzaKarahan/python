sayi = 28
inToplami = 0
for item in range(sayi-1,0,-1):
       if sayi % item == 0:
           print("bölünüyor",item)
           inToplami += item

if inToplami == sayi:
    print(inToplami,"Bir Mükemmel Sayıdır")
else:
    print(inToplami,"Mükemmel Sayı Değildir")
