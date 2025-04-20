#PY4E DERSLERİ 3.1 KONUSU PRATİK ALIŞTIRMASI
zaman = input("Enter Hours: ")
oran =input("Enter Rate: ")
zaman = float(zaman)
oran = float(oran)
if zaman > 40:
    print("Overtime")
    reg = zaman * oran
    otp = (zaman - 40.0) * (oran*0.5)
    print(reg,otp)
    sonuc = reg + otp
else:
    print("Regular")
    sonuc = zaman * oran
print(sonuc)