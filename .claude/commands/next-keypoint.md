# Next Keypoint

Extract the next keypoint from a transcription file.

## Instructions

1. **First run only** — If no `_keypoints_copy.txt` exists alongside the transcription, create one as a working copy. Never modify the original `_transcribed.txt`.

2. **Find the next keypoint** — Read the `_keypoints_copy.txt`. Find the first section that has NOT yet been marked with `---`. Identify the next major keypoint (a distinct idea, insight, or argument shift).

3. **Mark it in the copy** — Insert markers in `_keypoints_copy.txt` so a human can audit the boundaries:
   - At the START of the keypoint section: `--- KEYPOINT <number> START: <short title> ---`
   - At the END of the keypoint section: `--- KEYPOINT <number> END: <short title> ---`

4. **Append to keypoints collection** — The keypoints md file is ALWAYS stored in the project root directory (`/home/jayrpc/Developer/ragnroll/keypoints/`), never alongside the transcription. If no `keypoints_<source_filename>.md` exists in the project dir, create it with a `# Keypoints` heading and the source filename. Append the new keypoint as a numbered bullet with a concise 1-2 sentence summary.

5. **Show the user** — Print the keypoint you just extracted.

## File naming convention

Given a source transcription at `/path/to/video.mp4_transcribed.txt`:
- Working copy: `/path/to/video.mp4_keypoints_copy.txt` (alongside the transcription)
- Keypoints collection: `/home/jayrpc/Developer/ragnroll/keypoints/keypoints_video.mp4.md` (always in keypoints/ folder, tracked by git)

## Usage

The user will provide the transcription file path on first use. On subsequent `/next-keypoint` calls, continue from where you left off using the `---` markers in the working copy.
