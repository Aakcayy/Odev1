# # Ders 1 Uygulama
# print("AcunMedya")
# baslik="yapay zeka"
# print(baslik)
# #yorum satırı için ya # koy veya CTRL+Ö 

# vade=36

# aylikodeme=200.504

# yukselistemi=False

# print(5+5)
# print(vade+12)

# print(5*5)
# print(10/2)
# ekvade=vade/2

# print(ekvade)
# print(10%2)
# print(vade%ekvade)

# print(1>2)
# print(1<2)
# print(1>=2)
# print(1<=1)
# print(1!=1)

# print(1<2 or 5>2)
# print(1<2 and 5>2)

# sayi1=10
# sayi2=15


# if sayi1>sayi2:
#     print("Sayi1 sayi 2 den büyüktür")
#     print("Hala if teyim 1  boşluk birakip yazdigin sürece")
# elif sayi1 == sayi2:  #if else burada elif şeklinde
#   print("Sayi1 sayi 2 ye esittir")
# else:
#     print("Sayi1 sayi 2 den küçüktür")

# # Ders 2 Uygulama

# print(type(faiz))

# print(int(vade)+12) #vade değişkenini int tipine döndürür her zaman olmaz uygun değişken türüne döndürür ve toplar yoksa hata verir

# vade=input("Sayi giriniz:")
# print(vade)

# vade=input("Kullanicinin girdiği sayi:"+vade) #int ile string toplamış gibi oluyor onun için str(vade)
# vade=input("Kullanicinin girdiği sayi:{p}"+vade.format(p=vade))#format ile süslü parantez içinde p gördüğüm yere bu değeri ata diyor

# isim="halit"
# metin="Merhaba {isim}".format(isim="Hasan")
# print(metin)

# #f -string
# metin=f"Hosgeldiniz{isim}"
# metin=f"Hosgeldiniz{1+1}" #Metin içerisinde kod yazabiliriz veya aynı format gibi ama daha kolay biçimde kullanabiliriz
# print(metin)

# krediler=["a","b","c"]
# print(type(krediler))
# print(krediler[0])

# print(len(krediler)) #Liste uzunluğu

# dizi=["a",1,5.2,True]
# print(dizi)

# krediler.append("c") #Objeyi listeye ekler
# print(krediler)

# krediler.pop(0) #Parametre verirse objeyi listeden siler vermezsen son objeyi siler > index e göre
# print(krediler)

# krediler.remove("a") #Değer veya değerler varsa olanları siler  > değere göre
# print(krediler)

# krediler.extends(["a","b"]) #Elemanları dizeye ekler
# print(krediler)

# for i in range(50): #range => i yi 0 dan başlatıp döngüyü sağladığı sürece içindeki sayıya kadar arttırır(İnt için) + dışardan da değer alabilir
#    print(i)

# for i in range(5,50): #0 dan değilde neyden başlatmak istiyorsam 5 den 10 a kadar
#    print(i)

# for i in range(5,50,5): #1 er 1 er değilde kaçar kaçar artmasını istiyorsam 
#    print(i)

# krediler=["a","b","c"] 

# for i in krediler: #Listedeki elemanlar aktarana kadar dön <<İkiside aynı işlemi yapar
#    print(i)

# for i in range(len(krediler)): #Listedeki elemanlar aktarana kadar dön <<İndex li hali
#    print(krediler[i])

# while True: #Sonsuz döngü >>Sonsuz döngüyü bitirebilmek için ya manuel olarak CTRL+C ile kırabilirim ya da döngü içine break ekleyerek
#    print("x")

# i = 0

# while i < 10: #Sonsuz döngü >>Sonsuz döngüyü bitirebilmek için manuel olarak CTRL+C
#    print("x")
#    i=i+1    # i++ hata verir bu şekil olacak


# def hesaplama():
#    print(100-20)

# calculate()

# def Parametrelerilehesaplama(a,b):
#    print(a-b)

# Parametrelerilehesaplama(50,10)

# def hesaplamadondur(sayi1,sayi2):
#    return sayi1-sayi2

# tutar=hesaplamadondur(50,40) #geriye döndürdüğü için bir değişkene eşitleyebildik
# print(tutar)

#ders 3

# class Human:
 
#  def talk(self,sentence):
#       name="Ercan"
#       print(f"{self.name}:{sentence}")

#  def walk(self):
#       print(f"{self.name}: is walking")
    
#  def __init__(self,name):
#        self.name=name

#  def __str__(self):
#      return f"Donen deger:{self.name}"

# human1=Human("Ali")
# human1.talk("Merhaba")
# human1.walk()
# print(human1)

# human2=Human("Yusuf")
# human2.name="Murat"
# human2.talk("Merhaba")
# human2.Walk()
# print(human2)

from human import Human
import matematik as math
