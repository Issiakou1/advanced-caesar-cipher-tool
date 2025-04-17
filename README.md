# Advanced Caesar Cipher Encryption/Decryption 🔐

<img width="1012" alt="Screenshot 2025-04-18 at 04 13 20" src="https://github.com/user-attachments/assets/8f6d2fee-7900-47cd-b377-28186af1dafa" />


A cybersecurity project that implements an advanced version of the Caesar Cipher encryption algorithm with additional features for cryptanalysis and security.

## Features ✨

- **Basic Caesar Cipher** - Traditional implementation with customizable shift values
- **Advanced Caesar Cipher** - Enhanced version using key-based shifting for increased security
- **Brute Force Decryption** - Try all possible shift values (1-25) to decrypt ciphertext
- **Frequency Analysis** - Analyze character frequency in text to help with cryptanalysis
- **Automatic Decryption** - Attempt to automatically decrypt ciphertext based on English language frequency analysis
- **Command-Line Interface** - Perform operations via terminal commands
- **Web Interface** - User-friendly web application with graphical displays

## Installation 📦

1. Clone this repository:
   ```
   git clone https://github.com/pakagronglb/advanced-caesar-cipher.git
   cd advanced-caesar-cipher
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Detailed Usage Guide

### Initial Encryption and Decryption ⚙️

#### Command Line

```bash
# Encrypt a message with shift 3 (default)
python caesar_cli.py encrypt "Hello, World!"
# Output: Khoor, Zruog!

# Decrypt a message with shift 3
python caesar_cli.py decrypt "Khoor, Zruog!"
# Output: Hello, World!

# Encrypt with custom shift (e.g., 7)
python caesar_cli.py encrypt "Hello, World!" -s 7
# Output: Olssv, Dvysk!

# Decrypt with custom shift
python caesar_cli.py decrypt "Olssv, Dvysk!" -s 7
# Output: Hello, World!
```

#### Web Interface 👩🏻‍💻

1. Navigate to the "Encrypt" tab
2. Enter "Hello, World!" in the "Message to Encrypt" field
3. Set shift value to 5
4. Click "Encrypt" button
5. Result: "Mjqqt, Btwqi!"

### Advanced Key-Based Encryption ✨

The advanced mode uses both a shift value and a key for additional security, creating a variable shift pattern based on the key characters.

#### Command Line 🔐

```bash
# Encrypt using advanced key-based method
python caesar_cli.py encrypt "Hello, World!" -s 5 -k "SECRET"
# Output: Wphsg, Ogioe!

# Decrypt using the same key and shift
python caesar_cli.py decrypt "Wphsg, Ogioe!" -s 5 -k "SECRET"
# Output: Hello, World!
```

#### Web Interface 🕸️

1. Navigate to the "Encrypt" tab
2. Enter "Hello, World!" in the "Message to Encrypt" field
3. Set shift value to 5
4. Enter "SECRET" in the "Advanced Key" field
5. Click "Encrypt" button
6. Result: "Wphsg, Ogioe!"

### Brute Force Decryption ⊩

When you don't know the shift value, brute force tries all possible shifts (0-25).

#### Command Line 👩🏻‍💻

```bash
# Brute force an encrypted message
python caesar_cli.py brute "Khoor, Zruog!"
```

Output:
```
Shift | Result
----------------------------------------
    0 | Khoor, Zruog!
    1 | Jgnnq, Yqtnf!
    2 | Ifmmp, Xpsme!
    3 | Hello, World!    <-- The correct decryption appears here
    4 | Gdkkn, Vnqkc!
    ...
```

#### Web Interface 🕸️

1. Navigate to the "Brute Force" tab
2. Enter "Khoor, Zruog!" in the message field
3. Click "Try All Shifts"
4. The results will show all 26 possible decryptions, with the correct one typically being recognizable as readable English text

### Frequency Analysis

This feature analyzes the frequency of characters in the text, which is useful for cryptanalysis as certain letters appear more frequently in English.

#### Command Line

```bash
# Analyze character frequency in a text
python caesar_cli.py analyze "The quick brown fox jumps over the lazy dog"
```

Output:
```
Character | Frequency
-------------------------
e         | 0.0750
o         | 0.0750
r         | 0.0500
t         | 0.0500
...
```

#### Web Interface

1. Navigate to the "Frequency Analysis" tab
2. Enter a longer piece of text
3. Click "Analyze"
4. You'll see a bar chart of character frequencies and a table with exact percentages

### Automatic Decryption

This feature attempts to automatically decrypt text based on English letter frequency patterns.

#### Command Line

```bash
# Auto decrypt an encrypted message
python caesar_cli.py auto "Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj"
```

Output:
```
Potential decryptions based on frequency analysis:
Shift | Result
----------------------------------------
    3 | The quick brown fox jumps over the lazy dog
   15 | Ftq cguow ndaiz raj vgybe ahqd ftq xmlk pas
   18 | Cqn zrflt yaxjw oxg sdrmp xena cqn wjih mxp
    8 | Ocz lpdxf wmjri ajs ephkn jqzm ocz gvut yjb
   21 | Znk wqaiq vtwue jsy paiil tazn znk gfev iti
```

#### Web Interface

1. Navigate to the "Auto Decrypt" tab
2. Enter an encrypted message like "Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj"
3. Set the number of top results (default 5)
4. Click "Auto Decrypt"
5. Review the potential decryptions, with the most likely option typically listed first

### Working with Files

You can also process files instead of typing messages directly:

```bash
# Create a text file with content to encrypt
echo "This is a secret message" > secret.txt

# Encrypt the file content
python caesar_cli.py encrypt -f secret.txt -s 10 > encrypted.txt

# Decrypt the file
python caesar_cli.py decrypt -f encrypted.txt -s 10
# Output: This is a secret message
```

## Security Considerations

- The basic Caesar Cipher is a classic example of substitution cipher but is not secure for modern cryptographic purposes.
- The advanced Caesar Cipher with key-based shifting adds complexity but is still vulnerable to frequency analysis.
- This project is intended for educational purposes to demonstrate basic cryptography principles.

## Project Structure

- `caesar_cipher.py` - Core implementation of the cipher algorithms
- `caesar_cli.py` - Command-line interface
- `web_interface.py` - Web server and API endpoints
- `templates/index.html` - Web interface frontend

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
