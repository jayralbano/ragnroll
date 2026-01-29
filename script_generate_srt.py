#!/usr/bin/env python3
import time
from faster_whisper import WhisperModel
import sys
import os
import subprocess


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

# ffmpeg -i input_video.mp4 -q:a 0 -map a output_audio.mp3
output_audio_filename = f"{source_filename}.mp3"
output_audio_path = os.path.join(source_dir, output_audio_filename)

# Skip conversion if MP3 already exists
if os.path.exists(output_audio_path):
    print(f"\n\nMP3 already exists: {output_audio_filename}, skipping conversion\n\n")
else:
    print(f"\n\nConverting {source} to {output_audio_filename}\n\n")
    subprocess.run(["ffmpeg", "-i", source, "-q:a", "0", "-map", "a", output_audio_path])

print(f"\n\nTranscribing {output_audio_filename} and generating SRT subtitles\n\n")

output_filename = f"{source_filename}_subtitles.srt"
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

# Write SRT file
with open(output_path, "w", encoding="utf-8") as f:
    for i, segment in enumerate(segments, start=1):
        # SRT format:
        # 1
        # 00:00:00,000 --> 00:00:02,500
        # Subtitle text
        # [blank line]
        f.write(f"{i}\n")
        f.write(f"{format_timestamp(segment.start)} --> {format_timestamp(segment.end)}\n")
        f.write(f"{segment.text.strip()}\n")
        f.write("\n")

end_time = time.time()

print(f"\n\nDone. SRT file saved to: {output_filename}")
print(f"Time taken: {end_time - start_time:.2f} seconds\n\n")
