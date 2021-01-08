from math import  *
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def karealma():
    karesi_alinan=float(input("Karesi alinancak sayi: "))
    karesi_alinan=karesi_alinan**2
    print(karesi_alinan)
def hipotenus():
   dikkenar1=float(input("Dik kenarin birincisi : ")) 
   dikkenar2=float(input("Dik kenarin ikincisi : "))
   hipo=(dikkenar1*dikkenar1+dikkenar2*dikkenar2)**0.5 
   print(hipo)  
def kupcevre():
    karekenar=float(input("Kupun herhangi bir kenarini giriniz : "))
    karekenarcevre=6*(karekenar**2)
    print(karekenarcevre)
def kupalan():
    karekenar=float(input("Kupun  herhangi bir kenarini giriniz : "))
    karekenaralan= karekenar**3
    print("kup : ",karekenaralan)   
def dairecevre():
    pi=float(input("Varsayilan Pi : "))
    daire=float(input("Yari Capi Giriniz : "))
    dairecevresonuc=2*pi*daire
    print(dairecevresonuc)
def dairealan():
    pi=float(input("Varsayilan Pi : "))
    daire=float(input("Yari Capi Giriniz : "))
    dairealansonuc = (pi) * (daire ** 2)
    print(dairealansonuc)

print("******************************************* ***\n"
"GELİŞMİŞ HESAP MAKİNESİ PROGRAMI \n"
"LÜTFEN İŞLEM SEÇİN\n"
"1. İşlem = Toplama \n"
"2. İşlem = Çıkarma \n"
"3. İşlem = Çarpma \n"
"4. İşlem = Bölme \n"
"5. İşlem = Kare Alma \n"
"6. İşlem = Faktoriyel \n"
"7. İşlem = Hipotenüs \n"
"8. İşlem = Küp Çevre Hesaplama \n"
"9. İşlem = Küp Alan Hesaplama \n"
"10. İşlem = Daire Çevre Hesaplama \n"
"11. İşlem = Daire Alan Hesaplama \n"
"**********************************************\n" )

islem =input("Islem Seciniz... ")
while True:
    if (islem == "q"):
      print("Cikis Yaptiniz Iyi Gunler Dileriz ...")
      break
    elif (islem == "1"):
        a=int(input("birinci sayi "))
        b=int(input("ikinci sayi ")) 
        print(toplama(a,b))
    elif (islem== "2"):
        a=int(input("birinci sayi "))
        b=int(input("ikinci sayi ")) 
        print(cikarma(a,b))   
    elif (islem == "3"):
        a=int(input("birinci sayi "))
        b=int(input("ikinci sayi ")) 
        print(carpma(a,b))
    elif (islem== "4"):
        a=int(input("birinci sayi "))
        b=int(input("ikinci sayi ")) 
        print(bolme(a,b))   
    elif (islem =="5"):
        karealma()
    elif (islem =="6"):
        faktoriyel =int(input("Faktoriyeli alinacak sayiyi giriniz ... "))
        faktoriyel_sonuc=factorial(faktoriyel)
        print(faktoriyel_sonuc)
    elif(islem=="7"):
        hipotenus()
    elif(islem=="8"):
        kupcevre()
    elif(islem=="9"):
        kupalan()
    elif(islem=="10"):
        dairecevre()
    elif(islem=="11"):
        dairealan()
    else:
        print("Geçersiz İşlem Yaptınız!! Lüfen Tekrar Deneyin !!")           