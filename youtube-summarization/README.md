# 🎥 YouTube Transcript & Summarization

## Overview
This project allows you to paste a YouTube URL and automatically:
1. Fetch the transcript (if available).
2. Generate an abstractive summary using a pre-trained Hugging Face model (`sshleifer/distilbart-cnn-12-6`).
3. Display both transcript and summary in a simple **Gradio web app**.

---

## Prerequisites
- Python 3.9+
- CUDA (optional, for GPU acceleration)
- Git, pip, and virtual environment recommended

---

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
### Install PyTorch (CUDA 12.8):
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip install youtube-transcript-api==1.1.1

## Usage
1. After setup, run the summarization script:
   ```bash
   python youtube-summarization/youtube-summary.py
   ```

Example code to use the pipeline:
```
import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import torch
import gradio as gr

model_path = "../Modules/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"
pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", torch_dtype=torch.bfloat16)

```
## Troubleshooting
* If you get DNS resolve errors, change your DNS to 8.8.8.8 or 8.8.4.4.
* If the model does not download automatically, copy it manually:

From: `C:\Users\User\.cache\huggingface\hub`
To: `Modules/models--sshleifer--distilbart-cnn-12-6`

You can also use the model directly from Hugging Face:
https://huggingface.co/sshleifer/distilbart-cnn-12-6


To use a different model, update the `model_path` variable accordingly.

## Example

Paste any valid YouTube URL (works with):

https://www.youtube.com/watch?v=VIDEO_ID

https://youtu.be/VIDEO_ID

https://www.youtube.com/embed/VIDEO_ID

You’ll get:

📜 Transcript text

📝 AI-generated summary


## Online Demo
Try the project on Hugging Face Spaces:
https://huggingface.co/spaces/Avituchband/YoutubeVideoSummarization