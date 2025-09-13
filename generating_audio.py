import pyttsx3
from pydub import AudioSegment
import os
import random

AUDIO_FOLDER = "audio"
OUTPUT_FOLDER = os.path.join(AUDIO_FOLDER, "triplets")
GAP_MS = 300
NUM_TRIPLETS = 240

def tts_digit_audio(digit, filename):
    engine = pyttsx3.init()
    engine.save_to_file(str(digit), filename)
    engine.runAndWait()

def generate_triplet_audio(triplet, output_path):
    # Generate temporary files for each digit
    temp_files = []
    for i, digit in enumerate(triplet):
        temp_file = f"temp_{i}.wav"
        tts_digit_audio(digit, temp_file)
        temp_files.append(temp_file)
    # Load and concatenate with gaps
    gap = AudioSegment.silent(duration=GAP_MS)
    audio = AudioSegment.from_wav(temp_files[0]) + gap + \
            AudioSegment.from_wav(temp_files[1]) + gap + \
            AudioSegment.from_wav(temp_files[2])
    audio.export(output_path, format="wav")
    # Clean up temp files
    for f in temp_files:
        os.remove(f)

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    generated = set()
    while len(generated) < NUM_TRIPLETS:
        triplet = ''.join(str(random.randint(0, 9)) for _ in range(3))
        if triplet in generated:
            continue
        generated.add(triplet)
        output_path = os.path.join(OUTPUT_FOLDER, f"{triplet}.wav")
        generate_triplet_audio(triplet, output_path)
        print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
