import pyautogui
import pyperclip
import time
import threading
from pynput import mouse, keyboard

class ClipboardWatcher:
    def __init__(self, callback=None):
        """
        callback: một hàm nhận 1 đối số là văn bản mới được copy
        """
        self.last_text = ""
        self.callback = callback
        self.mouse_listener = None
        self.keyboard_listener = None
        self.running = False  # Để kiểm soát việc chạy

    def _handle_copy(self):
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        new_text = pyperclip.paste().strip()
        if new_text and new_text != self.last_text:
            self.last_text = new_text
            if self.callback:
                self.callback(new_text)

    def _on_click(self, x, y, button, pressed):
        if self.running and button == mouse.Button.left and not pressed:
            threading.Thread(target=self._handle_copy, daemon=True).start()

    def _on_key_press(self, key):
        if key == keyboard.Key.esc:
            print("🛑 ESC được nhấn — dừng theo dõi.")
            self.stop()

    def start(self):
        print("🎯 Bắt đầu theo dõi clipboard. Nhấn ESC để dừng.")
        self.running = True

        self.mouse_listener = mouse.Listener(on_click=self._on_click)
        self.keyboard_listener = keyboard.Listener(on_press=self._on_key_press)

        self.keyboard_listener.start()
        self.mouse_listener.start()

        # Chờ đến khi mouse_listener dừng
        self.mouse_listener.join()

    def stop(self):
        self.running = False
        if self.mouse_listener:
            self.mouse_listener.stop()
        if self.keyboard_listener:
            self.keyboard_listener.stop()
