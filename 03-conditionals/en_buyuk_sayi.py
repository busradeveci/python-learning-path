a = 10
b = 35
c = 4

#bu sayıların en büyüğü hangisidir?

if a >= b:
    if a >= c:
        en_buyuk = a
    else:
        en_buyuk = c
else:
    if b >= c:
        en_buyuk = b
    else:
        en_buyuk = c

print("En büyük sayi:", en_buyuk)

