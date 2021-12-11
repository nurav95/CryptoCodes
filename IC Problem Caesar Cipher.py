import collections


def decrypt(v, w):
    plaintext = ''
    for x in range(len(v)):
        z = v[x]
        plaintext += chr((ord(z) + w - 65) % 26 + 65)
    return plaintext


def IC_1():
    pi = {'A': 0.082, 'B': 0.015,
          'C': 0.028, 'D': 0.043,
          'E': 0.127, 'F': 0.022,
          'G': 0.020, 'H': 0.061,
          'I': 0.070, 'J': 0.002,
          'K': 0.008, 'L': 0.040,
          'M': 0.024, 'N': 0.067,
          'O': 0.075, 'P': 0.019,
          'Q': 0.001, 'R': 0.060,
          'S': 0.063, 'T': 0.091,
          'U': 0.028, 'V': 0.010,
          'W': 0.023, 'X': 0.001,
          'Y': 0.020, 'Z': 0.001}
    return pi


def check():
    ciphertext = 'ZQHQDQHQDGEQFTQETURFOUBTQDMXSADUFTYIQMDQXQMDZUZSMNAGFUFNQOMGEQUFUEAZQARFTQOXMEEUOMXOUBTQDEUFUEMXEAMZUOQMBBXUOMFUAZARFTQYAPGXAMDUFTYQFUOFTQADK'
    length = len(ciphertext)
    prob = IC_1()
    frequency = collections.Counter(ciphertext)

    for test in range(0, 26):
        IC = 0.0
        for letter in range(0, 26):
            a = chr(65 + letter)
            b = chr(65 + (test + letter) % 26)
            print(a, b)
            prob2 = float(frequency[b]/length)
            IC += prob[a]*prob2
            print(IC)
        print(IC)
        if IC >= 0.064:
            key = ord(a) - ord(b)
            print(f'IC is: ', IC)
            print(f'Key is: {chr(test + 65)} : {test}')
            print(f'Plaintext is:', decrypt(ciphertext, key))


if __name__ == '__main__':
    check()