import numpy as np
residue26 = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19,
             15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}


def toNum(x):
    return 0 if x == 'Z' else ord(x) - 64


def toChar(i):
    return chr(int(i) % 26 + 64)


def mod26(x):
    if (x >= 0):
        return x % 26
    else:
        return 26 - (abs(x) % 26)


def fix(x):
    if len(x) % 2 != 0:
        return x + x[len(x) - 1]
    return x


def ciphering(plaintext, m):
    plaintext = plaintext.upper()
    cipher = [toNum(i) for i in plaintext]
    cipherTextPlaceholder = []

    for i in range(int(len(cipher) / 2)):
        tempArr = np.zeros((2, 1), dtype=int)
        tempArr[0] = cipher[i*2]
        tempArr[1] = cipher[i * 2 + 1]
        resultArr = np.dot(m, tempArr)
        print(m)
        print('*')
        print(tempArr)
        print('=')
        print(resultArr)
        print('///')
        cipherTextPlaceholder.append(toChar(resultArr[0]))
        cipherTextPlaceholder.append(toChar(resultArr[1]))

    ciphertext = ''.join(x for x in cipherTextPlaceholder)
    return ciphertext


def deciphering(ciphertext, m):
    decipher = [toNum(x) for x in ciphertext]
    plaintextPlaceholder = []
    det = int(np.linalg.det(m))
    inv_m = np.zeros((2, 2), dtype=int)

    inv_m[0][0], inv_m[1][1] = m[1][1], m[0][0]
    inv_m[0][1], inv_m[1][0] = -m[0][1], -m[1][0]

    inv_m = residue26[det] * inv_m

    it = np.nditer(inv_m, flags=['multi_index'])

    for x in it:
        inv_m[it.multi_index[0]][it.multi_index[1]] = mod26(
            inv_m[it.multi_index[0]][it.multi_index[1]])

    for i in range(int(len(decipher) / 2)):
        tempArr = np.zeros((2, 1), dtype=int)
        tempArr[0] = decipher[i*2]
        tempArr[1] = decipher[i * 2 + 1]
        resultArr = np.dot(inv_m, tempArr)
        print(inv_m)
        print('*')
        print(tempArr)
        print('=')
        print(resultArr)
        print('///')
        plaintextPlaceholder.append(toChar(resultArr[0]))
        plaintextPlaceholder.append(toChar(resultArr[1]))

    plaintext = ''.join(x for x in plaintextPlaceholder)
    return plaintext


m = np.zeros((2, 2))
detm = np.linalg.det(m)
while (detm not in residue26):
    print("Please enter 4 number to define the cipher matrix that has det associated with a residue: ")
    a, b, c, d = input().split()
    m = np.array([[a, b], [c, d]], dtype=int)
    detm = np.linalg.det(m)
    print("matrix's det: {}".format(detm))

plaintext = input("Please input the plaintext to cipher: ")
plaintext = fix(plaintext)

print("Ciphering:")
cipher = ciphering(plaintext, m)
print("Deciphering:")
plaintext = deciphering(cipher, m)

print("Cipher: {}".format(cipher))
print("Plaintext: {}".format(plaintext))
