girilen_sayi1=int(input("Bir sayı giriniz : "))
girilen_sayi2=int(input("İkinci satıyı giriniz : "))
print(" Değiştirilmeden önce değerler \n girlen_sayi1 :{}  girilen_sayi2:{}\n  ".format(girilen_sayi1,girilen_sayi2))
girilen_sayi1,girilen_sayi2=girilen_sayi2,girilen_sayi1
print("değiştirlidikten sonraki değer \n girilen_sayi1 :  {} girilen_sayi2 78: {}\n".format(girilen_sayi1,girilen_sayi2))