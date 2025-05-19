#basit bir for döngüsü kodu mantığı
for i in [5,4,3,2,1]:
    print(i)
print("Done!")

friends = ["Büşra ,Beyza ,Hilal"]
for friend in friends:
    print("Happy Birthday:", friends)
print("Done")

#aralarında en büyük sayıyı bulmak için for döngüsü kod
largest_so_far = -1
print("Before:", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
        print(largest_so_far, the_num)
print("After:", largest_so_far)

#sıfırdan başlayarak sayarak sırasıyla yazdırma for döngüsü kodu
zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("After", zork)

#for döngüsü içinde toplama
zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)

#for döngüsüyle bunları basitçe bölerek ortalamayı elde edeceğimiz kod
count = 0
sum = 0
print("Before", count, sum)  #yineleme değişkenidir.
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count) #sonucu 1,2,3,4,5,6 diye saydırdık sonra bunların birbiriyle olan toplamını 6 ya böldürdük. ve çıkan sonuç :)

#for döngüsünde bir değer yaptığımız şey de aramak, avlamaktır.mesela bir sayının bir sayıdan büyük değerler arıyorsunudr vs.vs.vs.
print("Before")
for value in [9, 41, 12, 3, 74, 15]:  #bu döngü bu kodda de 20'den büyük değerleri yazdırdık.
    if value > 20:  #bir for döngüsünün içinde if ifadesi bulundurma kavramıdır.
        print("Large number", value)
print("After")

#for döngüsünde boolean valiable kullanarak arama boolean değişkenini kullanmak. true ya da false.
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:  #for döngüsünde de öyle iki nokta üst üsteyi UNUTMA!!!!
    if value == 3 :  #if ifadelerinde iki nokta üst üsteyi HİÇ UNUTMAA KESİN KOYULACAK !!!!!
        found = True
    print('found', value)  #PRİNTLERDE TIRNAK İŞARETLERİ KESİN KONULACAK, DEĞİŞKEN OLANLARDA BAZILARINA KONULMAYACAK ÖZEL OLARAK YAZDIRACAĞIMIZ ŞEYLERE KOYUYORUZ!!
    print('After', found)   #Girintilere dikkat et!!!

#En küçük değeri bulmak için none kullanarak
smallest = None   #None büyük harfle yazmalısın
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None :  #is eşittir'den daha güçlüdür.
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print("After", smallest)

#basit örnekler for ile:
i = 2
for x in range(i):
  i +=1
  print(i)
  print(i)

for x in range(5):
  print(x)