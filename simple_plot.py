import csv

alphas = []
errors = []

with open("alpha_vs_error.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        alphas.append(float(row["alpha"]))
        errors.append(float(row["error"]))

print("Alpha values:", alphas)
print("Error values:", errors)

print("Use Excel or LibreOffice to plot the data.")
