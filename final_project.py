"""
OPTIMIZED FILE COMPRESSION USING BINARY TREES
- Complete Capstone Project Solution
- Combines Frequency Analysis (Module 1) and Huffman Coding (Module 2)
- Made by Dhilipan and Pradeepkumar
"""

import heapq
from collections import defaultdict

# ====================== TUTORIAL ======================
"""
HOW TO USE THIS PROGRAM:
1. RUN the script (python compression.py)
2. ENTER your text when prompted
3. VIEW the analysis:
   - Character frequencies (Module 1)
   - Huffman codes (Module 2)
   - Compression results
4. VERIFY perfect reconstruction

EXAMPLE OUTPUT FOR "hello":
-------------------------
CHARACTER COUNTS:
h 1 104
e 1 101
l 2 108
o 1 111

HUFFMAN CODES:
l: 0
o: 10
h: 110
e: 111

Compressed: 1101110010 (10 bits)
Original: 40 bits → 75% reduction
"""

# ====================== CORE IMPLEMENTATION ======================
class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def analyze_frequencies(text):
    """Module 1: Frequency Analysis"""
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    
    print("\nCHARACTER FREQUENCIES:")
    print("{:<8} {:<8} {:<8}".format("Char", "Count", "ASCII"))
    print("-" * 24)
    
    for char, count in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
        display = {' ': '[space]', '\n': '[newline]', '\t': '[tab]'}.get(char, char)
        print("{:<8} {:<8} {:<8}".format(display, count, ord(char)))
    
    print(f"\nOriginal size: {len(text)} bytes ({len(text)*8} bits)")
    return freq

def build_huffman_tree(freq_dict):
    """Module 2: Tree Construction"""
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq+right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    
    return heapq.heappop(heap)

def generate_huffman_codes(root):
    """Module 2: Code Generation"""
    codes = {}
    
    def traverse(node, code=""):
        if node.char:
            codes[node.char] = code
        else:
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")
    
    traverse(root)
    return codes

def compress_text(text, codes):
    """Module 2: Compression Engine"""
    return ''.join(codes[char] for char in text)

def decompress_text(compressed, root):
    """Module 2: Decompression Engine"""
    current = root
    result = []
    
    for bit in compressed:
        current = current.left if bit == '0' else current.right
        if current.char:
            result.append(current.char)
            current = root
    
    return ''.join(result)

# ====================== MAIN EXECUTION ======================
def main():
    print("=== OPTIMIZED FILE COMPRESSION SYSTEM ===")
    text = input("\nEnter text to compress: ").strip()
    
    if not text:
        print("Error: No input provided")
        return
    
    # Execute Module 1
    frequencies = analyze_frequencies(text)
    
    # Execute Module 2
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)
    compressed = compress_text(text, huffman_codes)
    
    # Display Results
    print("\nHUFFMAN CODES:")
    for char, code in sorted(huffman_codes.items(), key=lambda x: (len(x[1]), x[1])):
        display = {' ': '[space]', '\n': '[newline]', '\t': '[tab]'}.get(char, char)
        print(f"{display:<8} → {code}")
    
    print(f"\nCompressed binary: {compressed}")
    print(f"Compressed size: {len(compressed)} bits")
    print(f"Compression ratio: {len(compressed)/ (len(text)*8):.1%}")
    
    # Verification
    decompressed = decompress_text(compressed, huffman_tree)
    print("\nVERIFICATION:")
    print(f"Original:    '{text}'")
    print(f"Decompressed: '{decompressed}'")
    print("✅ Perfect reconstruction" if text == decompressed else "❌ Decompression failed")

if __name__ == "__main__":
    main()