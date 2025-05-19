yas = int(input("Yaşınızı Giriniz! "))
okuma = input("Okuyor musunuz? (evet:e , hayır:h)")
if yas >= 18 and okuma == "h":
    print("Askere gelme yaşınız geldi! ")
elif yas >= 18 and okuma == "e":
    print("Okulunuz bittiğinde askere geleceksiniz! ")
else:
    print("Daha askerlik yaşınız gelmedi! ")