# Archive

Move transcription source files to the archive folder after keypoint extraction is complete.

## Instructions

1. **Identify source files** — The user provides the base filename (e.g. `2026-03-03 22-32-11`). Find all related files on `~/Desktop`:
   - `.mp4` (video)
   - `.mp3` (audio)
   - `_transcribed.txt` (transcription)
   - `_keypoints_copy.txt` (working copy)
   - `.srt` (subtitles, if exists)

2. **Infer description** — Check the keypoints file in `keypoints/` for context. If the filename already contains a description (e.g. `2026-03-03 22-32-11 scrum.mp4`), keep it. Otherwise, infer from content: daily standup/scrum → `scrum`, huddle → `huddle`, etc. Default to `scrum` if it's a daily meeting.

3. **Move files** — Move all found files to `~/Desktop/archive/`:
   - Insert the description after the timestamp: `2026-03-03 22-32-11 scrum.mp4`
   - Do NOT ask the user for confirmation — this is fully autonomous

4. **Confirm** — List the files that were moved.

## Usage

Run `/archive <base-filename>` after all keypoints are extracted.
Example: `/archive 2026-03-03 22-32-11`

ARGUMENTS: $ARGUMENTS
