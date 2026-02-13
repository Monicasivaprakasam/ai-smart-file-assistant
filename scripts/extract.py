import fitz  # PyMuPDF

pdf_path = "../input/sample.pdf"
doc = fitz.open(pdf_path)

all_text = ""

for page in doc:
    text = page.get_text()
    all_text += text + "\n"

with open("../output/raw.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("Extraction Completed Successfully!")
