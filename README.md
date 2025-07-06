# File Converter App

This simple GUI application converts files between a few common formats. It is built with Python's Tkinter library to provide a user-friendly interface with buttons instead of command-line usage.

## Supported Conversions

Currently the app can:

- Convert a PNG image to JPEG.
- Convert a JPEG image to PNG.
- Convert a plain text (`.txt`) file to a PDF.

These options can be extended by adding more conversion functions.

## Setup

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python file_converter_app.py
```

A window will open where you can select a file, choose the conversion type, and click **Convert**.

## Notes

- This is a minimal example and does not handle every possible file type or extremely large files. Additional libraries may be needed to support more formats.
- Image conversion uses the Pillow library, and text-to-PDF conversion uses fpdf2.

