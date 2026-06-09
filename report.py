from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Create PDF file
doc = SimpleDocTemplate("POD_Report.pdf")

styles = getSampleStyleSheet()
content = []

# Title
content.append(Paragraph("POD Reduced Order Model (ROM) for 2D Heat Equation", styles["Title"]))
content.append(Spacer(1, 12))

# Abstract
abstract = """
This project implements a Reduced Order Model (ROM) using Proper Orthogonal Decomposition (POD)
applied to a 2D heat diffusion system. The goal is to reduce computational complexity while
preserving dominant dynamics.
"""
content.append(Paragraph("Abstract", styles["Heading2"]))
content.append(Paragraph(abstract, styles["BodyText"]))
content.append(Spacer(1, 12))

# Methodology
method = """
The system is decomposed using Singular Value Decomposition (SVD) into orthogonal modes.
A reduced basis is constructed by selecting the most energetic modes representing 99% of the system energy.
"""
content.append(Paragraph("Methodology", styles["Heading2"]))
content.append(Paragraph(method, styles["BodyText"]))
content.append(Spacer(1, 12))

# Results
results = """
The model achieves significant dimensionality reduction, requiring only 2 POD modes while maintaining
a relative reconstruction error of approximately 1.3%.
"""
content.append(Paragraph("Results", styles["Heading2"]))
content.append(Paragraph(results, styles["BodyText"]))
content.append(Spacer(1, 12))

# Conclusion
conclusion = """
The POD-based Reduced Order Model successfully captures the dominant dynamics of the system,
making it suitable for efficient simulations and real-time applications.
"""
content.append(Paragraph("Conclusion", styles["Heading2"]))
content.append(Paragraph(conclusion, styles["BodyText"]))

# Build PDF
doc.build(content)

print("PDF generated: POD_Report.pdf")