import unittest
from r2d2_morse_translator import lettersToMorseCode, morseCodeToLetters

class TestMorseTranslator(unittest.TestCase):
    def test_encode_basic(self):
        self.assertEqual(
            lettersToMorseCode("SOS"),
            "... --- ..."
        )

    def test_encode_with_space_and_punctuation(self):
        self.assertEqual(
            lettersToMorseCode("Hi!"),
            ".... .. -.-.--"
        )

    def test_decode_basic(self):
        self.assertEqual(
            morseCodeToLetters("... --- ..."),
            "SOS"
        )

    def test_decode_with_space_and_punctuation(self):
        self.assertEqual(
            morseCodeToLetters(".... .. / -.-.--"),
            "HI !"
        )

    def test_encode_empty(self):
        self.assertEqual(
            lettersToMorseCode(""),
            ""
        )

    def test_decode_empty(self):
        self.assertEqual(
            morseCodeToLetters(""),
            ""
        )

    def test_unknown_characters_ignored(self):
        # '@' is supported, but let's test an unsupported character like '#'
        self.assertEqual(
            lettersToMorseCode("Hello#"),
            ".... . .-.. .-.. ---"
        )
        # For decoding, unknown Morse should be ignored
        self.assertEqual(
            morseCodeToLetters(".... . .-.. .-.. --- ...-.-"),
            "HELLO"
        )

if __name__ == '__main__':
    unittest.main()