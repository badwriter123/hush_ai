import streamlit as st
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

st.title("🎧 Audio Comparison Dashboard")

# File paths
clean_path = "data/clean_voice.wav"
noisy_path = "data/noisy.wav"
denoised_path = "data/denoised_output.wav"

# Load files
def load_audio(path):
    audio, sr = sf.read(path)
    return audio, sr

# Plot waveform
def plot_waveform(audio, sr, label):
    st.subheader(f"{label} Waveform")
    fig, ax = plt.subplots()
    ax.plot(audio[:1000])
    ax.set_title(f"{label} - First 1000 Samples")
    st.pyplot(fig)

# Clean
if st.checkbox("Show Clean Voice"):
    clean, sr_clean = load_audio(clean_path)
    st.audio(clean_path, format='audio/wav')
    plot_waveform(clean, sr_clean, "Clean Voice")

# Noisy
if st.checkbox("Show Noisy Audio"):
    noisy, sr_noisy = load_audio(noisy_path)
    st.audio(noisy_path, format='audio/wav')
    plot_waveform(noisy, sr_noisy, "Noisy Audio")

# Denoised
if st.checkbox("Show Denoised Audio"):
    denoised, sr_denoised = load_audio(denoised_path)
    st.audio(denoised_path, format='audio/wav')
    plot_waveform(denoised, sr_denoised, "Denoised Output")
