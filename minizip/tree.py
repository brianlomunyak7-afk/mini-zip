import heapq


class Node:
    def __init__(self, freq, byte=None, left=None, right=None):
        self.freq = freq
        self.byte = byte      # only set on leaf nodes
        self.left = left
        self.right = right


def build_tree(freq: dict) -> Node:
    heap = []
    counter = 0  # tie-breaker so heapq never compares Nodes
    for byte, count in freq.items():
        heapq.heappush(heap, (count, counter, Node(count, byte)))
        counter += 1

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        parent = Node(f1 + f2, None, left, right)
        heapq.heappush(heap, (parent.freq, counter, parent))
        counter += 1

    return heap[0][2]