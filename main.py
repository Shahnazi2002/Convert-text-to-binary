def toBinary(string):
    result = ''
    for character in string:
        if character == ' ':
            result = result + ' '
        elif character == '.':
            result = result + '.'
        else:
            result = result + bin(ord(character))[2:].zfill(8) + ' '
    return result.strip()


print(toBinary(input('Enter text: ')))