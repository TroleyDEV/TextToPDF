import glob
from pathlib import Path

from fpdf import FPDF

filepaths = glob.glob("files/*.txt")

for filepath in filepaths:
    with open(filepath) as file:
        text = file.read()

    filename = Path(filepath).stem
    name = filename.title()

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=name, align="L")
    pdf.output(f"PDFs/{filename}.pdf")
