import hashlib

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

def merkle_root(hash_list):
    current = hash_list.copy()
    while len(current) > 1:
        if len(current) % 2 != 0:
            current.append(current[-1])
        new_level = []
        for i in range(0, len(current), 2):
            gabung = current[i] + current[i + 1]
            new_level.append(sha256(gabung))
        current = new_level
    return current[0]

print("=" * 50)
print("   TESTING FUNGSI BLOCKCHAIN")
print("=" * 50)

# Test SHA-256
print("\n[TEST 1] SHA-256")
data = "Rima -> Salwa : Rp100.000"
hasil = sha256(data)
print(f"Input  : {data}")
print(f"Output : {hasil}")
assert len(hasil) == 64, "GAGAL: panjang hash bukan 64"
print("Status : PASSED")

# Test Merkle Root
print("\n[TEST 2] MERKLE ROOT")
transaksi = [
    "Rima -> Salwa : Rp100.000",
    "Salwa -> Nazwa : Rp50.000",
    "Nazwa -> Andi : Rp75.000",
    "Andi -> Budi : Rp25.000"
]
hashes = [sha256(t) for t in transaksi]
root = merkle_root(hashes)
print(f"Merkle Root : {root}")
assert len(root) == 64, "GAGAL: merkle root tidak valid"
print("Status : PASSED")

# Test RSA
print("\n[TEST 3] RSA ENKRIPSI & DEKRIPSI")
p, q = 61, 53
n = p * q
e, d = 17, 2753
pesan = 123
cipher = pow(pesan, e, n)
plain = pow(cipher, d, n)
print(f"Pesan Asli     : {pesan}")
print(f"Enkripsi       : {cipher}")
print(f"Dekripsi       : {plain}")
assert pesan == plain, "GAGAL: dekripsi tidak cocok"
print("Status : PASSED")

print("\n" + "=" * 50)
print("SEMUA TEST BERHASIL")
print("=" * 50)
