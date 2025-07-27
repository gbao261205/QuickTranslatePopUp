from DisplayWindow import DisplayWindow
from GetText import ClipboardWatcher
from Translate import TextTranslator
import threading

def on_new_text(text):
    translated = translator.translate(text)
    window.update_text(translated)

def stop_everything():
    print("🛑 Đã tắt cửa sổ, dừng chương trình.")
    if watcher:
        watcher.stop()

if __name__ == "__main__":
    # Tạo đối tượng Translator
    translator = TextTranslator(dest_lang='vi')  # hoặc thay đổi sang 'en', 'ja', v.v.

    # Khởi tạo watcher trước
    watcher = ClipboardWatcher(callback=on_new_text)
    watcher_thread = threading.Thread(target=watcher.start, daemon=True)
    watcher_thread.start()

    # Sau đó tạo cửa sổ
    window = DisplayWindow("🚀 Đang theo dõi văn bản bạn bôi đen...")
    window.set_on_close(stop_everything)

    # Chạy giao diện
    window.run()

    print("✅ Chương trình đã kết thúc.")
