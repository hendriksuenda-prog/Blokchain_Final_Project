import hashlib

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

print("="*50)
print("VALIDASI BLOCKCHAIN")
print("="*50)

blockchain = []

previous_hash = sha256("GENESIS")

for i in range(3):

    block_hash = sha256(previous_hash + str(i))

    block = {
        "index": i + 1,
        "previous_hash": previous_hash,
        "hash": block_hash
    }

    blockchain.append(block)

    previous_hash = block_hash

valid = True

for i in range(1, len(blockchain)):

    if blockchain[i]["previous_hash"] != blockchain[i-1]["hash"]:
        valid = False

if valid:
    print("Blockchain VALID")
else:
    print("Blockchain TIDAK VALID")
