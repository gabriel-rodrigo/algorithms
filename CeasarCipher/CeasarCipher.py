def ciphertext(text=''):
    # Guard translated letters
    new_word = []

    for word in text:
        for letter in word:
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

    for word in text:
        for letter in word:
            # If letter is space append space
            # Else append letter deciphered letter
            if ord(letter) == 32:
                new_word.append(' ')
            else:
                new_word.append(chr(ord(letter)-3))
    
    # Join deciphered letters to return as string
    print('in : ' + text)
    print('out: ' + ''.join(new_word))



ciphertext('gabriel rodrigo')
print()
deciphertext('jdeulho urguljr')