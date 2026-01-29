#!/usr/bin/env python3
import time
from faster_whisper import WhisperModel
import sys
import os
import subprocess

source = sys.argv[1]
source_dir = os.path.dirname(source)
source_filename = os.path.basename(source)

# ffmpeg -i input_video.mp4 -q:a 0 -map a output_audio.mp3
output_audio_filename = f"{source_filename}.mp3"
output_audio_path = os.path.join(source_dir, output_audio_filename)

# Skip conversion if MP3 already exists
if os.path.exists(output_audio_path):
    print(f"\n\nMP3 already exists: {output_audio_filename}, skipping conversion\n\n")
else:
    print(f"\n\nConverting {source} to {output_audio_filename}\n\n")
    subprocess.run(["ffmpeg", "-i", source, "-q:a", "0", "-map", "a", output_audio_path])

print(f"\n\nTranscribing {output_audio_filename}\n\n")

output_filename = f"{source_filename}_transcribed.txt"
output_path = os.path.join(source_dir, output_filename)

start_time = time.time()

# Load Whisper model with faster-whisper
# Use "small" model, runs on CPU by default but should also work on MPS/GPU
model = WhisperModel("small", device="cpu", compute_type="int8")

# Transcribe the audio
segments, info = model.transcribe(
    output_audio_path,
    language="en",
    task="transcribe",
    beam_size=5
)

print(f"Detected language '{info.language}' with probability {info.language_probability}")

# Collect all segments into a single text
transcription_text = " ".join([segment.text for segment in segments])

end_time = time.time()

# write to file
with open(output_path, "w") as f:
    f.write(transcription_text)

print(f"\n\nDone. Time taken: {end_time - start_time} seconds\n\n")
