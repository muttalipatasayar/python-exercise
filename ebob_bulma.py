
def ebob_bulma(sayi1,sayi2):
    i=1
    ebob=1
    while (i <= sayi1 and i<= sayi2):
        if (not (sayi1 % i) and not (sayi2 % i)):
            ebob = i
        i += 1    
    return ebob
sayi1 = int(input("Sayı-1:"))
sayi2 = int(input("Sayı-2:"))

print("Ebob:",ebob_bulma(sayi1,sayi2))   

