x = 10
if x<2:
    print("x küçüktür")
elif x<20:
    print("20 den küçüktür")     #burada eliflerin sırası çok önemli. doğru şekilde kodlama da doğru sıraya koymazsak diğer yazdığımız elif kodu işlevsiz kalıyor
elif x<10:                          #elif x<10 kodu normalde x=10 ya da x=8 dediğimizde ikinci satırdaki kodu çalıştırıyor çünkü SIRA ÖNCELİĞİNİ ONA VERDİK. sıraları doğru kullanmamız lazım!!
    print("10 dan küçüktür")              #ve hangisi ilk doğruysa diğer satırı görmüyor ve o doğru olan kodu direk yazıyor if elif else de böyle.
                                              #elifleri istediğimiz kadar çok yazabiliriz if elif else de bunun sorunu hiç yoktur.
else:
    print("hiçbiridir")