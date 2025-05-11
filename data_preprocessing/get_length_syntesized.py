import os
from pydub import AudioSegment
import matplotlib.pyplot as plt


# to find the average duration of the synthesized sentences
# and plot the distribution of the durations
# for each model and dialect
base_dir = "../synthesized_sentences"
models = ["Matcha", "Toucan"]
dialects = ["Trondelag", "Vestland"]

all_durations = {"Trondelag": [], "Vestland": []}

durations_by_model_dialect = {}

def format_duration(milliseconds):
    seconds = int(milliseconds / 1000)
    minutes = seconds // 60
    hours = minutes // 60
    return f"{hours:02}:{minutes % 60:02}:{seconds % 60:02}"

for model in models:
    for dialect in dialects:
        path = os.path.join(base_dir, model, dialect)
        durations = []

        for filename in os.listdir(path):
            if filename.endswith(".wav"):
                file_path = os.path.join(path, filename)
                audio = AudioSegment.from_wav(file_path)
                duration = len(audio)  # ms
                durations.append(duration)
                all_durations[dialect].append(duration)

        durations_by_model_dialect[(model, dialect)] = durations

        durations_sec = [d / 1000 for d in durations]
        plt.figure(figsize=(10, 5))
        plt.hist(durations_sec, bins=30, edgecolor='black', alpha=0.7)
        plt.xlabel("Clip Length (seconds)")
        plt.ylabel("Frequency")
        plt.title(f"Duration Distribution: {model} - {dialect}")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        filename = f"wav_duration_distribution_{model.lower()}_{dialect.lower()}.pdf"
        plt.savefig(filename, format='pdf')
        plt.close()

print("AVERAGE DURATION PER DIALECT (ALL MODELS): \n")
for dialect in dialects:
    durations = all_durations[dialect]
    avg_ms = sum(durations) / len(durations) if durations else 0
    print(f"{dialect}: {format_duration(avg_ms)}")

print("\n AVERAGE DURATION PER MODEL + DIALECT: \n")
for (model, dialect), durations in durations_by_model_dialect.items():
    avg_ms = sum(durations) / len(durations) if durations else 0
    print(f"{model} - {dialect}: {format_duration(avg_ms)}")
