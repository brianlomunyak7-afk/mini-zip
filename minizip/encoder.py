def encode(data: bytes, codes: dict):
    bits = "".join(codes[b] for b in data)

    padding = (8 - len(bits) % 8) % 8
    bits += "0" * padding

    out = bytearray()
    for i in range(0, len(bits), 8):
        out.append(int(bits[i:i + 8], 2))

    return bytes(out), padding