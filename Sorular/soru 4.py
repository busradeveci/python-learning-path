#4 ikinci dereceden ax^2+bx+c = 0 denkleminin diskiriminant çözümünü yapınız?
# Kullanıcıdan a,b ve c değerlerini alarak deltayı hesaplayınız?
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

#diskriminantı hesaplama
D = b**2 - (4*a*c)

#sonuçları değerlendirme
if D > 0:
    print("İki farklı reel kök vardır.")
elif D == 0:
    print("Bir çift kök vardır (tek bir reel kök).")
else:
    print("Reel kök yoktur")  #karmaşık kökler vardır.

#diskriminant değerini yazdırma
print(f"Diskiriminant (D) değeri:{D}")
