# Basit bir şekil çizimi ve string çarpma işlemi
print("Büşra Deveci")
print(" o----")
print(" ||||")
print("*" * 10)  # 10 adet yıldız yazdırır

# Kullanıcıdan bilgi alma ve çıktı verme örnekleri
# name = input("Adınız nedir? ")
# print("Merhaba " + name)
# renk = input("En sevdiğiniz renk nedir? ")
# print(name + ", bu harika bir renk tercihi: " + renk)
# soz = input("En sevdiğiniz söz nedir? ")
# print(name + ", en sevdiğiniz söz gerçekten çok etkileyici: " + soz)

# Doğum yılına göre yaş hesaplama
# dogum_yili = input('Doğum yılınızı giriniz: ')
# yas = 2024 - int(dogum_yili)
# print("Yaşınız:", yas)

# Kilo dönüştürme (lbs'den kg'ye)
# kilo_lbs = input('Kilonuzu pound (lbs) cinsinden giriniz: ')
# kilo_kg = int(kilo_lbs) * 0.45
# print("Kilonuz kilogram cinsinden:", kilo_kg)

# Çok satırlı bir e-posta örneği
email = '''
Hello,
How are you? I hope everything's okay. Everything is going very well for me.
That's all for now, see you soon.
Take care of yourself!
'''
print(email)

# String işlemleri
isim = "büşra"
print("Harf 'q' dizide bulunuyor mu? Pozisyon:", isim.find('q'))  # 'q' harfi bulunamazsa -1 döner
print("Büyük harflerle yazılmış hali:", isim.upper())  # Tüm harfleri büyük yapar

# String dilimleme örneği
course = "Büşra Deveci"
print("Son 5 karakter:", course[-5:])  # Son 5 karakteri alır


