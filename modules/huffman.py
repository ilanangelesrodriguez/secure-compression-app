import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
        self.root = None
    
    def make_frequency_dict(self, text):
        return Counter(text)
    
    def make_heap(self, frequency):
        for char, freq in frequency.items():
            node = Node(char, freq)
            heapq.heappush(self.heap, node)
    
    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            
            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            
            heapq.heappush(self.heap, merged)
    
    def make_codes_helper(self, node, current_code):
        if node is None:
            return
        
        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
        
        self.make_codes_helper(node.left, current_code + "0")
        self.make_codes_helper(node.right, current_code + "1")
    
    def make_codes(self):
        self.root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(self.root, current_code)
    
    def get_encoded_text(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text
    
    def compress(self, text):
        frequency = self.make_frequency_dict(text)
        self.make_heap(frequency)
        self.merge_nodes()
        self.make_codes()
        
        encoded_text = self.get_encoded_text(text)
        return encoded_text, self.codes
    
    def decompress(self, encoded_text, root):
        current_node = root
        decoded_text = ""
        
        for bit in encoded_text:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right
            
            if current_node.char is not None:
                decoded_text += current_node.char
                current_node = root
        
        return decoded_text
    
    def get_tree_representation(self):
        """Generar una representación del árbol de Huffman para visualización"""
        def traverse(node, path=""):
            if node is None:
                return {}
            
            result = {
                "freq": node.freq,
                "char": node.char if node.char else "Internal",
                "path": path
            }
            
            if node.left or node.right:
                result["children"] = []
                if node.left:
                    result["children"].append(traverse(node.left, path + "0"))
                if node.right:
                    result["children"].append(traverse(node.right, path + "1"))
            
            return result
        
        return traverse(self.root)
