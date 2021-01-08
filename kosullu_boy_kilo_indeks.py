boy=float(input("boyunuzu giriniz : "))
kilo=int(input("kilonuzu giriniz : "))
indeks=kilo/(boy**2)
if (indeks<18.5):
    print("zayıf")
elif(indeks>=18.5 and indeks<25):
    print("Normal")    
elif(indeks>=25 and indeks<30):
    print("Fazla Kilolu")   
else:
    print("Obez")