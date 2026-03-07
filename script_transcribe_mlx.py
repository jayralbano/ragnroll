#!/usr/bin/env python3
import time
import sys
import os
import subprocess
import mlx_whisper


source = sys.argv[1]
source_dir = os.path.dirname(source)
source_filename = os.path.basename(source)
base_filename = os.path.splitext(source_filename)[0]

# Convert to MP3 first
output_audio_filename = f"{base_filename}.mp3"
output_audio_path = os.path.join(source_dir, output_audio_filename)

if os.path.exists(output_audio_path):
    print(f"\nMP3 already exists: {output_audio_filename}, skipping conversion\n")
else:
    print(f"\nConverting {source_filename} to MP3\n")
    subprocess.run(["ffmpeg", "-i", source, "-q:a", "0", "-map", "a", output_audio_path])

output_filename = f"{base_filename}_transcribed.txt"
output_path = os.path.join(source_dir, output_filename)

print(f"\nTranscribing with mlx-whisper (Metal GPU) → {output_filename}\n")

start_time = time.time()

result = mlx_whisper.transcribe(
    output_audio_path,
    language="en",
    path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
)

transcription_text = " ".join([segment["text"].strip() for segment in result["segments"]])

with open(output_path, "w", encoding="utf-8") as f:
    f.write(transcription_text)

end_time = time.time()

print(f"\nDone. Transcription saved to: {output_path}")
print(f"Time taken: {end_time - start_time:.2f} seconds\n")
