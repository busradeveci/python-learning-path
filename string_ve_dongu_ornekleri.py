isim = "busra"
print(isim.title())
#print(isim.replace("gidiyor","gitmiyor"))
# Bu fonksiyonla değişkendeki harfleri veya kelimeleri başka harf veya kelimeyle değiştirebilirsiniz.

#print(isim[-4:-1]) # Sıfırdan üçe kadar alır ama üçteki harfi almaz, "büş" olarak alır. Sıfırı dahil eder.
# -1'den başlar, en sondaki harften başlar yani -1, -2, -3, -4 diye gider. -1 harici diğer harfleri seçer ve yazar.
#print(len(isim)) # Kaç harften oluştuğunu yazar.

# ':' işareti konulması gerekir, hangi harften hangi harfe kadar alması gerektiğini belirtmek için.

#print(isim.title()) # title kullanarak ilk harfi büyük yazdırırız.
#print(isim.upper()) # Değişkenimizin bütün harflerini büyük yazar.
#print(isim.lower()) # Bu fonksiyon da değişkenimizin bütün harflerini küçük yazar.
#print(isim.find("a")) # Bu fonksiyon harf bulmak için kullanılır. Örneğin, "a" harfinin kaçıncı sırada olduğunu gösterir.
#print(isim)
mektup = """Hello, the weather is beautiful today. I hope you are having a great day!"""
print(mektup)  # Bu kod üç tırnak ile yazılan metni olduğu gibi gösterir, noktasından virgülüne kadar.

fruit = 'banana'   # "banana" kelimesinde 6 harf olduğu için 6 kez harfleri alt alta yazdırır. Bu bir for döngüsü örneğidir.
for letter in fruit:
    print(letter)

fruit = 'banana'   # Bu da while döngüsüyle string kullanımıdır. Sırasıyla 0'dan 5'e kadar alt alta yazdırır ve harfleri de gösterir.
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

word = 'banana'  # Kaç tane "a" olduğunu sayar. For döngüsü ve if ifadesi kullanılmıştır.
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

s = "The weather is beautiful today"
#  01234567891011
print(s[0:4])  # Sıfırdan başla, dördü dahil etme. Yani "Büşr" yazdırır.
print(s[6:7])  # 6'dan başla, 7'yi dahil etme. Yani "D" yazdırır.
print(s[6:20])  # 20 harf olmasa bile 6'dan başlayıp sonuna kadar yazdırır.
print(s[:2])   # İlk kısmı atlayıp yazmazsanız, dizenin başlangıcını varsayar.
print(s[8:])   # İkinci kısmı atlayıp yazmazsanız, dizenin sonunu varsayar.
print(s[:])    # Hiçbir şey yazmazsanız, baştan sona kadar tüm diziyi yazar.

metin = "Python Java C++"
print(metin.split(" ", 1))  # ['Python', 'Java C++']

width = 15
height = 12.0
print(height / 3)