#3 Kullanıcıdan alınan 3 sayının en büyüğünü bulan programı yazınız?
a = int(input("a sayısı : "))
b = int(input("b sayısı : "))
c = int(input("c sayısı : "))

if a>b and a>c:
    print("a en büyük sayıdır. ")
elif b>a or b>c:
    print("b en büyük sayıdır. ")
else:
    print("c sayısı en büyük sayıdır. ")