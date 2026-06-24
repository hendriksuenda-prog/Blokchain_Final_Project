import hashlib
import time

print("="*50)
print("SIMULASI PROOF OF WORK")
print("="*50)

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

start = time.perf_counter()

nonce = 0
target = "0000"

while True:

    data = "BLOCKCHAIN_RIMAWATI" + str(nonce)

    hasil_hash = sha256(data)

    if hasil_hash.startswith(target):
        break

    nonce += 1

end = time.perf_counter()

print("Nonce ditemukan :", nonce)
print("Hash Mining     :", hasil_hash)
print("Waktu Mining    :", round(end-start,4), "detik")
