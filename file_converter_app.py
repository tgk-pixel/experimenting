import os
import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image
from fpdf import FPDF


class FileConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Converter")
        self.file_path = tk.StringVar()
        self.selected_option = tk.StringVar(value="image_png_to_jpeg")

        # File selection
        tk.Button(master, text="Select File", command=self.select_file).pack(pady=5)
        tk.Entry(master, textvariable=self.file_path, width=50).pack(pady=5)

        # Conversion type
        options = [
            ("Image: PNG to JPEG", "image_png_to_jpeg"),
            ("Image: JPEG to PNG", "image_jpeg_to_png"),
            ("Text file to PDF", "text_to_pdf"),
        ]
        tk.Label(master, text="Conversion Type").pack(pady=(10, 0))
        self.option_menu = tk.Frame(master)
        self.option_menu.pack(pady=5)
        for text, value in options:
            tk.Radiobutton(self.option_menu, text=text, variable=self.selected_option, value=value).pack(anchor=tk.W)

        tk.Button(master, text="Convert", command=self.convert).pack(pady=10)

    def select_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_path.set(path)

    def convert(self):
        path = self.file_path.get()
        option = self.selected_option.get()
        if not path:
            messagebox.showerror("Error", "Please select a file first.")
            return
        try:
            if option == "image_png_to_jpeg":
                self.png_to_jpeg(path)
            elif option == "image_jpeg_to_png":
                self.jpeg_to_png(path)
            elif option == "text_to_pdf":
                self.text_to_pdf(path)
            else:
                messagebox.showerror("Error", "Unsupported conversion option.")
                return
            messagebox.showinfo("Success", "File converted successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def png_to_jpeg(self, path):
        img = Image.open(path)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        base, _ = os.path.splitext(path)
        output = base + ".jpg"
        img.save(output, "JPEG")

    def jpeg_to_png(self, path):
        img = Image.open(path)
        base, _ = os.path.splitext(path)
        output = base + ".png"
        img.save(output, "PNG")

    def text_to_pdf(self, path):
        base, _ = os.path.splitext(path)
        output = base + ".pdf"
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                pdf.multi_cell(0, 10, txt=line.rstrip())
        pdf.output(output)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()
