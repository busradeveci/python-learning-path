n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1


#ard arda stringleri yazdıran kod.
word = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))
word *= amount
print(word)