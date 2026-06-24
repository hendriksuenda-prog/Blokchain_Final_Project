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
            new_hash = sha256(gabung)
            new_level.append(new_hash)

        current = new_level

    return current[0]


if __name__ == "__main__":

    transaksi = [
        "Rima -> Salwa",
        "Salwa -> Nazwa",
        "Nazwa -> Andi",
        "Andi -> Budi"
    ]

    hashes = [sha256(t) for t in transaksi]

    print("Merkle Root:")
    print(merkle_root(hashes))
