from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii


def example():
    message = b'Encrypt'
    key = get_random_bytes(16)
    ciphertext = aes_encrypt_ctr(key, message)
    print(f'Encrypted Text is: ', pretty_hex(ciphertext), '\n')
    pad_value = aes_pad_check(key, ciphertext)
    attacker_decrypt(key, ciphertext, pad_value)


def aes_encrypt_ctr(k, text):
    nonce = b'0000'
    e_cipher = AES.new(k, AES.MODE_CTR, nonce=nonce)
    c = e_cipher.encrypt(pad(text, 16))
    return c


def aes_decrypt_ctr(k, code):
    nonce = b'0000'
    d_cipher = AES.new(k, AES.MODE_CTR, nonce=nonce)
    d = unpad(d_cipher.decrypt(code), 16)
    return d


def aes_pad_check(k, code):
    nonce = b'0000'
    i = 0
    while i < len(code):
        try:
            code2 = pretty_hex(code)
            sample = string_to_list(code2, 2)
            sample[i] = '00'
            code3 = ''.join(sample)
            code3 = binascii.unhexlify(code3)
            print(f'Ciphertext check : ', pretty_hex(code3))
            d_cipher = AES.new(k, AES.MODE_CTR, nonce=nonce)
            unpad(d_cipher.decrypt(code3), 16)
            print(f'{int(len(code3) - i)} is not the padding length\n')
            i += 1
        except ValueError:
            value = int(len(code) - i)
            print('Length of Pad found!\n')
            print(f'The padding length is : ', value)
            print(f'The message length is:', i, '\n')
            break
    return value


def attacker_decrypt(k, code, check):
    print('DECRYPTION ATTACK STARTING NOW!\n')
    nonce = b'0000'
    i = len(code) - check
    code2 = pretty_hex(code)
    new_plaintext = ['00'] * i + ['{:02x}'.format(check)] * check
    sample = string_to_list(code2, 2)
    sample2 = [int(x, 16) for x in sample]
    print(f'Current plaintext is : ', ''.join(new_plaintext))
    while i > 0:
        for z in range(i-1, len(sample)):
            sample2[z] = sample2[z] ^ check ^ (check + 1)
        new_c = ['{:02x}'.format(g) for g in sample2]
        print(f'New Ciphertext is : ', ''.join(new_c).upper(), '\n')
        for j in range(0, 256):
            try:
                sample2[i-1] = j
                sample3 = ['{:02x}'.format(y) for y in sample2]
                test = ''.join(sample3).upper()
                test = binascii.unhexlify(test)
                d_cipher = (AES.new(k, AES.MODE_CTR, nonce=nonce))
                unpad(d_cipher.decrypt(test), 16)
            except ValueError:
                continue
            else:
                m = hex((int((check + 1) ^ j ^ int(sample[i - 1], 16))))
                sample2[i - 1] = j
                new_plaintext[i - 1] = m[2:]
                print(f'Current plaintext is : ', ''.join(new_plaintext).upper())
                break
        i -= 1
        check += 1


def string_to_list(s, n):
    l = []
    for j in range(0, len(s), n):
        l.append(s[j:j + n])
    return l


def pretty_hex(c):
    c = binascii.hexlify(c).upper().decode()
    return c


if __name__ == "__main__":
    example()
