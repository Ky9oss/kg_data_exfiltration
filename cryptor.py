from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from io import BytesIO
import base64
import zlib


# 生成RSA密钥文件
def generate():

    new_key = RSA.generate(2048)
    public_key = new_key.publickey().exportKey()
    private_key = new_key.exportKey()

    with open("key.pub", 'wb') as t:
        t.write(public_key)
    with open("key.pri", 'wb') as t:
        t.write(private_key)

# 加载RSA密钥文件
def get_rsa_cipher(keytype):
    with open(f'key.{keytype}') as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    return (PKCS1_OAEP.new(rsakey), rsakey.size_in_bytes())


# 压缩，AES加密压缩后的数据，RSA加密AES密钥
def encrypt(plaintext):
    compressed_text = zlib.compress(plaintext) #压缩
    aes_key = get_random_bytes(16)
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(compressed_text)

    cipher_rsa, _ = get_rsa_cipher('pub')
    aes_key_encrypted = cipher_rsa.encrypt(aes_key)

    payload = aes_key_encrypted + cipher_aes.nonce + tag + ciphertext
    encrypted = base64.encodebytes(payload)
    return encrypted


# 解密
def decrypt(encrypted):
    payload_bytes = BytesIO(base64.decodebytes(encrypted))
    cipher_rsa, rsa_pri_keysize = get_rsa_cipher('pri')
    aes_key_encrypted = payload_bytes.read(rsa_pri_keysize)
    nonce = payload_bytes.read(16)
    tag = payload_bytes.read(16)
    ciphertext = payload_bytes.read()


    aes_key = cipher_rsa.decrypt(aes_key_encrypted)
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce)
    compressed_text = cipher_aes.decrypt_and_verify(ciphertext, tag)
    plaintext = zlib.decompress(compressed_text)

    return plaintext


if __name__ == "__main__":
    generate()

    plaintext = b'hello world'
    encrypted = encrypt(plaintext)
    decrypted = decrypt(encrypted)

    print(decrypted)
