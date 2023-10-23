# Huffman_Coding


# **Description**

This repository contains Python code for implementing Huffman coding. The script reads a text file and generates the Huffman codes for each character based on their frequencies in the file. The codes are then printed out along with their corresponding frequencies. The script also calculates and displays additional statistics, such as the total number of bits required for encoding, the average code length, and the savings achieved through Huffman coding compared to fixed-length encoding.

Link of the Book I used for the project: **https://www.gutenberg.org/ebooks/23591**

# **Functions**

**read_text_file(filename, mode, enc)**: Reads a text file and returns its content as a list of strings.

**frequency_calculator(content):** Calculates the frequency of each character in the given content.

**huffman_tree(content):** Constructs a Huffman tree based on the frequencies of characters.

**huffman_codes(node, code, codes):** Generates Huffman codes for each character.

# **Output**

The output includes:

Frequencies of all characters in the file

ASCII characters after filtering

Final frequencies after filtering

Huffman codes for each character

Total number of bits required for Huffman encoding

Average code length for Huffman encoding

Total number of bits required for fixed-length encoding

Average code length for fixed-length encoding

Savings in bits achieved through Huffman coding