def word_counter(word):
    words_list = word.split()
    word_counter = {}

    for word in words_list:
        word = word.lower()

        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1

    sum_word_number = len(words_list)

    print("Toplam kelime sayısı:", sum_word_number)
    print("Kelime sayıları: ")
    for word, number in word_counter.items():
        print(f"{word}: {number}")

text = input("Bir metin girin: ")
word_counter(text)




