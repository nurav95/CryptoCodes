import collections


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


def decrypt_vignere(k, c2):
    encrypted = ""
    for p in range(len(c2)):
        z = (ord(k[p]) - 65) % 26
        encrypted += chr((ord(c2[p]) - z - 65) % 26 + 65)
    return encrypted


def check(c):
    prob = IC_1()
    key_text = ""
    key_dict = {}
    check_length = 0
    for key_length in range(0, 26):
        IC = 0.0
        frequency = collections.Counter(c)
        if key_length == 0:
            for letter in range(0, 26):
                a = chr(65 + letter)
                length = len(c)
                prob2 = float(frequency[a] / length)
                IC += prob[a] * prob2
                if IC > 0.064:
                    print(f'The text is not encrypted.')
                else:
                    pass
        elif key_length == 1:
            for test in range(0, 26):
                IC = 0.0
                for letter in range(0, 26):
                    a = chr(65 + letter)
                    length = len(c)
                    b = chr(65 + (test + letter) % 26)
                    prob2 = float(frequency[b] / length)
                    IC += prob[a] * prob2
                if IC > 0.060:
                    print(f'IC is: ', IC)
                    key = chr(test + 65)
                    print(f'Key is:', key)
                    key_text = key
                else:
                    pass
        else:
            for chosen in range(0, key_length):
                stream = ""
                stream += c[chosen::key_length]
                frequency = collections.Counter(stream)
                for test in range(0, 26):
                    IC = 0.0
                    for letter in range(0, 26):
                        a = chr(65 + letter)
                        length = len(stream)
                        b = chr(65 + (test + letter) % 26)
                        prob2 = float(frequency[b] / length)
                        IC += prob[a] * prob2
                    if IC > 0.058:
                        key = chr(test + 65)
                        key_dict[check_length] = {'IC': IC, 'Key': key, 'Stream': stream}
                        check_length += 1
                    else:
                        pass
                    chosen += 1
            if check_length == key_length:
                for variable in range(0, key_length):
                    print('IC: ', key_dict[variable]['IC'])
                    print('Key: ', key_dict[variable]['Key'])
                    print('Stream: ', key_dict[variable]['Stream'], '\n')
                    key_text += key_dict[variable]['Key']
                check_length = 0
            else:
                check_length = 0

    print(f'Key is : ', key_text)
    print(f'Length of key is : ', len(key_text))
    if key_text == '':
        pass
    elif len(key_text) == len(c):
        key_text = key_text
    else:
        for i in range(len(c) - len(key_text)):
            key_text += key_text[i % len(key_text)]
        print(f'Key stream is :', key_text)

    plaintext = decrypt_vignere(key_text, c)
    print('Plaintext is : ', plaintext)


if __name__ == '__main__':
    ciphertext = 'TWTLPMDCOXRTTHESXCEINIPEMVTQWSSHDXXHTSLCSLTCILDCRIRDUEINTCOMNVLTXHBPRRIUXNINITGINXCRWOURZVRJVLXESETRKHZTISIWPLUCITRGHTLWOCLLWOKTCAIIWSSUCSDENSVFRSEJEEWPNQSRHXIQOCISWTWTGMNTNLVDHLPVEQJDCAVPTRAHISIWTAWSRVPYMZTSQERBTCWTGTLXESISIIGKTREHPYHTWTXSRTALGKPSLMSXRLPNTXRLBDGDLUGGTIDIDOSTWTAVUCXYKTWTJWHDJWHHPKPHOCTTRNDKPQBTG'
    check(ciphertext)
