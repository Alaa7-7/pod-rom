import numpy as np

energy = np.load("energy_modes.npy")
cum_energy = np.load("energy_cumulative.npy")

with open("energy_plot.csv", "w") as f:
    f.write("mode,energy,cumulative\n")
    for i in range(len(energy)):
        f.write(f"{i+1},{energy[i]},{cum_energy[i]}\n")

print("Energy CSV generated: energy_plot.csv")