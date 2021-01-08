birler=["","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz","on"]
onlar=["","On","Yirmi","Otuz","Kirk","Elli","Altmis","Yetmis","Seksen","Doksan",]

def okunus(sayi):
    
    birinci=sayi % 10
    ikinci=sayi // 10
    
    return onlar[ikinci] + " " + birler[birinci]

sayi = int(input("Sayi : "))

print(okunus(sayi))