#fstring print kısmında daha kullanışlı yazmak için kullandığımız ifadedir.f ile başlar.
name = "Mark"
age = 37
city = "Palo Alto"
print(f"Hi {name}, you are {age} years old. You live in {city}.")

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old")
print("")
print("my skills are")
print(f" - {skill1} ({level1}) ")
print(f" - {skill2} ({level2}) ")
print(f" - {skill3} ({level3})\n ")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

# Write your solution here
x = 27
y = 15
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

# Write your solution here
number = int(input("Enter a number: "))
result = number * 5
print(f"{number} times 5 is {result}")

# Write your solution here
name = input("What is your name? ")
year = int(input("Which year were you born? "))
birth_day = year
current_year = 2021
age = current_year - birth_day
print(f"Hi {name}, you will be {age} years old at the end of the year {current_year}")

# Write your solution here
days = int(input("How many days? "))
second = 86400
sum = days * second
print(f"Seconds in that many days: {sum}")

# Fix the code (düzelttin number1 number2 number3 diye)

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = number1 * number2 * number3
print(f"The product is {product} ")

# Write your solution here
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
number3 = float(input("Enter a number: "))
number4 = float(input("Enter a number: "))
total_sum = number1 + number2 + number3 + number4
mean = total_sum / 4
print(f"The sum of the numbers is {int(total_sum)} and the mean is {mean}")

# Write your solution here
# Kullanıcıdan bilgileri al
cafeteria_visits = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery_expense = float(input("How much money do you spend on groceries in a week? "))

# Haftalık kafeterya harcamasını hesapla
cafeteria_expense = cafeteria_visits * lunch_price

# Toplam haftalık harcamayı hesapla
total_weekly_expense = cafeteria_expense + grocery_expense

# Günlük harcamayı hesapla
daily_expense = total_weekly_expense / 7

# Sonuçları yazdır
print(f"Average food expenditure:")
print(f"Daily:{daily_expense: } euros")
print(f"Weekly:{total_weekly_expense: } euros")

# bir grup oluşturma kodu öğrencilerin kaç tane grup oluşturacağı ile ilgili.
total_student = int(input("How many studenst on the course? "))
group_size = int(input("Desired group size? "))
number_groups = total_student // group_size
remaining_students = total_student % group_size
if remaining_students > 0:
    number_groups += 1
print(f"Number of groups formed: {number_groups}")

#mutlak değerli hesaplama negatif sayıları pozitife çeviriyor mutlak değer.
number = int(input("Please type in a number:"))
result = 0
if number > 0:
    result = number
if number < 0 :
    result = number * -1

print(f"The absolute value of this number is {result}")


#Jerrye sormaması lazım!!! o haricinde diğer isimlere soruyu devam ettirmek için if'in içinde input sorusuna devam ettirdik.
name = input("Please tell me your name: ")
portions_soup1 = 5.90
if name != "Jerry":
    portions_soup = int(input("How many portions of soup? "))
    total_portions_soup = portions_soup * 5.90
    print(f"The total cost is {total_portions_soup}")
if name == "Jerry":
    print()

print("Next please!")

#Lütfen kullanıcıdan bir tamsayı numarası isteyen bir program yazın.örneklere göre büyüklüğünü yazdırdık.
number = int(input("Please type in a number:"))
if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")
print("Thank you!")

#hesap makinesi 3 (if ve boolean ile)
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operation = input("add: + , multiply: * , subtract: - ")
is_valid_operation = False
result = 0
if operation == "add":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    is_valid_operation = True
if operation == "multiply":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    is_valid_operation = True

if operation == "subtract":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    is_valid_operation = True

#fahrenayt ve santigrat hesaplama:
fahrenheit = int(input("Please type in a temperature (F): "))
celsius = (5/9) * (fahrenheit - 32)
print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")


# Kullanıcıdan saatlik ücreti al
hourly_wage = float(input("Hourly wage: "))

# Kullanıcıdan çalışılan saat sayısını al
hours_worked = float(input("Hours worked: "))

# Kullanıcıdan haftanın gününü al
day_of_week = input("Day of the week: ")

# Günlük ücreti hesapla
if day_of_week.lower() == "sunday":
    daily_wages = hourly_wage * hours_worked * 2  # Pazar günü saatlik ücret iki kat
else:
    daily_wages = hourly_wage * hours_worked  # Diğer günlerde normal ücret

# Sonucu yazdır
print(f"Daily wages: {daily_wages} euros")

# Kullanıcıdan hava durumu tahmini için sıcaklık değerini al
temperature = float(input("What is the weather forecast for tomorrow?\nTemperature: "))

# Kullanıcıdan yağmur durumu bilgisini al
rain = input("Will it rain (yes/no): ").strip().lower()

# Kıyafet önerileri
if temperature > 20:
    print("Wear jeans and a T-shirt")
elif temperature > 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
elif temperature > 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
else:  # temperature <= 5
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

# Yağmur durumu kontrolü
if rain == "yes":
    print("Don't forget your umbrella!")

# diskriminat hesaplama kodu
# Kullanımdaki matematik modülünün karekökünü alalım
from math import sqrt

# Kullanıcıdan a, b ve c değerlerini al
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

# Diskriminantı hesapla
discriminant = b**2 - 4*a*c

# Kökleri hesapla
first_root = (-b + sqrt(discriminant)) / (2*a)
second_root = (-b - sqrt(discriminant)) / (2*a)

# Sonuçları yazdır
print(f"The roots are {first_root} and {second_root}")

#Number of characters, kelimeler kaç tane var onu sayma, len(word) değeriyle.
# Kullanıcıdan bir kelime al
word = input("Please type in a word: ")

# Kelimenin uzunluğunu hesapla
length = len(word)

# Eğer kelimenin uzunluğu 1'den fazla ise, karakter sayısını yazdır
if length > 1:
    print(f"There are {length} letters in the word {word}")

# Her durumda teşekkür mesajı yazdır
print("Thank you!")

#float integer çevirerek yaz float olan kalacak şekilde yaz.
number = float(input("Please type in a number: "))
print("Integer part:", int(number))
Decimal_part = number - int(number)  #(float yapma işlemidir.) Sayının ondalık kısmını bulmak için, sayının kendisinden tam sayı kısmını çıkarıyoruz.
print("Decimal part:", Decimal_part )  #(float yapma işlemi için.) Sayının tam kısmını çıkardığınızda, geriye kalan kısım ondalık kısımdır.

#reşit olup olmadığını soran if-else kodu.
person = int(input("How old are you? "))
legal_age = 18
if person >= 18 :
    print(f"You are of age!")
else :
    print(f"You are not of age!")

# Kullanıcıdan iki tam sayı al
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in another number: "))

# Sayıları karşılaştır
if number1 > number2:
    print(f"The greater number was: {number1}")
elif number2 > number1:
    print(f"The greater number was: {number2}")
else:
    print("The numbers are equal!")

#hangilerinin yaşı büyük ya da eşit if-else kodu
name1 = input("Name: ")
age1 = int(input("Age: "))
name2 = input("Name: ")
age2 = int(input("Age: "))
if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")
print("Person 1: ")
print("Person 2: ")

#alfabetik olarak a-z ya da A-Z ye kadar ingiliz alfabesi kullanılır, hangisi alfabetik olarak en sonra geliyorsa onu yazdırıyor.
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")
if word1 > word2 :
    print(f"{word1} comes alphabetically last.")
elif word1 < word2:
    print(f"{word2} comes alphabetically last.")
else:
    print(f"You gave the same word twice.")
#karşılaştırılan karakterler aynı büyük/küçük harftir, yani hem BÜYÜK HARF ister her ikisi de küçük harftir.


# Kullanıcıdan yaşını sor
age = input("What is your age? ")

# Yaşı sayıya dönüştürmeye çalış
try:
    age = int(age)

    # Yaş kontrolü
    if age < 0:
        print("That must be a mistake.")
    elif age < 5:
        print("I suspect you can't write quite yet...")
    else:
        print(f"Ok, you're {age} years old.")
except ValueError:
    print("Please enter a valid number for your age.")

#if-else kuralları in and or kelime kullanımı liste oluşturarak gruplaştırdık.
name = input("Please type in your name: ")
valid_names = ["Huey", "Dewey", "Louie"]
valid_names1 = ["Morty", "Ferdie"]
if name in valid_names:
    print(f"I think you might be one of Donald Duck's nephews.")
elif name in valid_names1:
    print(f"I think you might be one of Mickey Mouse's nephews.")
else:
    print(f"You're not a nephew of any character I know of.")

#NOT ORTALAMASI HESAPLAMA İF-ELİF-ELSE kuralı and or is mantıksal operatörlerin kullanımı.
#Girintilere Dikkat Et, eşitler mi değiller mi diye!!
points = int(input("How many points: "))
if points < 0 or points > 100:
    print(f"Grade: impossible!")
elif points >= 0 and points <= 49:
    print(f"Grade: fail")
elif points >= 50 and points <= 59:
    print(f"Grade: 1")
elif points >= 60 and points <= 69:
    print(f"Grade: 2")
elif points >= 70 and points <= 79:
    print(f"Grade: 3")
elif points >= 80 and points <= 89:
    print(f"Grade: 4")
elif points >= 90 and points <= 100:
    print(f"Grade: 5")

#koşul sırasına dikkat et ilk hangisi doğruysa onu yazdırıyor çünkü.
number = int(input("Number: "))
if (number % 3 == 0) and (number % 5 == 0):
    print(f"FizzBuzz")
elif number % 5 == 0:
    print(f"Buzz")
elif number % 3 == 0:
    print(f"Fizz")
else:
    print()

#artık yıl hesaplaması 4 yılda bir şubat 29 çektiği için. sıralama önemli lütfen kavra.
year = int(input("Please type in a year: "))
if year % 400 == 0:
    print(f"That year is a leap year.")
elif year % 100 == 0:
    print(f"That year is not a leap year.")
elif year % 4 == 0:
    print(f"That year is a leap year.")
else:
    print(f"That year is not a leap year.")

#ALFABETİK SIRAYA KOYMA HARFLERİ. KODUMUZ sort() KULLANIYORUZ.
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
letters = [letter1, letter2, letter3]
letters.sort()
middle_letter = letters[1]
print(f"The letter in the middle is {middle_letter}")

#Evet, Python'da else ifadesinin içine if ve elif ifadeleri yazabilirsiniz. Bu yapıya "iç içe koşullu ifadeler" denir.
gift = float(input("Value of gift: "))
if gift < 5000:
    print("No tax")  # Vergi yoksa bu mesajı yazdır
else:
    if 5000 <= gift < 25000:
        tax = 100 + (gift - 5000) * 0.08
    elif 25000 <= gift < 55000:
        tax = 1700 + (gift - 25000) * 0.10
    elif 55000 <= gift < 200000:
        tax = 4700 + (gift - 55000) * 0.12
    elif 200000 <= gift < 1000000:
        tax = 22100 + (gift - 200000) * 0.15
    else:  # 1,000,000 € ve üzeri
        tax = 142100 + (gift - 1000000) * 0.17

    print(f"Amount of tax: {tax} euros")  # Vergi varsa bu mesajı yazdır

#while treu döngüsü while döngüsünden nasıl çıkılır nasıl duraklatılır kodu.
    while True:
        print("hi")
        response = input("Shall we continue? ")
        if response.lower() == "no":
            print("okay then")
            break
 #karekök hesaplama while döngüsünde floatlar kullandık. math import sqrt(karekök için)formüller kullandık.
from math import sqrt
# Write your solution here
while True:
    number = float(input("Please type in a number: "))
    if number < 0:
        print("Invalid number")
    elif number == 0:
        print("Exiting...")
        break
    else:
        root = sqrt(number)
        print(f"{root:.1f}")  # .1f yazdığımızda int floata çeviriyor ondalıklı sayı yapıyor.

#while döngüsü 54321 diye yazdırma işlemi. while veya for döngüsünü kullanabiliriz.
number = 5
print("Countdown!")
while number > 0:  # 0'dan büyük olduğu sürece döngü devam eder
    print(number)  # Her döngüde number'ı yazdır
    number = number - 1  # number'ı 1 azalt
print("Now!")  # Döngü sona erdiğinde çalışır



# kullanıcıdan parola istiyor ve o parolayı saklayıp parola doğru yazdırana kadar döngüyü devam ettiriyor.
password = input("Password: ")

# Keep asking the user to retype the password until it matches the first one
while True:
    repeat_password = input("Repeat password: ")
    if repeat_password == password:
        print("User account created!")
        break  # Exit the loop when the password matches
    else:
        print("They do not match!")

# Doğru PIN kodunu tanımla kodu.
correct_pin = "4321"
# Giriş sayısını başlatır.
attempts = 0

while True:
    # Kullanıcıdan PIN kodunu al
    pin = input("PIN: ")
    # Giriş sayısını artırır.
    attempts += 1

    # Kullanıcının girdiği PIN kodunu kontrol et
    if pin == correct_pin:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break  # Döngüden çıkmak için.
    else:
        print("Wrong")  # Yanlış PIN mesajıdır. en son yazılır.
#basit while döngüsü 2'şer giden 30'a kadar olan kod.
number = 2
while number < 30:
    print(number)
    number += 2
print(number)

#while döngüsü ard arda yazdırma kodu.
print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number = number - 1
print("Now!")


# Kullanıcıdan bir üst sınır al sınır yani sayı 5 mesela 5 hariç diğerlerini yazdıracak "1234" while döngü kodu.
upper_limit = int(input("Upper limit: "))  # Örneğin 5

# Başlangıç değeri
i = 1

# 1'den upper_limit - 1'e kadar olan sayıları yazdır
while i < upper_limit:
    print(i)
    i += 1  # i'yi bir artır



#upper limit 1 den başlayarak 2'şer çıkan count sayaç demek yazdığı sayıya kadar yazdıran while döngü.
upper_limit = int(input("Upper limit: "))
current_number = 1
count = 0
while count < upper_limit:
    print(current_number)
    current_number *= 2
    count = current_number
print(f"Upper limit: {upper_limit}")



#upper limit yine yukarıdaki gibi aynı fakat bu sefer base soruyoruz kaç kat olması gerektiğini. while döngüsü.
upper_limit = int(input("Upper limit: "))
base = int(input("Base: "))
current_number = 1
count = 0
while count <= upper_limit:
    print(current_number)
    current_number *= base
    count = current_number


#Ardışık sayıların toplamı, sürüm 1
limit = int( input("Limit: "))
total = 0
counter = 1
while total < limit:
    total += counter
    counter += 1
print(total)


