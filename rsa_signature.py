import hashlib

print("="*50)
print("SIMULASI RSA DIGITAL SIGNATURE")
print("="*50)

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = 2753

pesan = 123

cipher = pow(pesan, e, n)
plain = pow(cipher, d, n)

print("Pesan Asli :", pesan)
print("Cipher     :", cipher)
print("Dekripsi   :", plain)

message_hash = int(
    hashlib.sha256(str(pesan).encode()).hexdigest(),
    16
)

signature = pow(message_hash, d, n)

verify = pow(signature, e, n)

print("\nSignature :", signature)

if verify == message_hash % n:
    print("Signature VALID")
else:
    print("Signature TIDAK VALID")
