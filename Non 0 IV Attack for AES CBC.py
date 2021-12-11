from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import HMAC, SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii


def example():
    message = 'coolcryptographyisverycool'
    key = get_random_bytes(16)
    iv = '1234567891234567'
    new_message = 'pwnedpwnedpwnedpisverycool'
    next_message = [chr(ord(a) ^ ord(b) ^ ord(c)) for a, b, c in zip(message, new_message, iv)]
    new_iv = "".join(next_message)
    ciphertext = aes_encrypt_cbc(key, message.encode(), iv.encode())
    ciphertext2 = aes_encrypt_cbc(key, new_message.encode(), new_iv.encode())
    mac = generate_mac(ciphertext)
    mac1 = generate_mac(ciphertext2)
    print(f'\nMAC Digest 1 with IV = {iv} and plaintext = {message} is : {mac.hexdigest()}')
    print(f'The Ciphertext for the above is : ', pretty_hex(ciphertext))
    print(f'MAC Digest 2 with IV = {new_iv} and plaintext = {new_message} is : {mac1.hexdigest()}')
    print(f'The Ciphertext for the above is : ', pretty_hex(ciphertext2))
    plaintext = aes_decrypt_cbc(key, ciphertext, iv.encode())
    print(f'\n\nDecrypted Text is: ', pretty_hex(plaintext))


def aes_encrypt_cbc(k, text, iv):
    e_cipher = AES.new(k, AES.MODE_CBC, iv=iv)
    c = e_cipher.encrypt(pad(text, 16))
    return c


def aes_decrypt_cbc(k, code, iv):
    d_cipher = AES.new(k, AES.MODE_CBC, iv=iv)
    d = unpad(d_cipher.decrypt(code), 16)
    return d


def generate_mac(codex):
    key = b'commonkey'
    mac1 = HMAC.new(key, codex, digestmod=SHA256)
    return mac1


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
