from flask import Flask, render_template, request, jsonify, session
from modules.huffman import HuffmanCoding
from modules.des_cipher import DESCipher
import os
import base64

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/huffman', methods=['GET', 'POST'])
def huffman():
    result = None
    original_size = 0
    compressed_size = 0
    compression_ratio = 0
    codes = {}
    
    if request.method == 'POST':
        text = request.form.get('text', '')
        if text:
            huffman = HuffmanCoding()
            compressed, codes = huffman.compress(text)
            decompressed = huffman.decompress(compressed, huffman.root)
            
            # Calculate statistics
            original_size = len(text) * 8  # Assuming 8 bits per character
            compressed_size = sum(len(codes[char]) * text.count(char) for char in set(text))
            compression_ratio = (1 - (compressed_size / original_size)) * 100 if original_size > 0 else 0
            
            # Store in session for visualization
            session['huffman_tree'] = huffman.get_tree_representation()
            
            result = {
                'original_text': text,
                'compressed': compressed,
                'decompressed': decompressed,
                'original_size': original_size,
                'compressed_size': compressed_size,
                'compression_ratio': compression_ratio,
                'codes': codes
            }
    
    return render_template('huffman.html', result=result)

@app.route('/des', methods=['GET', 'POST'])
def des():
    result = None
    
    if request.method == 'POST':
        text = request.form.get('text', '')
        key = request.form.get('key', '')
        action = request.form.get('action', 'encrypt')
        
        if text and key:
            des_cipher = DESCipher(key)
            
            if action == 'encrypt':
                encrypted = des_cipher.encrypt(text)
                result = {
                    'original_text': text,
                    'processed_text': base64.b64encode(encrypted).decode('utf-8'),
                    'action': 'encrypted'
                }
            else:
                try:
                    decrypted = des_cipher.decrypt(base64.b64decode(text))
                    result = {
                        'original_text': text,
                        'processed_text': decrypted,
                        'action': 'decrypted'
                    }
                except Exception as e:
                    result = {
                        'error': f"Error al descifrar: {str(e)}"
                    }
    
    return render_template('des.html', result=result)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/visualize_huffman')
def visualize_huffman():
    tree_data = session.get('huffman_tree', {})
    return render_template('visualize_huffman.html', tree_data=tree_data)

if __name__ == '__main__':
    app.run(debug=True)
