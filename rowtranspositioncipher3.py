import math
import numpy as np

plain = input("Enter plaintext): ").lower().replace(" ", "") #to get rid of empty spaces and capital letters
key=input("Enter key: ").lower().replace(" ", "") 

len_key = len(key)
len_plain = len(plain)
row = int(math.ceil(len_plain / len_key))
matrix = [ ['X']*len_key for i in range(row) ]


#ENCRYPTION
t = 0
for r in range(row):
  for c,ch in enumerate(plain[t : t+ len_key]):
    matrix[r][c] = ch
  t += len_key

sort_order = sorted([(ch,i) for i,ch in enumerate(key)])  #to make alphabetically order of chars

cipher = ''
for ch,c in sort_order:
  for r in range(row):
    cipher += matrix[r][c]
  
print("Encryption")
print("Plaintext is :",plain)
print("Ciphertext is:",cipher)

# DECRYPTION
matrix_new = [ ['X']*len_key for i in range(row) ]
key_order = [ key.index(ch) for ch in sorted(list(key))]  #to make original key order when we know keyword

t = 0
for c in key_order:
  for r,ch in enumerate(cipher[t : t+ row]):
    matrix_new[r][c] = ch
  t += row

p_text = ''
for r in range(row):
  for c in range(len_key):
    p_text += matrix_new[r][c] if matrix_new[r][c] != 'X' else ''

print("Decryption")
print("Cipher text is:",cipher)
print("Plain text is :",p_text)
