sayi = input("Sayıyı Giriniz") # 24 örnek bir Tau sayısıdır
adet = 0

for i in range(sayi,0,-1):
    if sayi % i == 0:
        adet += 1
if sayi % adet == 0:
    print(sayi,"Sayısı Bir Tau sayısıdr")
else:
    print("!",sayi,"Sayısı Bir Tau Sayısı Değildir !")
