# Problem 1 // Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

a=int(input("birinci sayı : "))
b=int(input("ikinci sayı : "))
c=int(input("üçüncü sayı : "))
carpim=a*b*c
print(" {} X  {} X {} = {} ".format(a,b,c,carpim))