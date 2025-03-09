# sayilar = []
# sonuc=0
# for i in range(5):
#     sayi = int(input(f"{i+1}. sayıyı giriniz: "))
#     sayilar.append(sayi)

# print("Girilen Sayılar:", sayilar)

# print(sum(sayilar))
# print(sum(sayilar)/len(sayilar))
# print(min(sayilar))     
# print(max(sayilar))  

# kelimeler = []
# for i in range(5):
#     kelime= str(input(f"{i+1}. kelimeyi giriniz: "))
#     kelimeler.append(kelime)


# print(kelimeler)
# kelimeler.reverse()
# print(kelimeler)
# print(kelimeler[::-1])

kelimeler = []
for i in range(5):
    kelime= str(input(f"{i+1}. kelimeyi giriniz: "))
    kelimeler.append(kelime)
    

print(list(set(kelimeler)))