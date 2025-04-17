#!/usr/bin/env python3

import argparse
import sys
from caesar_cipher import CaesarCipher, AdvancedCaesarCipher, analyze_frequency, auto_decrypt

def main():
    parser = argparse.ArgumentParser(description='Advanced Caesar Cipher Encryption/Decryption Tool')
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Encrypt command
    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a message')
    encrypt_parser.add_argument('message', help='Message to encrypt')
    encrypt_parser.add_argument('-s', '--shift', type=int, default=3, help='Shift value (default: 3)')
    encrypt_parser.add_argument('-k', '--key', help='Key for advanced encryption')
    encrypt_parser.add_argument('-f', '--file', help='Read message from file')
    
    # Decrypt command
    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt a message')
    decrypt_parser.add_argument('message', help='Message to decrypt')
    decrypt_parser.add_argument('-s', '--shift', type=int, default=3, help='Shift value (default: 3)')
    decrypt_parser.add_argument('-k', '--key', help='Key for advanced decryption')
    decrypt_parser.add_argument('-f', '--file', help='Read message from file')
    
    # Brute force command
    brute_parser = subparsers.add_parser('brute', help='Try all possible shifts to decrypt')
    brute_parser.add_argument('message', help='Message to decrypt')
    brute_parser.add_argument('-f', '--file', help='Read message from file')
    
    # Frequency analysis command
    freq_parser = subparsers.add_parser('analyze', help='Perform frequency analysis')
    freq_parser.add_argument('message', help='Message to analyze')
    freq_parser.add_argument('-f', '--file', help='Read message from file')
    
    # Auto decrypt command
    auto_parser = subparsers.add_parser('auto', help='Attempt automatic decryption')
    auto_parser.add_argument('message', help='Message to decrypt')
    auto_parser.add_argument('-n', '--top', type=int, default=5, help='Number of top results to show')
    auto_parser.add_argument('-f', '--file', help='Read message from file')
    
    args = parser.parse_args()
    
    # Handle file input if specified
    if hasattr(args, 'file') and args.file:
        try:
            with open(args.file, 'r') as f:
                args.message = f.read().strip()
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            return 1
    
    # Execute appropriate command
    if args.command == 'encrypt':
        if args.key:
            cipher = AdvancedCaesarCipher(shift=args.shift, key=args.key)
        else:
            cipher = CaesarCipher(shift=args.shift)
        
        encrypted = cipher.encrypt(args.message)
        print(encrypted)
    
    elif args.command == 'decrypt':
        if args.key:
            cipher = AdvancedCaesarCipher(shift=args.shift, key=args.key)
        else:
            cipher = CaesarCipher(shift=args.shift)
        
        decrypted = cipher.decrypt(args.message)
        print(decrypted)
    
    elif args.command == 'brute':
        cipher = CaesarCipher()
        results = cipher.brute_force(args.message)
        
        print("Shift | Result")
        print("-" * 40)
        for shift, result in results:
            print(f"{shift:5d} | {result}")
    
    elif args.command == 'analyze':
        frequencies = analyze_frequency(args.message)
        
        print("Character | Frequency")
        print("-" * 25)
        for char, freq in frequencies:
            print(f"{char:9s} | {freq:.4f}")
    
    elif args.command == 'auto':
        results = auto_decrypt(args.message, args.top)
        
        if results:
            print("Potential decryptions based on frequency analysis:")
            print("Shift | Result")
            print("-" * 40)
            for shift, result in results:
                print(f"{shift:5d} | {result}")
        else:
            print("Not enough data for frequency analysis.")
    
    else:
        parser.print_help()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 