from minizip.tree import build_tree
from minizip.container import unpack


def decode(blob: bytes) -> bytes:
    freq, padding, encoded = unpack(blob)
    root = build_tree(freq)

    # edge case: file had only one unique byte
    if root.byte is not None:
        return bytes([root.byte]) * root.freq

    bits = "".join(f"{b:08b}" for b in encoded)
    if padding:
        bits = bits[:-padding]

    out = bytearray()
    node = root
    for bit in bits:
        node = node.left if bit == "0" else node.right
        if node.byte is not None:
            out.append(node.byte)
            node = root

    return bytes(out)