import argparse

# 📡 Morse code dictionary mapping letters, digits, and punctuation to Morse signals
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.',
    ' ': '/'
}

def encode_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def decode_from_morse(morse_code):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict.get(code, '') for code in morse_code.split())

def main():
    parser = argparse.ArgumentParser(description="R2-D2 Morse Code Translator")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--encode', type=str, help="Text message to encode to Morse code")
    group.add_argument('--decode', type=str, help="Morse code message to decode to text")

    args = parser.parse_args()

    if args.encode:
        encoded = encode_to_morse(args.encode)
        print("\nEncoded Morse Code:")
        print(encoded)

    if args.decode:
        decoded = decode_from_morse(args.decode)
        print("\nDecoded Text:")
        print(decoded)

if __name__ == "__main__":
    main()
