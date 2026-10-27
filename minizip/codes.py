def build_codes(root) -> dict:
    codes = {}

    def walk(node, path):
        if node.byte is not None:      # leaf: we reached a letter
            codes[node.byte] = path or "0"
            return
        walk(node.left, path + "0")    # go left, add 0
        walk(node.right, path + "1")   # go right, add 1

    walk(root, "")
    return codes