def toBinary(string):
    binary = ''
    for character in string:
        binary = binary + bin(ord(character))[2:].zfill(8) + ' '
    return binary.strip()


print(toBinary(input('Enter text: ')))
