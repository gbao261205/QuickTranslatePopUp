# DisplayWindow.py
import tkinter as tk

class DisplayWindow:
    def __init__(self, text="Chờ văn bản...", width=450, height=200):
        self.text = text
        self.width = width
        self.height = height
        self.on_close_callback = None  # Gán sau từ main nếu cần

        self.root = tk.Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("Trình hiển thị văn bản")
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

        # Frame chứa Text + Scrollbar
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Scrollbar dọc
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text widget thay cho Label, có wrap và font
        self.text_widget = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12), yscrollcommand=scrollbar.set)
        self.text_widget.insert(tk.END, self.text)
        self.text_widget.config(state=tk.DISABLED)  # Không cho người dùng chỉnh sửa
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Gán scrollbar điều khiển text
        scrollbar.config(command=self.text_widget.yview)

    def update_text(self, new_text):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, new_text)
        self.text_widget.config(state=tk.DISABLED)

    def set_on_close(self, callback):
        self.on_close_callback = callback

    def _on_close(self):
        print("❌ Đã đóng cửa sổ.")
        if self.on_close_callback:
            self.on_close_callback()
        self.root.destroy()

    def run(self):
        self.root.mainloop()
