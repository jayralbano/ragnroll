#!/usr/bin/env python3
import time
import sys
import os
import subprocess
import mlx_whisper


def format_timestamp(seconds):
    """Convert seconds to SRT timestamp format: HH:MM:SS,mmm"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


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
output_filename = f"{base_filename}.srt"
output_path = os.path.join(source_dir, output_filename)

print(f"\nTranscribing with mlx-whisper (Metal GPU) → {output_filename}\n")

start_time = time.time()

result = mlx_whisper.transcribe(
    output_audio_path,
    language="en",
    word_timestamps=True,
    path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
)

segments = result["segments"]

with open(output_path, "w", encoding="utf-8") as f:
    for i, segment in enumerate(segments, start=1):
        f.write(f"{i}\n")
        f.write(f"{format_timestamp(segment['start'])} --> {format_timestamp(segment['end'])}\n")
        f.write(f"{segment['text'].strip()}\n")
        f.write("\n")

end_time = time.time()

print(f"\nDone. SRT saved to: {output_path}")
print(f"Segments: {len(segments)}")
print(f"Time taken: {end_time - start_time:.2f} seconds\n")
