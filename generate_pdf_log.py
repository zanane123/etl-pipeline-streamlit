from fpdf import FPDF
from datetime import datetime

# Nom du log
log_file = "etl.log"

# Nom dynamique du PDF
date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
pdf_file = f"etl_log_{date_str}.pdf"

# Créer le PDF
pdf = FPDF()
pdf.add_page()

# ✅ Police UTF-8
pdf.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf', uni=True)
pdf.set_font('DejaVu', '', 12)

# Lire le log ligne par ligne
with open(log_file, "r", encoding="utf-8") as f:
    for line in f:
        pdf.multi_cell(0, 10, line.strip())

pdf.output(pdf_file)
print(f"✅ PDF généré : {pdf_file}")
