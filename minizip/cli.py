import argparse
import sys

from minizip.frequency import count_frequencies
from minizip.tree import build_tree
from minizip.codes import build_codes
from minizip.encoder import encode
from minizip.container import pack
from minizip.decoder import decode


def compress(src):
    with open(src, "rb") as f:
        data = f.read()
    if not data:
        sys.exit("Empty file, nothing to compress")

    freq = count_frequencies(data)
    codes = build_codes(build_tree(freq))
    encoded, padding = encode(data, codes)
    blob = pack(freq, padding, encoded)

    out = src + ".mz"
    with open(out, "wb") as f:
        f.write(blob)

    saved = (1 - len(blob) / len(data)) * 100
    print(f"Original:   {len(data):,} bytes")
    print(f"Compressed: {len(blob):,} bytes")
    print(f"Saved:      {saved:.1f}%")
    print(f"Written to: {out}")


def decompress(src):
    with open(src, "rb") as f:
        blob = f.read()
    try:
        data = decode(blob)
    except ValueError as e:
        sys.exit(f"Error: {e}")

    out = (src[:-3] if src.endswith(".mz") else src) + ".restored"
    with open(out, "wb") as f:
        f.write(data)
    print(f"Restored {len(data):,} bytes to: {out}")


def main():
    parser = argparse.ArgumentParser(prog="mini-zip")
    parser.add_argument("command", choices=["compress", "decompress"])
    parser.add_argument("file")
    args = parser.parse_args()

    if args.command == "compress":
        compress(args.file)
    else:
        decompress(args.file)


if __name__ == "__main__":
    main()