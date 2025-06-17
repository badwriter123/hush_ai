import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

def lms_denoise(noisy, noise_ref, mu=0.01, filter_len=64):
    N = len(noisy)
    w = np.zeros(filter_len)
    y = np.zeros(N)
    e = np.zeros(N)

    for n in range(filter_len, N):
        x = noise_ref[n - filter_len:n][::-1]  # reversed segment
        y[n] = np.dot(w, x)
        e[n] = noisy[n] - y[n]
        w += 2 * mu * e[n] * x

    return e  # e is the estimated clean signal

# Load audio files
noisy, sr = sf.read("data/noisy.wav")
noise_ref, _ = sf.read("data/noise_only.wav")

# Match length
min_len = min(len(noisy), len(noise_ref))
noisy = noisy[:min_len]
noise_ref = noise_ref[:min_len]

# Denoise
clean_est = lms_denoise(noisy, noise_ref)

# Save output
sf.write("data/denoised_output.wav", clean_est, sr)
print("✅ Denoised audio saved as denoised_output.wav")

# Optional: visualize
plt.figure(figsize=(10, 4))
plt.plot(noisy[:1000], label="Noisy")
plt.plot(clean_est[:1000], label="Denoised", alpha=0.75)
plt.legend()
plt.title("LMS Denoising (First 1000 samples)")
plt.show()
