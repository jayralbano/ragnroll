# Next Keypoint

Extract the next keypoint from a transcription file.

## Instructions

1. **First run only** — If no `_keypoints_copy.txt` exists alongside the transcription, create one as a working copy. Never modify the original `_transcribed.txt`.

2. **Find the next keypoint** — Read the `_keypoints_copy.txt`. Find the first section that has NOT yet been marked with `---`. Identify the next major keypoint (a distinct idea, insight, or argument shift).

3. **Mark it in the copy** — Insert markers in `_keypoints_copy.txt` so a human can audit the boundaries:
   - At the START of the keypoint section: `--- KEYPOINT <number> START: <short title> ---`
   - At the END of the keypoint section: `--- KEYPOINT <number> END: <short title> ---`

4. **Append to keypoints collection** — The keypoints md file is ALWAYS stored in the project keypoints directory (`/Users/jayr/Developer/ragnroll/keypoints/`), never alongside the transcription. The filename uses the format `kp-<ai-generated-short-title>-<original-filename>.md` with all spaces replaced by dashes and absolutely no spaces in the filename. If the file doesn't exist yet, create it with a `# Keypoints` heading and the source filename. Append the new keypoint as a numbered bullet with a concise 1-2 sentence summary.

5. **Show the user** — Print the keypoint you just extracted.

## File naming convention

Given a source transcription at `/path/to/2026-03-05 01-43-57 long meeting big change.mp4_transcribed.txt`:
- Working copy: `/path/to/2026-03-05 01-43-57 long meeting big change.mp4_keypoints_copy.txt` (alongside the transcription)
- Keypoints collection: `/Users/jayr/Developer/ragnroll/keypoints/kp-<short-title>-2026-03-05-01-43-57-long-meeting-big-change.mp4.md` (always in keypoints/ folder, tracked by git)
- The `<short-title>` is a brief AI-generated descriptor of the meeting's main theme (e.g., `platform-strategy`, `ai-workflow-review`)
- All dashes, absolutely no spaces in the filename

## Usage

The user will provide the transcription file path on first use. On subsequent `/next-keypoint` calls, continue from where you left off using the `\n---...\n` markers in the working copy.
