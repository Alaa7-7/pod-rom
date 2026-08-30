from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


doc = SimpleDocTemplate("POD_ROM_Paper.pdf")

styles = getSampleStyleSheet()
content = []


# Title
content.append(
    Paragraph(
        "Reduced Order Modeling (POD) for 2D Heat Equation",
        styles["Title"]
    )
)

content.append(Spacer(1, 15))


# Project idea
content.append(
    Paragraph(
        "In this project, I solve a simple 2D heat equation using Python. "
        "I use a finite difference method to calculate the temperature over time. "
        "Then I use POD and SVD to reduce the amount of data.",
        styles["Normal"]
    )
)

content.append(Spacer(1, 10))


# Heat equation
content.append(
    Paragraph(
        "Heat Equation: dT/dt = alpha * (d2T/dx2 + d2T/dy2)",
        styles["Normal"]
    )
)

content.append(Spacer(1, 10))


# Numerical settings
content.append(
    Paragraph(
        "Numerical settings: grid = 50 x 50, dx = 1.0, dy = 1.0, dt = 0.1, "
        "and 100 time steps.",
        styles["Normal"]
    )
)

content.append(Spacer(1, 10))


# Initial condition
content.append(
    Paragraph(
        "The temperature starts at zero. I put a hot square in the middle "
        "of the grid with temperature 1.0. The boundary temperature stays at zero.",
        styles["Normal"]
    )
)

content.append(Spacer(1, 10))


# Training
content.append(
    Paragraph(
        "Training parameters: alpha = 0.1, 0.5, and 1.0. "
        "I combine the snapshots from these values and build one common POD basis.",
        styles["Normal"]
    )
)

content.append(Spacer(1, 10))


# POD
content.append(
    Paragraph(
        "I use SVD to find the main patterns in the training data. "
        "I use the energy of the singular values to choose the number of POD modes.",
        styles["Normal"]
    )
)

content.append(Spacer(1, 10))


# Energy
content.append(
    Paragraph(
        "The first 3 POD modes contain about 99.93% of the training energy.",
        styles["Normal"]
    )
)

content.append(Spacer(1, 10))


# Test
content.append(
    Paragraph(
        "Test parameter: alpha = 0.75. "
        "This value was not used during training. "
        "I use it to test the common POD basis.",
        styles["Normal"]
    )
)

content.append(Spacer(1, 10))


# Error
content.append(
    Paragraph(
        "The relative approximation error for the test parameter is "
        "0.0068056, which is about 0.68%.",
        styles["Normal"]
    )
)

content.append(Spacer(1, 10))


# Conclusion
content.append(
    Paragraph(
        "Conclusion: I used a simple POD approach for the 2D heat equation. "
        "Three POD modes keep about 99.93% of the training energy. "
        "The unseen test parameter alpha = 0.75 gives an approximation error "
        "of about 0.68%.",
        styles["Normal"]
    )
)


doc.build(content)

print("PDF generated: POD_ROM_Paper.pdf")