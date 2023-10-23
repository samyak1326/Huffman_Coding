#SAMYAK JAIN 
#G01448453
#CS-584
#Book_Link : https://www.gutenberg.org/ebooks/23591


#read text file and filtering the escape filters
def read_text_file(filename, mode, enc):
    with open(filename, mode, encoding=enc) as f:
        content = [i.strip() for i in f.read()]
    return content

#func() to calculate frequency of each character
def frequency_calculator(content):
    frequency = {}
    for i in content:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency

content = read_text_file("gutenberg_temp_ebook.txt", "r", "utf-8")

frequency = frequency_calculator(content)
print("FREQUENCY")
print(frequency)


#filtering the non-repeating characters using ASCII values
ascii_characters = [ord(i) for i in content if len(i) >0]
ascii_characters_finals = [chr(i) for i in ascii_characters if i >= 32 and i <= 128]
print("ASCII CHARACTERS")
print(set(ascii_characters_finals))


#final frequency of each character
final_frequency = {key: val for key, val in frequency.items() if key in ascii_characters_finals}
print("FINAL FREQUENCY")
print(final_frequency)

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    #comparing the nodes
    def __lt__(self, other):
        return self.freq < other.freq
    
    #function to create huffman tree
def huffman_tree(content):
    heap = []

    #creating leaf node for each char with its frequency
    for key, val in content.items():
        node = Node(key, val)
        heapq.heappush(heap, node)

    #combining the nodes 
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)
    return heap[0]
    
#function to create huffman codes
def huffman_codes(node, code, codes):
    if node is None:
        return
    
    if node.char:
        codes[node.char] = code
        return
    
    huffman_codes(node.left, code + "0", codes) 
    huffman_codes(node.right, code + "1", codes)
    
#dictionary
frequency_dict = final_frequency
root = huffman_tree(frequency_dict)
codes= {}
huffman_codes(root, "", codes)


#printing table with Huffman Codes
print("_________________________________________________________")
print("Characters\tFrequencies\tHuffman Codes")
print("----------\t-----------\t-------------")
for key, val in frequency_dict.items():
    if key == '':
        continue
    print(f"{key}\t\t{val}\t\t{codes[key]}")
    
#calculating total no of bots by multiplying frequency of each character with its huffman code length
total_bits = sum([frequency_dict[i] * len(codes[i]) for i in frequency_dict.keys()])
print("TOTAL BITS: ", total_bits)
#calculating average code length
average_code_length = total_bits / sum(frequency_dict.values())
print(f"AVERAGE CODE LENGTH: {average_code_length:.3f} bits per character")

#calculating tota; no of bits achieved by doing fixed length encoding
fixed_length_encoding = (sum([7 * f for c,f in frequency_dict.items()]))
print("FIXED LENGTH ENCODING: ", fixed_length_encoding)

#calculating average code length of fixed length encoding
average_code_length_fixed = fixed_length_encoding / sum(frequency_dict.values())
print(f"AVERAGE CODE LENGTH OF FIXED LENGTH ENCODING, {average_code_length_fixed:.3f} bits per character")

#calculating sving in bits acheived by huffman coding
saving_in_bits = fixed_length_encoding - total_bits
saving_percentage = (saving_in_bits / fixed_length_encoding) * 100

print("SAVING IN BITS: ", saving_in_bits)
print(f"SAVING PERCENTAGE: {saving_percentage:.3f}%")