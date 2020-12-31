import re
from .corpus_loader import word_list, name_list

def encrypt(text, shift):
    output = ''
    lower_floor = ord('a')
    upper_floor = ord('A')

    for char in text:
        num = ord(char)

        if lower_floor <= num <= (lower_floor + 26):
            base = lower_floor
        elif upper_floor <= num <= (upper_floor + 26):
            base = upper_floor
        else:
            base = None

        if base:
            num -= base
            num = (num + shift) % 26
            num += base
        output += chr(num)
    return output.strip()


def decrypt(text, shift):
  return encrypt(text, -shift)


def _estimate_if_phrase_is_real(phrase):
    words = phrase.split(' ')

    actual_words = 0

    for word in words:
        word.lower()
        if word in word_list or word in name_list:
            actual_words += 1

    return actual_words / len(words)


def crack(text, threshold=.5):
    best_phrase = ['', threshold]

    for i in range(0, 26):
        phrase = decrypt(text, i)

        realness =  _estimate_if_phrase_is_real(phrase)
        if realness >= best_phrase[1]:
            best_phrase[0] = phrase
            best_phrase[1] = realness
    
    return best_phrase[0]