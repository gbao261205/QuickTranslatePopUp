from DisplayWindow import DisplayWindow
from GetText import ClipboardWatcher
from Translate import TextTranslator
import threading

def on_new_text(text):
    # 👉 Lấy mã ngôn ngữ đích từ combobox trong DisplayWindow
    dest_lang_code = window.get_selected_lang()
    
    # 👉 Khởi tạo đối tượng dịch với mã ngôn ngữ đã chọn
    translator = TextTranslator(dest_lang=dest_lang_code)
    
    # 👉 Dịch văn bản clipboard
    translated = translator.translate(text)
    
    # 👉 Hiển thị kết quả dịch lên cửa sổ
    window.update_text(translated)

def stop_everything():
    print("🛑 Đã tắt cửa sổ, dừng chương trình.")
    if watcher:
        watcher.stop()

if __name__ == "__main__":
    # ✅ Tạo giao diện hiển thị văn bản trước
    window = DisplayWindow("🚀 Đang theo dõi văn bản bạn bôi đen...")
    window.set_on_close(stop_everything)

    # ✅ Bắt đầu theo dõi clipboard ở luồng nền
    watcher = ClipboardWatcher(callback=on_new_text)
    watcher_thread = threading.Thread(target=watcher.start, daemon=True)
    watcher_thread.start()

    # ✅ Bắt đầu giao diện chính
    window.run()

    print("✅ Chương trình đã kết thúc.")
