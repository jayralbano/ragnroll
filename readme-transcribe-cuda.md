# Transcribe with CUDA

GPU-accelerated video/audio transcription using faster-whisper on NVIDIA CUDA.

## Usage

### 1. Create and activate the virtual environment

```bash
uv venv --python 3.12
source .venv/bin/activate
echo $VIRTUAL_ENV
```

### 2. Install and sync dependencies

```bash
uv sync
uv run python --version
```

### 3. Ensure ffmpeg is available

```bash
ffmpeg -version
```

### 4. Run the script

```bash
python script_transcribe_cuda.py /path/to/video_or_audio.mp4
```

### 5. Find the output

```
/path/to/video_or_audio.mp4_transcribed.txt
```
