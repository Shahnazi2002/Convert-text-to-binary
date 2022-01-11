def toBinary(string):
    result = ''
    for character in string:
        result = result + bin(ord(character))[2:].zfill(8) + ' '
    return result.strip()


print(toBinary(input('Enter text: ')))
