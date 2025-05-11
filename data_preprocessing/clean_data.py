import csv
import re
import os

input_csv_path = "/home/victoria/training_data/combined_training_data_vestland/combined_training_data_vestland.csv"
output_csv_path = "/home/victoria/training_data/combined_training_data_vestland/combined_training_data_cleaned_vestland.csv"
new_audio_directory = "/home/victoria/training_data/combined_training_data_vestland/resampled_sound_clips"
# change filepath names to trondelag to clean that data


# made since LIA had some different symbols added  to the transcriptions, compared to NDC
def clean_text(text):
    text = re.sub(r'[^A-Za-zÆØÅæøå\s]', '', text) # remove non-alphabetic characters but keep the Norwegian letters
    text = re.sub(r'\s+', ' ', text).strip()
    return text


with open(input_csv_path, mode='r', encoding='utf-8') as input_file, \
     open(output_csv_path, mode='w', newline='', encoding='utf-8') as output_file:
    
    reader = csv.DictReader(input_file, delimiter='|')
    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames, delimiter='|')
    
    writer.writeheader()
    
    for row in reader:
        old_audio_path = row['audio_path']
        new_audio_path = os.path.join(new_audio_directory, os.path.basename(old_audio_path))
        row['audio_path'] = new_audio_path

        row['transcription'] = clean_text(row['transcription'])
        
        writer.writerow(row)

print("csv file cleaned and saved to", output_csv_path)
