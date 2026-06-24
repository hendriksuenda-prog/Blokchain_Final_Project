import hashlib
import time

class Block:

    def __init__(self, index, data, previous_hash):

        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = time.ctime()
        self.hash = self.calculate_hash()

    def calculate_hash(self):

        isi = (
            str(self.index)
            + self.data
            + self.previous_hash
            + self.timestamp
        )

        return hashlib.sha256(
            isi.encode()
        ).hexdigest()


class Blockchain:

    def __init__(self):

        self.chain = [self.create_genesis()]

    def create_genesis(self):

        return Block(
            0,
            "Genesis Block",
            "0"
        )

    def add_block(self, data):

        previous = self.chain[-1]

        block = Block(
            len(self.chain),
            data,
            previous.hash
        )

        self.chain.append(block)


bc = Blockchain()

bc.add_block("Rima kirim Rp100.000")
bc.add_block("Salwa kirim Rp50.000")

for block in bc.chain:

    print("\nBlock :", block.index)
    print("Data :", block.data)
    print("Hash :", block.hash)
