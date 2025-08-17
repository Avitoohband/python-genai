import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import torch
import gradio as gr

# Use a pipeline as a high-level helper
from transformers import pipeline#

text_summary = pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6",
                device=0 if torch.cuda.is_available() else -1,
                torch_dtype=torch.bfloat16)

def extract_video_id(url: str) -> str:
    # Handle all common YouTube URL formats
    regex_patterns = [
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([^\s&]+)',
        r'(?:https?://)?(?:www\.)?youtu\.be/([^\s?&]+)',
        r'(?:https?://)?(?:www\.)?youtu\.be/([^\si?&]+)',
        r'(?:https?://)?(?:www\.)?youtube\.com/embed/([^\s?&]+)',
    ]
    for pattern in regex_patterns:
        match = re.match(pattern, url)
        if match:
            return match.group(1)
    raise ValueError("Invalid YouTube URL format")


def fetch_transcript(input_url) :
    try:
        video_id = extract_video_id(input_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = "\n".join([entry["text"] for entry in transcript])
        return full_text ,summarize(full_text)
    except TranscriptsDisabled:
        return "❌ Transcript is disabled for this video."
    except NoTranscriptFound:
        return "❌ No transcript found for this video."
    except Exception as e:
        return f"❌ Error fetching transcript: {str(e)}"

def split_text(text, max_tokens=900):
    # Very basic splitter by sentence
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_tokens:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks



def summarize(text: str) -> str:
    chunks = split_text(text)
    summaries = []

    for i, chunk in enumerate(chunks):
        try:
            result = text_summary(chunk)
            summaries.append(result[0]["summary_text"])
        except Exception as e:
            summaries.append(f"[Error summarizing chunk {i}: {e}]")

    return "\n\n".join(summaries)

gr.close_all()

demo = gr.Interface(
    fn=fetch_transcript,
    inputs=gr.Textbox(label="YouTube URL"),
    outputs=
    [
        gr.Textbox(label="📜 Transcript"),
        gr.Textbox(label="📝 Summary"),
    ],
    title="🎥 YouTube Transcript & Summary",
    description="Paste a YouTube video URL to get its transcript and a summary."
)
demo.launch()