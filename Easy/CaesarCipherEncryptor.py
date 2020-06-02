#Method-1(With Builtin Function) Time - O(N) | Space - O(N)

def caesarCipherEncryptor(string,key):
    newKey = key % 26
    newString = []
    for letter in string:
        newString.append(getNewLetter(letter, newKey))

    return "".join(newString)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr( 96 + newLetterCode % 122 )

# Method-2(Without Builtin Function) Time - O(N) | Space - O(N)

def caesarCipherEncryptor(string,key):
    newKey = key % 26
    newString = []
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newString.append(getNewLetter(letter, newKey, alphabet))

    return "".join(newString)

def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1+newLetterCode%25]