#!/usr/bin/env python3
import time
from faster_whisper import WhisperModel, BatchedInferencePipeline
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
    # Use NVENC-accelerated ffmpeg if available, fall back to CPU
    subprocess.run(["ffmpeg", "-i", source, "-q:a", "0", "-map", "a", output_audio_path])

print(f"\n\nTranscribing {output_audio_filename}\n\n")

output_filename = f"{source_filename}_transcribed.txt"
output_path = os.path.join(source_dir, output_filename)

start_time = time.time()

# Use large-v3 model on CUDA with float16 for maximum speed and accuracy
model = WhisperModel(
    "large-v3",
    device="cuda",
    compute_type="float16",
    num_workers=4,
)

# Batched inference pipeline for maximum GPU throughput
batched_model = BatchedInferencePipeline(model=model)

# Transcribe with CUDA-optimized settings
segments, info = batched_model.transcribe(
    output_audio_path,
    language="en",
    task="transcribe",
    batch_size=24,
    vad_filter=True,
    vad_parameters=dict(
        min_silence_duration_ms=500,
        speech_pad_ms=400,
    ),
)

print(f"Detected language '{info.language}' with probability {info.language_probability}")

# Collect all segments into a single text
transcription_text = " ".join([segment.text for segment in segments])

end_time = time.time()

# write to file
with open(output_path, "w") as f:
    f.write(transcription_text)

print(f"\n\nDone. Time taken: {end_time - start_time} seconds\n\n")
