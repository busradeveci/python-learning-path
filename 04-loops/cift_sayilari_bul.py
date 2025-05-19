def find_even_numbers(liste):
    result_list = []   #sonuç listesi oluştur
    for members in liste:  #listeyi döngü ile gez
        if members %2 == 0:  #elemanı kontrol et
            result_list.append(members)  #çiftse sonuç listesine ekle
    return result_list      #sonuç listesini döndür

#örnek kullanım
input_list = [1, 2, 3, 4, 5, 6, 7, 10, 15, 17, 16, 18, 20, 24, 8, 26, 32, 36, 11, 12]
double_numbers = find_even_numbers(input_list)
print(f"Çift sayılar:", double_numbers)









