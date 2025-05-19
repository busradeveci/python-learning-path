def find_allowed(wordlist, minimum):
    allowed_letters = "aeiouy"
    result = []

    for word in wordlist:
        count = sum(1 for char in word if char in allowed_letters)

    if count >= minimum:
        result.append(word)

    return result

wordlist = ["apple", "banana", "cherry", "date", "elderberry"]
minimum = 3
result = find_allowed(wordlist, minimum)
print(result)