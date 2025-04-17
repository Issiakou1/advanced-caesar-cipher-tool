#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
from caesar_cipher import CaesarCipher, AdvancedCaesarCipher, analyze_frequency, auto_decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data.get('message', '')
    shift = int(data.get('shift', 3))
    key = data.get('key', None)
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    if key:
        cipher = AdvancedCaesarCipher(shift=shift, key=key)
    else:
        cipher = CaesarCipher(shift=shift)
    
    result = cipher.encrypt(message)
    return jsonify({'result': result})

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    message = data.get('message', '')
    shift = int(data.get('shift', 3))
    key = data.get('key', None)
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    if key:
        cipher = AdvancedCaesarCipher(shift=shift, key=key)
    else:
        cipher = CaesarCipher(shift=shift)
    
    result = cipher.decrypt(message)
    return jsonify({'result': result})

@app.route('/api/brute-force', methods=['POST'])
def brute_force():
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    cipher = CaesarCipher()
    results = cipher.brute_force(message)
    
    return jsonify({'results': [{'shift': shift, 'text': text} for shift, text in results]})

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    frequencies = analyze_frequency(message)
    
    return jsonify({'frequencies': [{'char': char, 'frequency': freq} for char, freq in frequencies]})

@app.route('/api/auto-decrypt', methods=['POST'])
def auto_decrypt_api():
    data = request.json
    message = data.get('message', '')
    top_n = int(data.get('top_n', 5))
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    results = auto_decrypt(message, top_n)
    
    return jsonify({'results': [{'shift': shift, 'text': text} for shift, text in results]})

if __name__ == '__main__':
    app.run(debug=True) 