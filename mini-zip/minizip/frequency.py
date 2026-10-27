def count_frequencies(data: bytes) -> dict:
    freq = {}
    for byte in data:
        freq[byte] = freq.get(byte, 0) + 1
    return freq
