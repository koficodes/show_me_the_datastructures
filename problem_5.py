import hashlib
import time


class Block:

    def __init__(self, timestamp=None, data=None, previous_hash=None):
        if not timestamp or not data:
            raise("Timestamp or Data required")
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next_block = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "{}{}{}".format(
            self.timestamp, self.data, self.previous_hash)

        sha.update(hash_str.encode('utf-8'))

        return sha.hexdigest()

    def __str__(self):
        return "{}-{}-{}-{}\n".format(
            self.timestamp, self.data, self.hash, self.previous_hash)


class BlockChain:

    def __init__(self):
        self.head = None

    def append(self, block=None):
        if not block:
            return

        if not self.head:
            self.head = block
            return

        node = self.head

        while node.next_block:
            node = node.next_block

        node.next_block = block
        node.next_block.previous_hash = node.hash
        return

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next_block
        return count

    def __str__(self):
        if self.head is None:
            return 'Block chain empty'
        node = self.head
        output = ''
        while node:
            output += str(node)
            node = node.next_block
        return output


blockchain = BlockChain()

blockchain.append(Block(time.time(), '1st transaction'))
blockchain.append(Block(time.time(), '2nd transaction'))
blockchain.append(Block(time.time(), '3nd transaction'))

print(blockchain)

# 1560701945.9167106-1st transaction-2f274d2e5f3ac3a88f7b90ac0eb52489587d5e0a2fe605e89cc743a818d47b2b-None
# 1560701945.916737-2nd transaction-0b40d31d754b14138d1efeaeccade1f5631899236901416b91cd7b5d219e6566-2f274d2e5f3ac3a88f7b90ac0eb52489587d5e0a2fe605e89cc743a818d47b2b
# 1560701945.9167457-3nd transaction-7f5dccb637b4650dbafa275456167c1b796c96a11faabe83efda60593acaf098-0b40d31d754b14138d1efeaeccade1f5631899236901416b91cd7b5d219e6566

empty_block = BlockChain()
print(empty_block)  # Block chain empty

blockchain_2 = BlockChain()
blockchain_2.append()

# raises exception raise("Timestamp or Data required")
blockchain_2.append(Block())
