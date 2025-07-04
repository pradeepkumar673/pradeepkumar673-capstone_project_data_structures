"""
Simple Huffman Encoder
- Compresses text using Huffman coding
- Made by Dhilipan and Pradeepkumar
"""

# Tutorial
"""To use the Huffman Encoder:
1. Run the program and enter your text
2. See the Huffman codes generated
3. View compressed binary output
4. Verify decompression works perfectly

Example: Input "hello" gives:
h: 00
e: 01
l: 10
o: 11
Compressed: 0001101011 (10 bits vs original 40 bits)
"""

import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    return freq

def build_huffman_tree(freq):
    heap = []
    for char, count in freq.items():
        heapq.heappush(heap, HuffmanNode(char, count))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    
    return heapq.heappop(heap)

def generate_codes(node, prefix="", codes={}):
    if node.char:
        codes[node.char] = prefix
    else:
        generate_codes(node.left, prefix + "0", codes)
        generate_codes(node.right, prefix + "1", codes)
    return codes

def huffman_compress(text):
    if not text:
        return "", {}, ""
    
    freq = build_frequency_dict(text)
    tree = build_huffman_tree(freq)
    codes = generate_codes(tree)
    
    compressed = "".join([codes[char] for char in text])
    return compressed, codes, tree

def huffman_decompress(compressed, tree):
    current = tree
    result = []
    
    for bit in compressed:
        current = current.left if bit == '0' else current.right
        if current.char:
            result.append(current.char)
            current = tree
    
    return "".join(result)

# Main Program
print("=== SIMPLE HUFFMAN ENCODER ===")
text = input("Enter text to compress: ")

compressed, codes, tree = huffman_compress(text)

print("\nHUFFMAN CODES:")
for char, code in sorted(codes.items()):
    display = {' ': '[space]', '\n': '[newline]', '\t': '[tab]'}.get(char, char)
    print(f"{display}\t{code}")

print(f"\nCompressed binary: {compressed}")
print(f"Original size: {len(text) * 8} bits")
print(f"Compressed size: {len(compressed)} bits")
print(f"Compression ratio: {len(compressed)/(len(text)*8):.1%}")

decompressed = huffman_decompress(compressed, tree)
print(f"\nDecompressed text: {decompressed}")
print("Success!" if decompressed == text else "Error in decompression")