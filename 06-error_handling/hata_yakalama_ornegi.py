# TRY / EXCEPT KOŞULLU YAPI ÖRNEĞİ
a = input("Bir sayı giriniz: ")
try:
    b = int(a)
except:                          #bu kodlarla hata tespiti yapmış oluyoruz aslında. kullanıcı kodumuzun hata vereceği bir kod gönderdi ama biz o satırı try ve except bloguna koyduk
                                                                          #ve böylece yakaladık ve bu gerçekle yüzleştik.
    b = -1
if b>0 :
    print("Nice work")
else:
    print("sayı yok")
