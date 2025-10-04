from fpdf import FPDF
import os

SRC_DIR = r"C:\Users\Alvin\Desktop\eBook_creator\sorce_txt_files"
OUT_PDF = r"C:\Users\Alvin\Desktop\eBook_creator\result\solutions_book.pdf"

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\arialuni.ttf",
    r"C:\Windows\Fonts\segoeui.ttf",
    r"C:\Windows\Fonts\calibri.ttf",
    r"C:\Windows\Fonts\verdana.ttf",
    r"C:\Windows\Fonts\tahoma.ttf",
]
MONO_CANDIDATES = [
    r"C:\Windows\Fonts\consola.ttf",
    r"C:\Windows\Fonts\lucon.ttf",
]

def pick_first_existing(paths):
    for p in paths:
        if os.path.isfile(p):
            return p
    return None

def create_pdf(filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    main_ttf = pick_first_existing(FONT_CANDIDATES)
    mono_ttf = pick_first_existing(MONO_CANDIDATES)

    if not main_ttf:
        raise RuntimeError("Something went wrong!")

    pdf.add_font("Main", "", main_ttf, uni=True)
    if mono_ttf:
        pdf.add_font("Mono", "", mono_ttf, uni=True)
    else:
        pdf.add_font("Mono", "", main_ttf, uni=True)

    txt_files = sorted(f for f in os.listdir(SRC_DIR) if f.lower().endswith(".txt"))
    if not txt_files:
        print("No .txt files found.")
        return

    for fname in txt_files:
        path = os.path.join(SRC_DIR, fname)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.read().splitlines()

        if lines:
            title = (lines[0] or fname).strip()
            body  = "\n".join(lines[1:]).strip()
        else:
            title = fname
            body  = ""

        pdf.add_page()

        pdf.set_font("Main", "", 18)
        pdf.cell(0, 10, title if title else "(no title)", ln=1)

        pdf.set_font("Mono", "", 11)
        pdf.multi_cell(0, 6, body if body else "(no content)")
        pdf.ln(2)

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    pdf.output(filename)
    print(f"PDF created: {filename}")

if __name__ == "__main__":
    create_pdf(OUT_PDF)
