# Python3.6  
# Coding: utf-8  
import math
# Création d'une fonction définie par l'utilisateur
def getDoubleAlphabet(alphabet):
   doubleAlphabet = alphabet + alphabet
   return doubleAlphabet
# Chiffrement d'un message
def getMessage():
   stringToEncrypt = input("Please enter a message to encrypt: ")
   return stringToEncrypt
# Recupération d'une clé de chiffrement
def getCipherKey():
   shiftAmount = input( "Please enter a key (whole number from 1-25): ")
   return shiftAmount

""" 1. Take three arguments: the message, the cipherKey, and the alphabet.

    2. Initialize variables.

    3. Use a `for` loop to traverse each letter in the message.

    4. For a specific letter, find the position.

    5. For a specific letter, determine the new position given the cipher key.

    6. If current letter is in the alphabet, append the new letter to the encrypted message.

    7. If current letter is not in the alphabet, append the current letter.

    8. Return the encrypted message after exhausting all the letters in the message.
"""
# Chiffrement d'un message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

