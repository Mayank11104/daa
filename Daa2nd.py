
import heapq

text = input("Enter a string: ")

if not text:
    print("Please enter a non-empty string.")
else:
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

    # Build the Huffman tree
    while len(heap) > 1:
        f1, c1, left = heapq.heappop(heap)
        f2, c2, right = heapq.heappop(heap)

        new_node = (left, right)

        heapq.heappush(
            heap, (f1 + f2, counter, new_node)
        )
        counter += 1

    # Generate Huffman codes
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

    # Display Huffman codes
    print("Huffman Codes:")

    for ch, code in codes.items():
        print(repr(ch), ":", code)

    # Encode the original string
    encoded = "".join(codes[ch] for ch in text)

    print("Encoded String:", encoded)
