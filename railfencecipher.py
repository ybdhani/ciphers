import numpy as np

def encrypt(plain : str, depth: int):
    cipher = ""
    rows = {}
    descending = True
    for i in range(depth):
        rows[i] = ""

    currRow = 1

    rows[0] = plain[0]

    for i in range(1, len(plain)):
        if(i%(depth-1) == 0):
            descending = not descending
        
        rows[currRow] += plain[i]

        if(descending):
            currRow += 1
        else:
            currRow -= 1 

    for i in range(depth):
        cipher += rows[i]

    return cipher

def decrypt(cipher: str, depth: int):
    plain = ""
    plainArray = np.empty(len(cipher), dtype=str)
    
    cipherCopy = cipher
    
    for i in range(depth):
        offset = 2 * depth - 2
        currIndex = i
        
        for q in range(2):
            getLetterIndex = 0
            for letter in cipher:
                if(currIndex >= len(cipher) or (i == 0 and q == 1) or  (i == depth-1 and q == 1)):
                    break
                
                plainArray[currIndex] = cipherCopy[getLetterIndex]
                
                if(q==0 and i != 0 and i != depth-1):
                    cipherCopy = cipherCopy[:getLetterIndex] + cipherCopy[getLetterIndex+1:]
                    getLetterIndex += 1
                else:
                    getLetterIndex = 0
                    cipherCopy = cipherCopy[1:]
                currIndex += offset
            
            currIndex = i + 2 * depth - 2 - i*2

    for char in plainArray:
        plain += char
    
    return plain


if __name__ == "__main__":
    cipher = encrypt('meetmeatthecafeatfivepm', 4)
    print(f"Encrypted: {cipher}")
    print(f"Decrypted: {decrypt(cipher, 4)}")
