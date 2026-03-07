# Transcribe

Transcribe a video file using MLX Whisper (Metal GPU).

## Instructions

1. **Resolve the file path** — If the argument is not an absolute path, look for the file in `~/Desktop/` first. Construct the full path as `~/Desktop/"<filename>"`.

2. **Run the transcription script** — Execute `uv run script_transcribe_mlx.py <file>` on the resolved file path. Run in background since it takes time.

3. **When complete** — Report the output file path and time taken.

4. **Auto-rename timestamp-only files** — If the original filename is purely a timestamp (matches pattern `YYYY-MM-DD HH-MM-SS.mp4` with no additional text after the timestamp), then:
   - Read the first ~500 lines of the transcription output
   - Determine the meeting type from context clues. Common types:
     - **scrum** — daily standup/scrum meetings (most common — look for status updates, blockers, what people worked on)
     - **huddle slack** — informal Slack huddle conversations
     - **ai innovation** — AI/innovation focused discussions
     - **sprint planning** — sprint planning sessions
     - **retro** — retrospectives
     - **1on1** — one-on-one meetings
     - Use your best judgment for other meeting types; keep names short and lowercase
   - Rename both the `.mp4` file on Desktop AND the transcription `.txt` file by appending `<space><meeting type>` before the extension. Example: `2026-02-11 22-32-16.mp4` → `2026-02-11 22-32-16 scrum.mp4`
   - Also rename the `.mp3` file if it exists
   - Report the new filenames

## Usage

`/transcribe 2026-03-03 22-32-11.mp4`

ARGUMENTS: $ARGUMENTS
