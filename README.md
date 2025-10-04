# PDF Creator — Python Solutions E-Book Generator

> **Status:** Early preview (v0). This project is actively being developed.  
> It may behave unexpectedly and can produce errors. Use at your own risk.

## Overview
This repository converts plain-text study notes into a single, nicely formatted PDF.  
Each `.txt` file represents one topic; the **first line is the section title**, and the remaining lines are the content. The app reads all `.txt` files from a folder and compiles them into a multi-page e-book.

## Features
- 📂 Reads **all** `.txt` files from a source folder (sorted by filename)
- 🧾 **First line → section title**, rest → body
- 🖨️ Outputs a single PDF into `result/`
- 🔤 Unicode support via system TTF fonts (e.g., Arial / Consolas on Windows)

## Folder Structure
```text
eBook_creator/
├─ software/
│  └─ app.py
├─ sorce_txt_files/      # place your .txt files here
│  ├─ 01_variables.txt
│  ├─ 02_loops.txt
│  └─ ...
└─ result/               # generated PDFs appear here
```

## Requirements
- Python 3.10+
- Install dependency:
```bash
pip install fpdf2
```

## Quick Start
```bash
# 1) Put your .txt files into: eBook_creator/sorce_txt_files/
# 2) Run the script from the software/ directory:
cd eBook_creator/software
python app.py
# 3) Find the PDF here:
#    eBook_creator/result/solutions_book.pdf
```

## TXT File Format (example)
```text
Loops
A loop repeats code. In Python:
- for iterates over an iterable
- while runs while a condition is True

for i in range(5):
    print(i)
```

## Configuration
Open `software/app.py` and adjust:
```text
SRC_DIR  – source .txt directory
OUT_PDF  – output PDF path/name
Fonts    – optional: the script tries common Windows TTF fonts 
           (e.g., C:\Windows\Fonts\arial.ttf, C:\Windows\Fonts\consola.ttf).
           You can also point to a custom Unicode TTF (e.g., DejaVuSans.ttf).
```

## Troubleshooting
```text
FileNotFoundError: ... sorce_txt_files
→ Ensure the folder name/path is correct and you are running the script from software/.

UnicodeEncodeError: 'latin-1' codec ...
→ Use a Unicode TTF font. Set a valid TTF path 
  (e.g., C:\Windows\Fonts\arial.ttf or C:\Windows\Fonts\consola.ttf).

TTF Font file not found
→ Verify the font file exists at the specified path.

Empty or missing pages
→ Check that .txt files actually exist in sorce_txt_files/ and are not empty.
```

## Roadmap
- Auto-generated Table of Contents  
- Cover page (title / author / date)  
- Section grouping by subfolders (Loops / Functions / Classes …)  
- CLI arguments (custom source/output paths)  
- Optional Markdown support  

## License
MIT — do what you like; attribution appreciated.
