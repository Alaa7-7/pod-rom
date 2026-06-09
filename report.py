from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import numpy as np

# Load data
energy = np.load("energy_modes.npy")
cum_energy = np.load("energy_cumulative.npy")

doc = SimpleDocTemplate("POD_ROM_Paper.pdf")
styles = getSampleStyleSheet()
content = []

# Title
content.append(Paragraph("Reduced Order Modeling (POD-ROM) for 2D Heat Equation", styles["Title"]))
content.append(Spacer(1, 12))

# Abstract
content.append(Paragraph(
"This project presents a POD-based reduced order model for the 2D heat equation using SVD.",
styles["Normal"]))
content.append(Spacer(1, 12))

# Governing equation (ASCII safe)
content.append(Paragraph(
"Governing Equation: dT/dt = alpha * (d2T/dx2 + d2T/dy2)",
styles["Normal"]))
content.append(Spacer(1, 12))

# Energy table
data = [["Mode", "Energy", "Cumulative Energy"]]

for i in range(len(energy)):
    data.append([
        str(i + 1),
        str(round(float(energy[i]), 6)),
        str(round(float(cum_energy[i]), 6))
    ])

table = Table(data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.grey),
    ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
    ("GRID", (0,0), (-1,-1), 0.5, colors.black),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
]))

content.append(table)

# Build PDF
doc.build(content)

print("PDF generated: POD_ROM_Paper.pdf")
