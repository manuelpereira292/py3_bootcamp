import rsa

with open('public.pem', mode='rb') as publicfile:
    keydata = publicfile.read()
pubkey = rsa.PublicKey.load_pkcs1(keydata)

message = 'Hello World!'.encode('utf8')
crypto = rsa.encrypt(message, pubkey)
print(crypto)


#----------------------------------------------------------------


with open('private.pem', mode='rb') as privatefile:
    keydata = privatefile.read()
privkey = rsa.PrivateKey.load_pkcs1(keydata)

message = rsa.decrypt(crypto, privkey)
print(message.decode('utf8'))