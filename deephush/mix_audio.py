# import soundfile as sf
# import numpy as np
# import os

# clean_path = "data/clean_voice.wav"
# noise_path = "data/noise_only.wav"
# output_path = "data/noisy.wav"

# # Load audio
# clean_audio, sr_clean = sf.read(clean_path)
# noise_audio, sr_noise = sf.read(noise_path)

# # Make sure sample rates match
# assert sr_clean == sr_noise, "❌ Sample rates must match!"

# # Match lengths
# min_len = min(len(clean_audio), len(noise_audio))
# clean_audio = clean_audio[:min_len]
# noise_audio = noise_audio[:min_len]

# # Mix
# noisy_audio = clean_audio + 0.5 * noise_audio  # Tune weight

# # Save
# sf.write(output_path, noisy_audio, sr_clean)
# print("✅ noisy.wav created!")


import soundfile as sf
import numpy as np
import librosa

clean_path = "data/clean_voice.wav"
noise_path = "data/noise_only.wav"
output_path = "data/noisy.wav"

# Load clean voice
clean_audio, sr_clean = sf.read(clean_path)

# Load and resample noise to match clean sample rate
noise_audio, sr_noise = librosa.load(noise_path, sr=sr_clean)

# Match lengths
min_len = min(len(clean_audio), len(noise_audio))
clean_audio = clean_audio[:min_len]
noise_audio = noise_audio[:min_len]

# Mix signals
noisy_audio = clean_audio + 0.5 * noise_audio

# Save
sf.write(output_path, noisy_audio, sr_clean)
print("✅ noisy.wav created at matching sample rate.")
