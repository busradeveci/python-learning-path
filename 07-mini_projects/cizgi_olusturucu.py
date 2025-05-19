def line(lenght, character):
    if character == "":
        character = "*"
    else:
        character = character[0]
    output = character * lenght
    print(output)

if __name__ == "__main__":
    line(7, "%")
    line(10, "#")
