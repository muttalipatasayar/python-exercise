sayi=int(input("bir sayı giriniz :  "))
toplam= 0
i=1
while(i<sayi):
    if(sayi % i == 0):
        toplam +=i
    i += 1
if(toplam == sayi):
    print(sayi, "mükemmel bir sayıdır: ")  
else:          
    print(sayi, "mükemmel bir sayı değildir.  ")
