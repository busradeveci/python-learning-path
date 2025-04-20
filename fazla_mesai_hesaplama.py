
def computepay(zaman,oran):
    #print("In computepay, zaman, oran")
    if zaman > 40:
        reg = zaman * oran
        otp = (zaman - 40.0) * (oran * 0.5)        #hesaplamamızı fonksiyonun içine taşıdık yani def'in içine.if else de defin altına yazabiliyoruz.
        pay = reg + otp
    else:
        pay = zaman * oran
        #print("Returning, pay")
        return pay

zaman = input("Enter Hours: ")
oran =input("Enter Rate: ")
zaman = float(zaman)
oran = float(oran)

xp = computepay(zaman,oran)
print("Pay:", xp)