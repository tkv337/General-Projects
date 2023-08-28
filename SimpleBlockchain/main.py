import hashlib

class TKVCoinBlock:

    def __init__(self, previous_block_hash, transaction_list): 
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list 

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Arshia sends 2 TKV Coin to Saba"
t2 = "Saba sends 1.1 TKV Coin to Ruby"
t3 = "Ruby sends 5 TKV Coin to Amy"
t4 = "Amy sends 2 TKV Coin to Miso"
t5 = "Miso sends 11 TKV Coin to Saba"
t6 = "Saba sends 2 TKV Coin to Arshia"

initial_block = TKVCoinBlock("Initial Message", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = TKVCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = TKVCoinBlock(second_block.block_hash, [t4, t5])

print(third_block.block_data)
print(third_block.block_hash)