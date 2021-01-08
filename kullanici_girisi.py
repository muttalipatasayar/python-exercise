sys_kullanici_adi="muttalip"
sys_parola="12345"
giris_hakki= 3

while True:
    kullanici_adi=input("Kullanıcı adı : ")
    parola=input("Parola : ")
    if(kullanici_adi !=sys_kullanici_adi and parola ==sys_parola):
        print("Kullanıcı adını yanlış girdiniz :   ")
        giris_hakki -=1
    elif (kullanici_adi == sys_kullanici_adi and parola !=sys_parola):
        print("Parolayı yanlış girdiniz :  ")
        giris_hakki -=1
    elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı adı ve parola hatalı")
        giris_hakki -=1
    else:
        print("Sisteme giriş işleminiz başarılı")
        break
    if(giris_hakki==0):
        print("Giriş hakkınız bitti...")
        break            
    
 
