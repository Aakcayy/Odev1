print("Hoşgeldiniz")

while True:
 dosya=input("Çalışacağınız dosyayı yazınız->>  ")
 with open(f"{dosya}", "a") as odev3:
   metin=input("Yazdırmak istediğiniz metni yazınız->>  ")
   odev3.write(metin+"\n")
 

 try: 
   
   with open(f"{dosya}", "r") as odev3: 
       lines = odev3.readlines()   
   for oku in lines:   
        print("\n"+oku)
   continue

 except FileNotFoundError:
    with open(f"{dosya}", "w") as odev3:
       
     break
   



 


