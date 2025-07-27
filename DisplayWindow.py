# DisplayWindow.py
import tkinter as tk

class DisplayWindow:
    def __init__(self, text="Chờ văn bản...", width=300, height=100):
        self.text = text
        self.width = width
        self.height = height
        self.on_close_callback = None  # Gán sau từ main nếu cần

        self.root = tk.Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("Trình hiển thị văn bản")
        self.root.attributes("-topmost", True)

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

        self.label = tk.Label(self.root, text=self.text, font=("Arial", 12), wraplength=self.width-20)
        self.label.pack(expand=True, fill="both", padx=10, pady=10)

    def update_text(self, new_text):
        self.label.config(text=new_text)

    def set_on_close(self, callback):
        self.on_close_callback = callback

    def _on_close(self):
        print("❌ Đã đóng cửa sổ.")
        if self.on_close_callback:
            self.on_close_callback()
        self.root.destroy()

    def run(self):
        self.root.mainloop()
