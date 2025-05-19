# Mevcut günlük girişlerini dosyadan okuma
try:
    with open('diary.txt', 'r') as file:
        entries = file.readlines()
except FileNotFoundError:
    entries = []

# Kullanıcıya günlük işlemleri için seçenekler sunma
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = input("Function: ")

    if function == '1':
        # Günlük girişi ekleme
        diary_entry = input("Diary entry: ")
        with open('diary.txt', 'a') as file:
            file.write(diary_entry + '\n')  # Girişi dosyaya ekle
        print("Diary saved")

    elif function == '2':
        # Günlük girişlerini okuma
        print("Entries:")
        for entry in entries:
            print(entry.strip())  # Girişleri yazdır

    elif function == '0':
        # Programdan çıkma
        print("Bye now!")
        break

    else:
        print("Invalid option, please try again.")