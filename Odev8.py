# print("Hesaplama zamanı")

# sayi1=int(input("Bir sayi giriniz ->>  "))
# sayi2=int(input("İkinci sayiyi giriniz ->>  "))

# secim=int(input("Yapmak istediğiniz işlemi seçiniz\n1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\n\n"))



# def hesaplama(sayi,sayi2,secim):
#  case={}
#  while True:
#         try:

#             case = {

#                  1:sayi1+sayi2,
#                  2: sayi1-sayi2,
#                  3: sayi1*sayi2,
#                  4: sayi1/sayi2, 
#                  'default':'yanlış bir değer girdiniz' 

#             }
#             return case[secim]  
#             break 



#         except KeyError:
#             print(case['default']) 
#             break 
   

# sonuc = hesaplama(secim, sayi1, sayi2)
# print("İşlemin sonucu ->>",sonuc)


# print("Yaş bulmaca")

# yas1=int(input("Yaşınızı giriniz ->>  "))


# def yas(yas1):
#     if yas1<100:
#         kalan_yas=100-yas1
#         return kalan_yas
#     elif yas1>=100:
#         print("Hedef tamamlanmıştır")
#     else:
#         print("Yanlış giriş yapılmıştır\nTekrar deneyiniz.")
    
# sonuc=yas(yas1)
# print(sonuc)

print("Polindrom kelime kontrolü\n")

kelime=input("Bir kelime giriniz ->>  ").lower()

def palindrom(kelime):
    if kelime==kelime[::-1]:
         return 1
    else:
         return 0

sonuc=palindrom(kelime)
if sonuc==1:
 print(f"Kullanıcı tarafından girilen {kelime} kelimesi bir palindromdur. ")

else:
    print(f"Kullanıcı tarafından girilen {kelime} kelimesi bir palindrom değildir ")
 



    