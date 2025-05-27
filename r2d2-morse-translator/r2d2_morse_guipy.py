import tkinter as tk
from tkinter import scrolledtext, messagebox
from r2d2_morse_translator import lettersToMorseCode, morseCodeToLetters

class MorseTranslatorGUI:
    def __init__(self, root):
        self.root = root
        root.title("R2-D2 Morse Code Translator")

        # Input label and text box
        tk.Label(root, text="Input:").grid(row=0, column=0, sticky='w')
        self.input_text = scrolledtext.ScrolledText(root, height=5, width=50)
        self.input_text.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        # Output label and text box
        tk.Label(root, text="Output:").grid(row=2, column=0, sticky='w')
        self.output_text = scrolledtext.ScrolledText(root, height=5, width=50, state='disabled')
        self.output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

        # Encode button
        self.encode_button = tk.Button(root, text="Encode to Morse", command=self.encode)
        self.encode_button.grid(row=4, column=0, pady=10)

        # Decode button
        self.decode_button = tk.Button(root, text="Decode from Morse", command=self.decode)
        self.decode_button.grid(row=4, column=1, pady=10)

        # Clear button
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_all)
        self.clear_button.grid(row=4, column=2, pady=10)

    def encode(self):
        input_str = self.input_text.get('1.0', tk.END).strip()
        if not input_str:
            messagebox.showinfo("Info", "Please enter text to encode.")
            return
        encoded = lettersToMorseCode(input_str)
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, encoded)
        self.output_text.config(state='disabled')

    def decode(self):
        input_str = self.input_text.get('1.0', tk.END).strip()
        if not input_str:
            messagebox.showinfo("Info", "Please enter Morse code to decode.")
            return
        decoded = morseCodeToLetters(input_str)
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, decoded)
        self.output_text.config(state='disabled')

    def clear_all(self):
        self.input_text.delete('1.0', tk.END)
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseTranslatorGUI(root)
    root.mainloop()
