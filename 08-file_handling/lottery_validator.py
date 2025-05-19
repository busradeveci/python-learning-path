def filter_incorrect():
    correct_lines = []  # Doğru satırları tutacak liste

    # Orijinal dosyayı okuma
    with open('lottery_numbers.csv', 'r') as file:
        for line in file:
            line = line.strip()  # Satırdaki boşlukları temizle
            if validate_line(line):  # Satırı doğrula
                correct_lines.append(line)  # Doğru satırı listeye ekle

    # Doğru satırları yeni dosyaya yazma
    with open('correct_numbers.csv', 'w') as file:
        for correct_line in correct_lines:
            file.write(correct_line + '\n')  # Her satırı yeni dosyaya yaz

def validate_line(line: str) -> bool:
    # Satırı parçalara ayır
    parts = line.split(';')
    if len(parts) != 2:
        return False  # Yanlış format

    week_part, numbers_part = parts
    # Hafta numarasını kontrol et
    if not week_part.startswith('week ') or not week_part[5:].isdigit():
        return False

    week_number = int(week_part[5:])
    if week_number < 1 or week_number > 52:  # Hafta numarası 1-52 arasında olmalı
        return False

    # Sayıları kontrol et
    numbers = numbers_part.split(',')
    if len(numbers) != 7:  # Tam olarak 7 sayı olmalı
        return False

    seen_numbers = set()  # Tekrar eden sayıları kontrol etmek için set
    for number in numbers:
        try:
            num = int(number)  # Sayıyı tam sayıya çevir
            if num < 1 or num > 39:  # Sayı 1-39 arasında olmalı
                return False
            if num in seen_numbers:  # Aynı sayı iki kez var mı?
                return False
            seen_numbers.add(num)  # Sayıyı set'e ekle
        except ValueError:
            return False  # Sayıya dönüştürülemedi

    return True  # Tüm kontroller geçildi

# Ana program bloğu
if __name__ == "__main__":
    filter_incorrect()
