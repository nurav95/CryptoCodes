from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

UID = 117386356
Last_Name = 'Warrier'
First_Name = 'Varun'


def aes_encrypt_ctr(k, text):
    e_cipher = AES.new(k, AES.MODE_ECB)
    c = e_cipher.encrypt(pad(text, 16))
    return c


def aes_input_av_test(plaintext, key, bit_list):
    new_list = []
    count = 0
    ciphertext = aes_encrypt_ctr(key, plaintext)
    bit_cipher = ''.join(format(ord(m), '08b') for m in str(ciphertext.decode('ISO-8859-1')))
    bit_plain = ''.join(format(ord(n), '08b') for n in str(plaintext.decode('ISO-8859-1')))
    for i in bit_list:
        modified_ptext = list(bit_plain)
        if modified_ptext[i] == '0':
            modified_ptext[i] = '1'
            modified_ptext2 = ''.join(modified_ptext)
        else:
            modified_ptext[i] = '0'
            modified_ptext2 = ''.join(modified_ptext)
        str_ptext2 = ''.join(chr(int(modified_ptext2[x:x+8], 2)) for x in range(0, len(modified_ptext2), 8)).encode('ISO-8859-1')
        new_ciphertext = aes_encrypt_ctr(key, str_ptext2)
        new_bit_cipher = ''.join(format(ord(l), '08b') for l in str(new_ciphertext.decode('ISO-8859-1')))
        for x in range(128):
            if new_bit_cipher[x] != bit_cipher[x]:
                count += 1
            else:
                pass
        new_list.append(count)
        count = 0
    print('The corresponding number of bits changed : ', new_list)


def aes_key_av_test(plaintext, key, bit_list):
    new_list = []
    count = 0
    ciphertext = aes_encrypt_ctr(key, plaintext)
    bit_cipher = ''.join(format(ord(m), '08b') for m in str(ciphertext.decode('ISO-8859-1')))
    bit_key = ''.join(format(ord(n), '08b') for n in str(key.decode('ISO-8859-1')))
    for i in bit_list:
        modified_key = list(bit_key)
        if modified_key[i] == '0':
            modified_key[i] = '1'
            modified_key2 = ''.join(modified_key)
        else:
            modified_key[i] = '0'
            modified_key2 = ''.join(modified_key)
        str_key2 = ''.join(chr(int(modified_key2[x:x + 8], 2)) for x in range(0, len(modified_key2), 8)).encode('ISO-8859-1')
        new_ciphertext = aes_encrypt_ctr(str_key2, plaintext)
        new_bit_cipher = ''.join(format(ord(l), '08b') for l in str(new_ciphertext.decode('ISO-8859-1')))
        for x in range(0, 128):
            if bit_cipher[x] != new_bit_cipher[x]:
                count += 1
            else:
                pass
        new_list.append(count)
        count = 0
    print('The corresponding number of bits changed : ', new_list)


if __name__ == "__main__":
    plaintext = input('Enter the required plaintext : ').encode('ISO-8859-1')
    key = input('Enter master key : ').encode('ISO-8859-1')
    n = int(input('Enter number of tries : '))
    bit_list = []
    for i in range(n):
        j = int(input(f'Enter bit number {i + 1} to flip (b/w 0 and 127) : '))
        if j < 0 or j > 127:
            raise ValueError('Invalid input provided!')
        bit_list.append(j)
    aes_input_av_test(plaintext, key, bit_list)
    aes_key_av_test(plaintext, key, bit_list)
