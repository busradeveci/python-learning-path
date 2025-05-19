#alıştırma2 modül operatörüyle iki sayıyı bölümünden kalanları hesaplama
num = int(input('Give me a number: '))
check = int(input('Give me a number divide by: '))
if num %4 == 0:
    print(num, "4'ün katıdır. ")
elif num %2 == 0:
    print(num, "2'nin katıdır. ")
else:
    print("Nothing.")
if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "divides not evenly by", check)

