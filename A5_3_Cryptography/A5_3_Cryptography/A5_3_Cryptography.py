## Cryptography

input = raw_input('Enter some text to encrypt: ')
shift = raw_input('Enter a number: ')

shift = int(shift)%26

if len(input) > 0:
    print shift