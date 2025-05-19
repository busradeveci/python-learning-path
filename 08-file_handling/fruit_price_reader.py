def read_fruits() -> dict:
    # Meyve isimleri ve fiyatlarını tutacak bir sözlük
    fruits_dict = {}

    # Dosyayı okuma
    with open('fruits.csv', 'r') as file:
        for line in file:
            # Satırı noktalı virgüle göre ayır
            fruit, price = line.strip().split(';')
            # Fiyatı float türüne çevir ve sözlüğe ekle
            fruits_dict[fruit] = float(price)

    return fruits_dict  # Sözlüğü döndür


# Ana program bloğu
if __name__ == "__main__":
    fruits = read_fruits()
    print(fruits)  # Sözlüğü yazdır