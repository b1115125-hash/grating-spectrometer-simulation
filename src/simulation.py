
import numpy as np
import matplotlib.pyplot as plt

# 1. Set wavelength range (nm)
wavelength = np.linspace(495, 505, 2000)

# 2. Define a Gaussian spectral peak
def gaussian(x, center, fwhm):
    sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))
    return np.exp(-0.5 * ((x - center) / sigma) ** 2)

# 3. Set spectral width and wavelength separation
fwhm = 1.0
separations = [0.5, 1.0, 2.0]

# 4. Calculate spectral intensity
for delta in separations:
    peak1 = gaussian(wavelength, 500 - delta / 2, fwhm)
    peak2 = gaussian(wavelength, 500 + delta / 2, fwhm)

    intensity = peak1 + peak2

    plt.plot(
        wavelength,
        intensity,
        label=f"Delta wavelength = {delta} nm"
    )

# 5. Display simulation results
plt.xlabel("Wavelength (nm)")
plt.ylabel("Relative Intensity")
plt.title("Spectral Peak Separation Simulation")
plt.legend()
plt.grid(True)
plt.show()
