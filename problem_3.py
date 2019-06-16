import sys
from collections import defaultdict
import heapq


class Node:

    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __cmp__(self, other):
        if other is None or not isinstance(other, Node):
            return -1

        return self.frequency > other.frequency


class HuffmanTree:

    def __init__(self, text):
        self.text = text
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}

    def get_frequency(self):
        frequency = defaultdict(int)
        for char in self.text:
            frequency[char] += 1
        return frequency

    def create_heap(self, frequency):
        for key, freq in frequency.items():
            node = Node(key, freq)
            heapq.heappush(self.heap, node)

    def merge_node(self):
        while(len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            sum_freq = node1.frequency + node2.frequency

            merged_node = Node(None, sum_freq)
            merged_node.left = node1
            merged_node.right = node2

            heapq.heappush(self.heap, merged_node)

    def make_codes_recursive(self, root, code=""):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = code
            self.reverse_codes[code] = root.char
            return

        self.make_codes_recursive(root.left, code+"0")
        self.make_codes_recursive(root.right, code+"1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        self.make_codes_recursive(root, "")

    def make_encoded_text(self):
        encoded_text = ""
        for character in self.text:
            encoded_text += self.codes[character]
        return encoded_text

    def make_decoded_text(self, encoded_text):
        code = ""
        decoded_text = ""

        for bit in encoded_text:
            code += bit
            if code in self.reverse_codes:
                character = self.reverse_codes[code]
                decoded_text += character
                code = ""
        return decoded_text


def huffman_encoding(data):
    hTree = HuffmanTree(data)
    freq = hTree.get_frequency()
    hTree.create_heap(freq)
    hTree.merge_node()
    hTree.make_codes()
    encoded_data = hTree.make_encoded_text()
    return encoded_data, hTree


def huffman_decoding(data, tree):
    return tree.make_decoded_text(data)


if __name__ == "__main__":
    # codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print(encoded_data)
    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
