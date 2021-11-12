# def hash(text):
#   """ Ushbu funksiya matnlar uzunligini beradi """
#   return len(text)

# print(hash("Azamat"))  

import string

alphabet = list(string.ascii_lowercase)
# Pythondagi tayyor lotin alifbosi

def hash_func(text):
  """ Ushbu funksiya matnning  harfini index sifatida qaytaradi """
  return alphabet.index(text[0].lower())

print(hash_func("Darslik")) 
print(hash_func("Azamat")) 