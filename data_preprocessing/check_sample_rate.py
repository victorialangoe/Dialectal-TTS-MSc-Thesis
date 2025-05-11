import os
import wave

# Code to check the sample rates of all .wav files so that we can see if they are consistent or not

directory = "../training_data/wav_files"

unique_sample_rates = set()

for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        filepath = os.path.join(directory, filename)
        try:
            with wave.open(filepath, 'r') as file:
                sample_rate = file.getframerate()
                unique_sample_rates.add(sample_rate)
        except wave.Error as e:
            print(f"Could not process {filename}: {e}")

print("Unique sample rates found:")
for sr in unique_sample_rates:
    print(f"{sr} Hz")


