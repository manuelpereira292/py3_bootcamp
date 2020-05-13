import rsa

with open('private.pem', mode='rb') as privatefile:
    keydata = privatefile.read()
privkey = rsa.PrivateKey.load_pkcs1(keydata)

message = 'Hello World!'.encode('utf8')
signature = rsa.sign(message, privkey, 'SHA-1')
print(signature)

#-------------------------------------------------------------

with open('public.pem', mode='rb') as publicfile:
    keydata = publicfile.read()
pubkey = rsa.PublicKey.load_pkcs1(keydata)

validation = rsa.verify(message, signature, pubkey)
if validation == 'SHA-1':
   print('Valid')
else:
   print('Innalid')