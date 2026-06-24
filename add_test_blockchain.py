from blockchain_class import Blockchain

print("="*50)
print("TEST BLOCKCHAIN")
print("="*50)

bc = Blockchain()

bc.add_block("Rima -> Salwa")
bc.add_block("Salwa -> Nazwa")
bc.add_block("Nazwa -> Andi")

print("Jumlah Block :", len(bc.chain))

for block in bc.chain:
    print(
        f"Block {block.index} : "
        f"{block.hash[:20]}..."
    )
