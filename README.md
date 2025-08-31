# 🦻 Web-Based Hearing Test Prototype

This is a simple, browser-based hearing screening tool that allows users to assess their hearing at different frequencies and volumes. It is intended for **educational and awareness purposes only** and is **not a medical diagnostic tool**.

## 🔍 Features

- Tests standard audiometric frequencies: **250 Hz – 8000 Hz**
- Two intensity levels: **20 dB and 40 dB (simulated)**
- Supports testing in:
  - **Speaker mode** (both ears together)
  - **Headphones mode** (tests each ear separately)
- Interactive tone playback and response recording
- Audiogram visualization using Chart.js
- Expandable result view with summary and per-tone breakdown
- Mobile and desktop-friendly layout

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/hearing-test.git
cd hearing-test
```
### 2. Open the site
You can run it locally by simply opening index.html in your browser:
```
open index.html  # Mac
start index.html # Windows
```
### Or use a simple Python web server:

```
python3 -m http.server
```
Then visit: http://localhost:8000

### 🎧 Audio Files
All tone files (.wav) are pre-generated and located in the /audio directory. These include:

Frequencies: 250, 500, 1000, 2000, 4000, 8000 Hz

Volumes: 20 dB and 40 dB (simulated amplitudes)

### Modes:

both: stereo (same tone to both ears)

left: tone in left ear only

right: tone in right ear only

Example filenames:

1000Hz_20dB.wav
4000Hz_40dB_left.wav
8000Hz_20dB_right.wav

### 📊 Interpreting Results
After completing the test, the site provides:

A textual summary based on your hearing responses

An audiogram chart showing hearing thresholds per frequency

A detailed table showing each tone and your response

### ⚠️ Disclaimer: This is a prototype and not a substitute for professional audiometry. Results may vary based on your headphones, device volume, and environment.

### 🛠️ Built With
HTML, CSS, JavaScript

Chart.js – for audiogram visualization

### 📦 Future Improvements
Add masking noise for non-test ear (for headphones)

Support more dB levels (10, 30, 50...)

Calibration step before test

Save results or export as PDF

Mobile optimization
