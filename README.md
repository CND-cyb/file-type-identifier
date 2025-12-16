# File Type Identifier

A lightweight cybersecurity tool written in Python to detect **Extension Spoofing** attempts.
It analyzes files based on their **Magic Numbers** (file signatures) rather than their extensions, ensuring that a file claiming to be a `.jpg` isn't actually a malicious `.exe`.

## 🚀 Features

- **Magic Number Detection**: Identifies real file types by reading the first 20 bytes (Hex Signature).
- **Extension Mismatch Alert**: Compares the detected signature against the file extension and alerts on mismatches.
- **Recursive Scanning**: Can analyze a single file or walk through entire directories recursively.
- **Silent Mode**: In directory mode, it only reports anomalies to reduce noise.
- **Safe Handling**: Robust error handling for missing files or permission issues.

## 🛠️ Supported Formats

Currently supports detection for:
- PDF
- JPEG / PNG / GIF
- ZIP / RAR
- EXE (Windows Executables)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/TON_USER/file-type-identifier.git](https://github.com/TON_USER/file-type-identifier.git)
   ```
2. Navigate to the folder:
   ```bash
   cd file-type-identifier
   ```
3. No external dependencies required (uses standard Python libraries: os, argparse).

## 💻 Usage

* Analyze a single file
    ```bash
    python scanner.py -f suspicious_image.jpg
    ```
*Output:
    The file type is: jpg OR ALERT MISMATCH! The file type is : exe*

* Scan a directory (Recursive)
    ```bash
    python scanner.py -d C:/Downloads
    ```
*Output:
    ...................................
    - ALERT MISMATCH! The file type of vacation_photo.jpg is : exe*

## 📚 Sources
* [Wikipedia - List of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
* [GitHub - List of file signatures](https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5)
* [Python - Documentation argparse](https://docs.python.org/fr/3/howto/argparse.html)
* [W3Schools - Documentation os.walk()](https://www.w3schools.com/python/ref_os_walk.asp)
* [GeeksForGeeks - Documentation os.path.splitext()](https://www.geeksforgeeks.org/python/python-os-path-splitext-method/)
* [GeeksForGeeks - Documentation os.path.join()](https://www.geeksforgeeks.org/python/python-os-path-join-method/)
* [DataCamp - Print without new line](https://www.datacamp.com/tutorial/python-print-without-new-line?dc_referrer=https%3A%2F%2Fwww.google.com%2F)

## ⚠️ Disclaimer
This tool is for **educational and defensive purposes**. It is designed to help system administrators and security enthusiasts audit their file systems.
