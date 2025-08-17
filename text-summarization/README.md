# Text Summarization Project

## Prerequisites

- Ensure you have CUDA installed for GPU support.
- If you do **not** have CUDA, update `requirements.txt`:
  - Replace `ctransformers[cuda]>=0.2.24` with `ctransformers[cpu]>=0.2.24`.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
### Install PyTorch (CUDA 12.8):
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

## Usage
1. After setup, run the summarization script:
   ```bash
   python text-summarization/texts-summary.py
   ```

Example code to use the pipeline:
```
import torch
import gradio as gr
from transformers import pipeline

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


## Online Demo
Try the project on Hugging Face Spaces:
https://huggingface.co/spaces/Avituchband/TextSummarization