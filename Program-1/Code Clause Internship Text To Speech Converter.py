# Imports
import tkinter as tk
from tkinter import ttk, messagebox
import pyttsx3

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Converter")
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.rate = self.engine.getProperty('rate')
        self.create_widgets()

# Defining a function to create widgets
    def create_widgets(self):

        # Input text
        self.text_label = ttk.Label(self.root, text="Enter text:")
        self.text_label.pack(pady=5)
        self.text_entry = tk.Text(self.root, height=10, width=50)
        self.text_entry.pack(pady=5)
        
        # Voice selection
        self.voice_label = ttk.Label(self.root, text="Select voice:")
        self.voice_label.pack(pady=5)
        self.voice_combo = ttk.Combobox(self.root, values=[voice.name for voice in self.voices])
        self.voice_combo.pack(pady=5)
        
        # Speech rate
        self.rate_label = ttk.Label(self.root, text="Set speech rate:")
        self.rate_label.pack(pady=5)
        self.rate_scale = ttk.Scale(self.root, from_=50, to=300, orient=tk.HORIZONTAL)
        self.rate_scale.set(self.rate)
        self.rate_scale.pack(pady=5)

        # Convert button
        self.convert_button = ttk.Button(self.root, text="Convert to Speech", command=self.convert_to_speech)
        self.convert_button.pack(pady=20)

# Defining a function to convert text to speech    
    def convert_to_speech(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter some text to convert.")
            return
        selected_voice = self.voice_combo.get()
        for voice in self.voices:
            if voice.name == selected_voice:
                self.engine.setProperty('voice', voice.id)
                break
        self.engine.setProperty('rate', int(self.rate_scale.get()))
        self.engine.say(text)
        self.engine.runAndWait()

# Main loop
def main():
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()