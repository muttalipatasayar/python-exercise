print(""" **************************************** 

Faktöriyel Bulma Programı

Çıkmak için "q" harine basın

**************************************** """)


while True:
    sayi=input("sayi: ")
    if (sayi=="q"):
      print("Program Sonlandırılıyor:  ")  
      break
    else:
        sayi=int(sayi)
        faktoriyel=1
    for i in range(2,sayi+1):
            print("faktöriyel : ",faktoriyel," i ",i)
            faktoriyel*=i
    print("faktöriyel : ",faktoriyel)