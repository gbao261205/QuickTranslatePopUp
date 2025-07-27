# Translate.py
from googletrans import Translator

class TextTranslator:
    def __init__(self, dest_lang='vi'):
        self.dest_lang = dest_lang
        self.translator = Translator()

    def translate(self, text):
        try:
            translated = self.translator.translate(text, dest=self.dest_lang)
            return translated.text
        except Exception as e:
            print(f"❌ Lỗi khi dịch: {e}")
            return "[Lỗi dịch]"
