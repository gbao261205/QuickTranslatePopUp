# 📘 Instant Text Translator (Popup Translator for Windows)

A lightweight Windows desktop tool that automatically translates any text you highlight — and instantly displays the translation in a popup window near your cursor.

Ideal for reading foreign-language content, studying, or fast on-screen translation — without switching applications.

# ✨ Features

+ Auto-translate highlighted text (no need to press keys)

+ Supports multiple languages (select from a dropdown)

+ Popup display window for translations

+ Fast & responsive — minimal delay after highlighting text\

+ Works in any application: browser, Word, PDF, etc.

+ Privacy-friendly: does not store any text


# 📦 Installation
1. Clone or download this repository:
   
+ git clone https://github.com/gbao261205/QuickTranslatePopUp.git

2. Install required packages (Please using Python version 3.12 or under and not using Python 3.13):
   
+ pip install pyperclip pyautogui pynput googletrans==4.0.0rc1

3. Run the app:

+ python main.py

# 🛠 Dependencies:

Make sure Python 3.12 (Recommended) is installed. Required libraries:
+ pyperclip
+ pyautogui
+ pynput
+ tkinter (usually comes with Python)
+ googletrans==4.0.0rc1 (or your chosen translation backend)

# 🧠 How It Works

You highlight any text on screen (left-click release).

The app simulates Ctrl+C to copy it.

The copied text is sent to a translator module (Google Translate API by default).

The translated text is shown in a popup window.

Note: After typing the text, please click back on the application window to continue using it.

# 🌍 Supported Languages

You can choose from dozens of languages including:

+ English (en)

+ Vietnamese (vi)

+ Japanese (ja)

+ French (fr)

+ Chinese (zh-cn)

+ ... and more.

# 🧩 Customization

Change translation engine (e.g., DeepL, Microsoft Translator)

Customize UI in DisplayWindow.py

Modify behavior in GetText.py

# 🚫 Limitations

Currently optimized for Windows OS.

May not work with protected applications that block clipboard access.

Translation speed depends on your internet connection and API speed.

# 📄 License

MIT License. Feel free to modify and use for both personal and commercial purposes.

# 🙏 Acknowledgements

Google Translate — for powering the translation engine via the googletrans Python library.

OpenAI ChatGPT — for supporting development with AI-powered guidance, debugging, and writing support.
