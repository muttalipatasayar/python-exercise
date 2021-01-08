print ("""///////////////////////////////////////////////

ATM Makinesine Hoş Geldiniz :)

İşlemler : 
1. Bakiye sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için q harfine basınız.... 

///////////////////////////////////////////////""")

bakiye=1000

while True:
    islem= input("İşlemi seçiniz : ")
    if (islem=="q"):
        print("Yine bekleriz....")
    elif(islem=="1"):
        print("Bakiyeniz {} TL'dir ..".format( bakiye))
    elif(islem=="2"):
        miktar=int(input("Miktarı giriniz :  "))
        bakiye+=miktar
        print("Güncel Bakiyeniz {} TL dir: ".format(bakiye))
    elif(islem=="3"):
        miktar=int(input("miktar giriniz :  "))  
        if(bakiye-miktar<0): 
            print("böyle bir miktar çekemezsiniz  :  ")
            continue
        bakiye-=miktar
        print("güncel bakiyeniz {} TL dir".format(bakiye))
    else:
        print("Geçersiz işlem :   ")   
        break 
