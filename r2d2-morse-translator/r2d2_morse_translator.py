#!/usr/bin/env python3
"""
R2-D2 Morse Code Translator
---------------------------
Encode and decode messages between plain text and Morse code.

Usage:
  Encode text:
    python r2d2_morse_translator.py --encode "Help me Obi-Wan!"
  Decode Morse code:
    python r2d2_morse_translator.py --decode ".... . .-.. .--. / -- . / --- -... .. -....- .-- .- -. -.-.--"
"""

import argparse

# 📡 Morse code dictionary mapping letters, digits, and punctuation to Morse signals
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',   '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',  '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# 🔁 Reverse dictionary for decoding Morse back to plain text
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def lettersToMorseCode(text: str) -> str:
    """
    Convert plain text to Morse code.
    Spaces become '/' in Morse.
    Unsupported characters are skipped.
    """
    morse_chars = []
    for char in text.upper():
        morse_char = MORSE_CODE_DICT.get(char)
        if morse_char is not None:
            morse_chars.append(morse_char)
        else:
            # Skip unknown characters but log for debugging
            # print(f"Warning: Unsupported character '{char}' skipped.")
            pass
    return ' '.join(morse_chars)

def morseCodeToLetters(code: str) -> str:
    """
    Convert Morse code to plain text.
    '/' is treated as space.
    Unknown Morse sequences are skipped.
    """
    words = code.strip().split(' / ')
    decoded_words = []
    for word in words:
        letters = []
        for morse_char in word.split():
            letter = REVERSE_MORSE_CODE_DICT.get(morse_char)
            if letter is not None:
                letters.append(letter)
            else:
                # Skip unknown Morse sequences but log for debugging
                # print(f"Warning: Unknown Morse '{morse_char}' skipped.")
                pass
        decoded_words.append(''.join(letters))
    return ' '.join(decoded_words)

def main():
    parser = argparse.ArgumentParser(description="R2-D2 Morse Code Translator")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--encode', '-e', type=str, help='Text to encode into Morse code')
    group.add_argument('--decode', '-d', type=str, help='Morse code to decode into text')
    args = parser.parse_args()

    if args.encode:
        result = lettersToMorseCode(args.encode)
        print(f"Encoded Morse Code:\n{result}")
    elif args.decode:
        result = morseCodeToLetters(args.decode)
        print(f"Decoded Text:\n{result}")

if __name__ == "__main__":
    main()
