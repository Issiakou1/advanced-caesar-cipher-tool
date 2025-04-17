#!/usr/bin/env python3

class CaesarCipher:
    def __init__(self, shift=3):
        """Initialize Caesar cipher with a default shift of 3."""
        self.shift = shift % 26
        self.char_set = 'abcdefghijklmnopqrstuvwxyz'
        self.char_map_encrypt = {}
        self.char_map_decrypt = {}
        self._build_char_maps()

    def _build_char_maps(self):
        """Build character mapping dictionaries for encryption and decryption."""
        for i, char in enumerate(self.char_set):
            shifted_index = (i + self.shift) % 26
            shifted_char = self.char_set[shifted_index]
            
            # Lowercase mappings
            self.char_map_encrypt[char] = shifted_char
            self.char_map_decrypt[shifted_char] = char
            
            # Uppercase mappings
            self.char_map_encrypt[char.upper()] = shifted_char.upper()
            self.char_map_decrypt[shifted_char.upper()] = char.upper()

    def encrypt(self, plaintext):
        """Encrypt plaintext using Caesar cipher."""
        return self._transform_text(plaintext, self.char_map_encrypt)
    
    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Caesar cipher."""
        return self._transform_text(ciphertext, self.char_map_decrypt)
    
    def _transform_text(self, text, char_map):
        """Transform text using provided character mapping."""
        result = []
        for char in text:
            if char.isalpha():
                result.append(char_map.get(char, char))
            else:
                result.append(char)
        return ''.join(result)

    def brute_force(self, text, is_encrypted=True):
        """Try all possible shift values to decrypt or encrypt text."""
        results = []
        transform_func = self.decrypt if is_encrypted else self.encrypt
        
        original_shift = self.shift
        
        for shift in range(26):
            self.shift = shift
            self._build_char_maps()
            result = transform_func(text)
            results.append((shift, result))
        
        # Restore original shift
        self.shift = original_shift
        self._build_char_maps()
        
        return results
    
    def set_shift(self, shift):
        """Set a new shift value."""
        self.shift = shift % 26
        self._build_char_maps()


class AdvancedCaesarCipher(CaesarCipher):
    def __init__(self, shift=3, key=None):
        """Initialize with optional shift and key for key-based shifting."""
        super().__init__(shift)
        self.key = key
        self.use_key = key is not None
    
    def _get_shift_for_position(self, position):
        """Get shift value for a specific position when using key-based shifting."""
        if not self.use_key:
            return self.shift
        
        # Use the ASCII value of the key character at corresponding position (cycling through key)
        key_char = self.key[position % len(self.key)]
        return (self.shift + ord(key_char)) % 26
    
    def encrypt(self, plaintext):
        """Encrypt using position-based shifting if a key is provided."""
        if not self.use_key:
            return super().encrypt(plaintext)
        
        result = []
        char_position = 0
        
        for char in plaintext:
            if char.isalpha():
                # Calculate shift for this position
                pos_shift = self._get_shift_for_position(char_position)
                
                # Determine base and offset
                if char.islower():
                    base = ord('a')
                else:
                    base = ord('A')
                
                # Apply shift
                shifted = (ord(char) - base + pos_shift) % 26 + base
                result.append(chr(shifted))
                char_position += 1
            else:
                result.append(char)
        
        return ''.join(result)
    
    def decrypt(self, ciphertext):
        """Decrypt using position-based shifting if a key is provided."""
        if not self.use_key:
            return super().decrypt(ciphertext)
        
        result = []
        char_position = 0
        
        for char in ciphertext:
            if char.isalpha():
                # Calculate shift for this position
                pos_shift = self._get_shift_for_position(char_position)
                
                # Determine base and offset
                if char.islower():
                    base = ord('a')
                else:
                    base = ord('A')
                
                # Apply reverse shift
                shifted = (ord(char) - base - pos_shift) % 26 + base
                result.append(chr(shifted))
                char_position += 1
            else:
                result.append(char)
        
        return ''.join(result)
    
    def set_key(self, key):
        """Set a new encryption/decryption key."""
        self.key = key
        self.use_key = key is not None


def analyze_frequency(text):
    """Analyze character frequency in text to help with cryptanalysis."""
    # Only consider alphabetic characters
    text = ''.join(c.lower() for c in text if c.isalpha())
    
    # Count character occurrences
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Calculate frequency
    total_chars = len(text)
    frequency = {char: count / total_chars for char, count in char_count.items()}
    
    # Sort by frequency
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_freq


def auto_decrypt(ciphertext, top_n=5):
    """Attempt automatic decryption based on frequency analysis."""
    # English letter frequency (most common first)
    english_freq = 'etaoinsrhdlucmfywgpbvkjxqz'
    
    # Get frequency analysis
    text_freq = analyze_frequency(ciphertext)
    
    # If we have at least a few characters to work with
    if text_freq:
        possible_shifts = []
        
        # Try matching the most frequent character to each of the top 5 English characters
        for eng_char in english_freq[:5]:
            cipher_char = text_freq[0][0]  # Most frequent character in ciphertext
            
            # Calculate potential shift
            shift = (ord(cipher_char) - ord(eng_char)) % 26
            possible_shifts.append(shift)
        
        # Try each potential shift and return top N results
        cipher = CaesarCipher()
        results = []
        
        for shift in possible_shifts:
            cipher.set_shift(shift)
            decrypted = cipher.decrypt(ciphertext)
            results.append((shift, decrypted))
        
        return results[:top_n]
    
    return []


if __name__ == "__main__":
    # Basic usage example
    cipher = CaesarCipher(shift=3)
    message = "Hello, World!"
    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # Advanced usage with key
    adv_cipher = AdvancedCaesarCipher(shift=5, key="SECRET")
    adv_encrypted = adv_cipher.encrypt(message)
    adv_decrypted = adv_cipher.decrypt(adv_encrypted)
    
    print("\nAdvanced Caesar Cipher with key:")
    print(f"Original: {message}")
    print(f"Encrypted: {adv_encrypted}")
    print(f"Decrypted: {adv_decrypted}") 