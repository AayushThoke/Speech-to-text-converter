import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox
import threading

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def record_voice():
    def listen_and_display():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            status_label.config(text="Listening...", fg="#FF6B6B")
            root.update()
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language='en')
                text_display.delete("1.0", tk.END)
                text_display.insert(tk.END, text)
                with open('you_said_this.txt', 'w') as file:
                    file.write(text)
                status_label.config(text="Speech recognized and saved!", fg="#4CAF50")
            except sr.UnknownValueError:
                status_label.config(text="I didn't understand what you said.", fg="#FF6B6B")
            except sr.RequestError:
                status_label.config(text="Could not request results, check your internet.", fg="#FF6B6B")
    
    thread = threading.Thread(target=listen_and_display)
    thread.start()

def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showerror("Error", "Please enter text to convert to speech.")

def speak_recognized_text():
    text = text_display.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showerror("Error", "No recognized text available.")

# GUI setup
root = tk.Tk()
root.title("Speech to Text & Text to Speech Converter")
root.geometry("400x500")
root.configure(bg="#F8EDEB")

status_label = tk.Label(root, text="Click the mic to start speaking", font=("Arial", 12), bg="#F8EDEB", fg="#6D6875")
status_label.pack(pady=10)

record_button = tk.Button(root, text="🎤", command=record_voice, font=("Arial", 20), bg="#A1A1A1", fg="#FFFFFF", relief=tk.FLAT, width=3, height=1, bd=0)
record_button.pack(pady=10)
record_button.config(borderwidth=2, highlightbackground="#FFFFFF", activebackground="#888888")

text_display = tk.Text(root, height=5, width=50, font=("Arial", 12), bg="#FFEBE5", fg="#6D6875", bd=0, wrap=tk.WORD)
text_display.pack(pady=10, padx=10)

speak_button = tk.Button(root, text="🔊", command=speak_recognized_text, font=("Arial", 12), bg="#A1A1A1", fg="#FFFFFF", relief=tk.FLAT, width=10, height=1, bd=0)
speak_button.pack(pady=5)
speak_button.config(borderwidth=2, highlightbackground="#FFFFFF", activebackground="#888888")

text_entry_label = tk.Label(root, text="Enter Text for Speech:", font=("Arial", 12), bg="#F8EDEB", fg="#6D6875")
text_entry_label.pack(pady=5)

text_entry = tk.Text(root, height=5, width=50, font=("Arial", 12), bg="#FFEBE5", fg="#6D6875", bd=0, wrap=tk.WORD)
text_entry.pack(pady=10, padx=10)

speak_text_button = tk.Button(root, text="🔊 Speak", command=text_to_speech, font=("Arial", 12), bg="#A1A1A1", fg="#FFFFFF", relief=tk.FLAT, width=10, height=1, bd=0)
speak_text_button.pack(pady=10)
speak_text_button.config(borderwidth=2, highlightbackground="#FFFFFF", activebackground="#888888")

root.mainloop()