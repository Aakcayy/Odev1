# print("Programımıza hoşgeldiniz")

# isim=input("Adınız ve soyadınız ->>  ")
# yas=input("Yaşınız ->>  ")
# dogum_yili=input("Doğum yılınız ->>  ")

# print(f"Merhaba {isim}! {yas} yaşındasın ve {dogum_yili} yılında doğmuşsun")


print("Hesaplama zamanı")

sayi1=int(input("Bir sayi giriniz ->>  "))
sayi2=int(input("İkinci sayiyi giriniz ->>  "))

secim=int(input("Yapmak istediğiniz işlemi seçiniz\n1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\n\n"))


def switch(secim,sayi1,sayi2):
    case={}
    while True:
        try:

            case = {

                 1:sayi1+sayi2,
                 2: sayi1-sayi2,
                 3: sayi1*sayi2,
                 4: sayi1/sayi2, 
                 'default':'yanlış bir değer girdiniz' 

            }
            return case[secim]  
            break 



        except KeyError:
            print(case['default']) 
            break 

sonuc = switch(secim, sayi1, sayi2)
print("İşlemin sonucu ->>",sonuc)
