#python -m pip install rsa
import rsa
# pubkey, privkey = rsa.newkeys(512)
pubkey, privkey = rsa.newkeys(4096)

privkey_pkcs1 = privkey.save_pkcs1()
pubkey_pkcs1 = pubkey.save_pkcs1()

with open("private.pem", "wb") as file:
    file.write(privkey_pkcs1)

with open("public.pem", "wb") as file:
    file.write(pubkey_pkcs1)

print(privkey_pkcs1)
print(pubkey_pkcs1)