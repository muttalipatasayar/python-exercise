a= int(input("birinci sayı : "))
b=int(input("ikinci sayı : "))
islem=input("işlem giriniz : ")
if islem=="1":
     print("{} ile {} in toplamı {} dir ".format(a,b,a+b))

elif islem=="2":
     print("{} ile {} in farkı {} dir ".format(a,b,a-b))
elif islem=="3":
     print("{} ile {} in çarpmı {} dir ".format(a,b,a*b))
elif islem=="4":
     print("{} ile {} in bölümü {} dir ".format(a,b,a/b))    
else: 
         print("geçersiz işlem")         