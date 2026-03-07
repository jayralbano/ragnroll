# Transcribe

Transcribe a video file using MLX Whisper (Metal GPU).

## Instructions

1. **Resolve the file path** — If the argument is not an absolute path, look for the file in `~/Desktop/` first. Construct the full path as `~/Desktop/"<filename>"`.

2. **Run the transcription script** — Execute `uv run script_transcribe_mlx.py <file>` on the resolved file path. Run in background since it takes time.

3. **When complete** — Report the output file path and time taken.

## Usage

`/transcribe 2026-03-03 22-32-11.mp4`

ARGUMENTS: $ARGUMENTS
