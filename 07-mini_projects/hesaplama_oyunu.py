isim = input("Lütfen adınızı giriniz: ")
print("Hoş geldiniz, " + isim + "!")
yas = int(input("Lütfen yaşınızı giriniz: "))
print("Teşekkürler! Şimdi devam edelim.")

giris = input("""Merhaba tekrar, hoş geldiniz! Şimdi sizinle küçük bir hesaplama oyunu oynayacağız. Hazır mısınız? (Evet/Hayır): """)
i = 1
while i <= 5000:
    i += 1
    print(i)
print("""Tamam, şimdi başlıyoruz! Lütfen dikkatli olun ve hazır olun!""")

print("Başlayalım!")
eee = int(input("Lütfen bir sayı giriniz: "))
bbb = int(input("Lütfen ikinci bir sayı giriniz: "))

islem = input("Lütfen yapmak istediğiniz işlemi seçiniz (Toplama: +, Çıkarma: -, Çarpma: *, Bölme: /): ")
if islem == "+":
    print("Sonuç:", eee + bbb)
elif islem == "-":
    print("Sonuç:", eee - bbb)
elif islem == "*":
    print("Sonuç:", eee * bbb)
elif islem == "/":
    print("Sonuç:", eee / bbb)
else:
    print("Geçersiz işlem seçimi.")
print("Teşekkürler! İşleminiz tamamlandı.")
















