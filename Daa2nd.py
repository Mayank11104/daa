
import heapq


def huffman_encoding(text):

    # Count frequency of each character
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    # Create a min-heap
    heap = []
    counter = 0

    for ch, f in freq.items():
        heapq.heappush(heap, (f, counter, ch))
        counter += 1

    # Build Huffman Tree
    while len(heap) > 1:

        f1, c1, left = heapq.heappop(heap)
        f2, c2, right = heapq.heappop(heap)

        new_node = (left, right)

        heapq.heappush(heap, (f1 + f2, counter, new_node))
        counter += 1

    # Generate Huffman Codes
    codes = {}

    def make_codes(tree, code=""):

        if isinstance(tree, str):
            codes[tree] = code
        else:
            make_codes(tree[0], code + "0")
            make_codes(tree[1], code + "1")

    if len(freq) == 1:
        only_char = next(iter(freq))
        codes[only_char] = "0"
    else:
        make_codes(heap[0][2])

    # Display frequencies
    print("\nCharacter Frequencies:")
    for ch, f in freq.items():
        print(repr(ch), ":", f)

    # Display Huffman Codes
    print("\nHuffman Codes:")
    for ch, code in codes.items():
        print(repr(ch), ":", code)

    # Encode original string
    encoded = "".join(codes[ch] for ch in text)

    print("\nEncoded String:", encoded)

    return encoded, codes


# # Huffman Decoding Function
# def huffman_decoding(encoded, codes):
#
#     # Reverse the codes dictionary to map code -> character
#     reverse_codes = {code: ch for ch, code in codes.items()}
#
#     decoded = ""
#     current_code = ""
#
#     for bit in encoded:
#         current_code += bit
#         if current_code in reverse_codes:
#             decoded += reverse_codes[current_code]
#             current_code = ""
#
#     if current_code:
#         print("\nWarning: Invalid or incomplete Huffman code bits:", current_code)
#
#     print("\nDecoded String:", decoded)
#     return decoded


# Main Menu
def main():
    last_encoded = None
    last_codes = None

    while True:

        print("\n===== HUFFMAN ENCODING =====")
        print("1. Encode String")
        # print("2. Decode String")
        print("2. Exit")  # Change to "3. Exit" when Decode String is uncommented

        choice = int(input("Enter your choice: "))

        if choice == 1:

            text = input("Enter a string: ")

            if not text:
                print("Please enter a non-empty string.")
            else:
                last_encoded, last_codes = huffman_encoding(text)

        # elif choice == 2:
        #
        #     if last_codes is None:
        #         print("Please encode a string first (Option 1) to generate Huffman codes.")
        #     else:
        #         encoded_input = input(
        #             f"Enter encoded string (or press Enter to decode '{last_encoded}'): "
        #         ).strip()
        #         if not encoded_input:
        #             encoded_input = last_encoded
        #         huffman_decoding(encoded_input, last_codes)

        elif choice == 2:  # Change to 3 when Decode String is uncommented

            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice! Please select 1 or 2.")

main()