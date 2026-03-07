# Archive

Move transcription source files to the archive folder after keypoint extraction is complete.

## Instructions

1. **Identify source files** — The user provides the base filename (e.g. `2026-03-03 22-32-11`). Find all related files on `~/Desktop`:
   - `.mp4` (video)
   - `.mp3` (audio)
   - `_transcribed.txt` (transcription)
   - `_keypoints_copy.txt` (working copy)
   - `.srt` (subtitles, if exists)

2. **Ask for description** — Ask the user: "Add a description to the filename? (e.g. `scrum`, `huddle mihai`) or press Enter to skip."

3. **Move files** — Move all found files to `~/Desktop/archive/`:
   - If a description is provided, insert it after the timestamp: `2026-03-03 22-32-11 scrum.mp4`
   - If no description, move files as-is without renaming

4. **Confirm** — List the files that were moved.

## Usage

Run `/archive <base-filename>` after all keypoints are extracted.
Example: `/archive 2026-03-03 22-32-11`

ARGUMENTS: $ARGUMENTS
