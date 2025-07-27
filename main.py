from DisplayWindow import DisplayWindow
from GetText import ClipboardWatcher
import threading

def on_new_text(text):
    window.update_text(text)

def stop_everything():
    print("🛑 Đã tắt cửa sổ, dừng chương trình.")
    if watcher:
        watcher.stop()

if __name__ == "__main__":
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
