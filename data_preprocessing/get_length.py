import os
import matplotlib.pyplot as plt
from pydub import AudioSegment

# to find the average duration of the sound clips after resampling AND cleaning
base_path = "../training_data/combined_training_data_vestland/resampled_sound_clips"

durations = []

def format_duration(milliseconds):
    seconds = int(milliseconds / 1000)
    minutes = seconds // 60
    hours = minutes // 60
    return f"{hours:02}:{minutes % 60:02}:{seconds % 60:02}"

for filename in os.listdir(base_path):
    if filename.endswith(".wav"):
        file_path = os.path.join(base_path, filename)
        audio = AudioSegment.from_wav(file_path)
        durations.append(len(audio))  

total_duration = sum(durations)
average_duration = sum(durations) / len(durations) if durations else 0

print(f"Total duration: {format_duration(total_duration)}")
print(f"Average duration: {format_duration(average_duration)}")

durations_sec = [d / 1000 for d in durations]

plt.figure(figsize=(10, 5))
plt.hist(durations_sec, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel("Clip Length (seconds)")
plt.ylabel("Frequency")
plt.title("Distribution of Vestland Sound Clip Lengths")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the figure as a DF
plt.savefig("wav_duration_distribution_vestland.pdf", format='pdf')