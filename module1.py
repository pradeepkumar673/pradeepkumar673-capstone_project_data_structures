"""
Simple Frequency Analyzer
- Type your message and see character counts immediately
- Made by Dhilipan and Pradeepkumar
"""


#tutorial
"""To use the Frequency Analyzer, simply run the program and type or paste your
text when prompted. The tool will instantly display a clear table showing each
character's frequency count and ASCII value, with special characters like spaces labeled as [space].
It also calculates the total size in bytes and bits. For example, if you input 'hello', you'll immediately
see counts for each letter and the total size (5 bytes, 40 bits). This output gives you the exact frequency
data needed to build your Huffman tree in Module 2 for the compression phase"""



print("=== SIMPLE FREQUENCY ANALYZER ===")
message = input("Type your message: ")

# to Calculate frequencies
freq = {}
for char in message:
    freq[char] = freq.get(char, 0) + 1

# Display results
print("\nCHARACTER COUNTS:")
print("Char\tCount\tASCII")
print("-" * 20)

for char, count in sorted(freq.items()):
    # Show special names for whitespace
    if char == ' ':
        display = "[space]"
    elif char == '\n':
        display = "[newline]" 
    elif char == '\t':
        display = "[tab]"
    else:
        display = char
        
    print(f"{display}\t{count}\t{ord(char)}")

# Show size info
print(f"\nTotal characters: {len(message)}")
print(f"Size: {len(message)} bytes ({len(message)*8} bits)")