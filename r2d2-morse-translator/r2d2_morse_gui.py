import tkinter as tk
from r2d2_morse_translator import encode_to_morse, decode_from_morse

def encode():
    text = input_text.get("1.0", "end-1c")
    output = encode_to_morse(text)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", output)

def decode():
    morse = input_text.get("1.0", "end-1c")
    output = decode_from_morse(morse)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", output)

# GUI Setup
root = tk.Tk()
root.title("R2-D2 Morse Code Translator")

tk.Label(root, text="Input:").pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack()

tk.Button(root, text="Encode to Morse", command=encode).pack(pady=5)
tk.Button(root, text="Decode from Morse", command=decode).pack(pady=5)

tk.Label(root, text="Output:").pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

root.mainloop()
