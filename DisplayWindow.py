# DisplayWindow.py
import tkinter as tk
from tkinter import ttk

class DisplayWindow:
    def __init__(self, text="Chờ văn bản...", width=450, height=250):
        self.text = text
        self.width = width
        self.height = height
        self.on_close_callback = None

        self.root = tk.Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("Trình hiển thị văn bản")
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

        # ✅ Từ ngôn ngữ hiển thị sang mã ngôn ngữ
        self.lang_map = {
            "Tiếng Việt": "vi",
            "English": "en",
            "日本語 (Japanese)": "ja",
            "한국어 (Korean)": "ko",
            "中文 (Chinese)": "zh-cn",
            "Français (French)": "fr",
            "Deutsch (German)": "de",
            "Русский (Russian)": "ru",
            "Español (Spanish)": "es",
            "ภาษาไทย (Thai)": "th"
        }

        self.selected_lang_display = tk.StringVar(self.root, value="Tiếng Việt")  # Mặc định

        top_frame = tk.Frame(self.root)
        top_frame.pack(fill=tk.X, padx=10, pady=(10, 0), anchor='nw')

        tk.Label(top_frame, text="Ngôn ngữ đích:", font=("Arial", 10)).pack(side=tk.LEFT)

        self.lang_dropdown = ttk.Combobox(
            top_frame,
            textvariable=self.selected_lang_display,
            state="readonly",
            width=22,
            font=("Arial", 10),
            values=list(self.lang_map.keys())
        )
        self.lang_dropdown.pack(side=tk.LEFT, padx=5)

        # Vùng hiển thị văn bản + scroll
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_widget = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12), yscrollcommand=scrollbar.set)
        self.text_widget.insert(tk.END, self.text)
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.text_widget.yview)

    def update_text(self, new_text):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, new_text)
        self.text_widget.config(state=tk.DISABLED)

    def get_selected_lang(self):
        # Trả về mã ngôn ngữ dựa vào tên người dùng chọn
        return self.lang_map.get(self.selected_lang_display.get(), "vi")

    def set_on_close(self, callback):
        self.on_close_callback = callback

    def _on_close(self):
        print("❌ Đã đóng cửa sổ.")
        if self.on_close_callback:
            self.on_close_callback()
        self.root.destroy()

    def run(self):
        self.root.mainloop()
