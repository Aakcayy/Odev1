# for i in range(1,100):
#     print(i)

# for i in range(2,100,2):
#     print(i)

# sayi=int(input("Faktöriyel hesaplama ->>"))
# sonuc=1
# for i in range(1,sayi+1,1):
#    sonuc*=i
  
# print(sonuc)

sayi=int(input("Asal sayıları bulma ->>"))
if sayi <2:
 print("Asal sayı değildir")
else:
 for i in range(2,sayi):
     if sayi%i==0:
      print("Asal sayi değildir")
      break
     
 else :
   print("Asal sayi ")

