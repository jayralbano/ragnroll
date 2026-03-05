# Ragnroll Project Memory

## Project Overview
- Transcription utilities for meeting recordings stored on Desktop
- Uses `uv` as package manager
- Video files are stored on `~/Desktop` with naming pattern: `YYYY-MM-DD HH-MM-SS <description>.mp4`

## Transcription Scripts
- `script_generate_srt.py` — Old script, uses `faster-whisper` with `small` model on CPU. Slow (~498s for 1h52m video)
- `script_transcribe_mac.py` — Plain text transcription (no timestamps), also `faster-whisper` on CPU
- `script_generate_srt_mlx.py` — SRT subtitles via `mlx-whisper` with Metal GPU + `whisper-large-v3-turbo`. ~375s for 1h52m. WARNING: `word_timestamps=True` produces broken SRT with empty segments and hallucinations — avoid it
- `script_transcribe_mlx.py` — **Preferred for keypoints**. Plain text transcription via `mlx-whisper` + Metal GPU + `whisper-large-v3-turbo`. ~305s for 1h52m. No word_timestamps, clean output
- `script_transcribe_cuda.py` — CUDA-based transcription (for non-Mac)

## Key Conventions
- Always convert MP4 to MP3 first before transcribing (user preference)
- MP3 filename should strip the `.mp4` extension: `video.mp3` NOT `video.mp4.mp3`
- Run scripts with: `uv run script_generate_srt_mlx.py ~/Desktop/"filename.mp4"`

## Whisper Transcription Quirks
- "Austin" or "Awesome" in transcriptions = **Asim** (co-founder/CTO)
- "Andrew" = Andrew (co-founder/CEO)
- "cloud" or "clock code" = **Claude** / **Claude Code**
- "Claudia" or "Cloudy" = **Claudiu**
- "JR" or "Jared" = **Jayr** (note: "Jira" can be Jayr OR Atlassian Jira — use context to decide)
- "Cheri" = **Sherry**
- "Elkin" = **Alkin**
- "DeMarco" = **Marco**
- "OpenFlow" = **OpenClaw** (product/concept referenced by Andrew)

## Keypoints Workflow
- `/next-keypoint` skill extracts keypoints from transcriptions
- Keypoints stored in `/Users/jayr/Developer/ragnroll/keypoints/`
- Working copy: `<filename>_keypoints_copy.txt` alongside the transcription on Desktop
- Use `============================================================` separator lines around `--- KEYPOINT N START/END ---` markers for easy visual auditing
- After extracting all keypoints, audit each boundary: check gaps between END→START for orphaned text
- When doing bulk extraction, loop manually (extract → sleep 1s → repeat) — don't delegate to background agent
- Always apply whisper name corrections to BOTH the keypoints md file AND the keypoints_copy.txt

## Team Members (membership.io)
- **Andrew** — co-founder/CEO
- **Asim** — co-founder/CTO (whisper hears "Austin"/"Awesome")
- **Jayr** — developer (whisper hears "JR")
- **Claudiu** — QA (whisper hears "Claudia"/"Cloudy")
- **Marius** — developer
- **Mihai** — developer
- **Marco** — developer
- **Milan** — front-end/UI
- **Jake** — QA
- **Sherry** — QA
- **Marcus** — developer
- **Adam** — support (stepping in for Amar on daily scrums)
- **Alkin** — developer
