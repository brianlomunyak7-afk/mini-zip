import struct

MAGIC = b"MZ"


def pack(freq: dict, padding: int, encoded: bytes) -> bytes:
    out = bytearray(MAGIC)
    out += struct.pack(">BH", padding, len(freq))
    for byte, count in freq.items():
        out += struct.pack(">BI", byte, count)
    out += encoded
    return bytes(out)


def unpack(blob: bytes):
    if blob[:2] != MAGIC:
        raise ValueError("Not a .mz file")
    padding, n = struct.unpack(">BH", blob[2:5])
    pos = 5
    freq = {}
    for _ in range(n):
        byte, count = struct.unpack(">BI", blob[pos:pos + 5])
        freq[byte] = count
        pos += 5
    return freq, padding, blob[pos:]