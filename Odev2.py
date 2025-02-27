print("Asal sayı mı değil mi")

sayi=input("Bir sayı giriniz ->>  ")
print(sayi)

def asalbulma(sayi,i,kontrol):
   
 while i<int(sayi):
    if int(sayi)%i==0 :
      kontrol=kontrol+1
      
        
    else:
        break 

    i=i+1
 return kontrol

sonuc=asalbulma(sayi,i=2,kontrol=0)
if sonuc==0:
   print("Sayi asaldır")

else:
   print("Sayi asal sayı değildir")


# print("Hesaplamaya hoşgeldiniz")

# sayi1=int(input("İlk sayıyı giriniz ->> "))
# sayi2=int(input("İkinci sayıyı giriniz ->> "))

# print("Hangi işlemi yapmak istersiniz \n1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme")
# islem=int(input("->> "))


# if islem>=1 and islem<=4:
     
#  def hesaplama(sayi1,sayi2,islem):
     
#      if islem==1:
#           sonuc=sayi1+sayi2
          
#      elif islem==2:
#            sonuc=sayi1-sayi2

#      elif islem==3:
#           sonuc=sayi1*sayi2

#      elif islem==4:
#           if sayi2==0:
#                print("Bölme işlemi için ikinci sayı 0 olamaz!" )
#           else:
#                sonuc=float(sayi1/sayi2)
        
#      return sonuc
 
#  tutar=hesaplama(sayi1,sayi2,islem) 
#  print(tutar)
 
# else:
#      print("Geçersiz işlem türü! \nTekrar deneyiniz")

          
 
     








          


 