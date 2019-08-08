def ciphertext(text=''):
    # Guard translated letters
    new_word = []

    for letter in text:
        # If letter is space append space
        # Else append letter ciphered letter
        if ord(letter) == 32:
            new_word.append(' ')
        else:
            new_word.append(chr(ord(letter)+3))
    
    # Join ciphered letters to return as string
    print('in : ' + text)
    print('out: ' + ''.join(new_word))

def deciphertext(text=''):
    # Guard translated letters
    new_word = []

    for letter in text:
        # If letter is space append space
        # Else append letter deciphered letter
        if ord(letter) == 32:
            new_word.append(' ')
        else:
            new_word.append(chr(ord(letter)-3))
    
    # Join deciphered letters to return as string
    print('in : ' + text)
    print('out: ' + ''.join(new_word))



ciphertext('gabriel rodrigo da costa silva')
print()
ciphertext('Gabriel Rodrigo da Costa Silva')
print()
ciphertext('GABRIEL RODRIGO DA COSTA SILVA')
print()
deciphertext('jdeulho urguljr')