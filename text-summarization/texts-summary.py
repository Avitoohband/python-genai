import torch
import gradio as gr

# Use a pipeline as a high-level helper
from transformers import pipeline

moodel_path = "../Modules/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"
text_summary = pipe = pipeline("summarization", model=moodel_path,
                torch_dtype=torch.bfloat16)

# text_summary = pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6",
#                 torch_dtype=torch.bfloat16)


def summarize(input_text):
    output = text_summary(input_text)
    return output[0]['summary_text']

gr.close_all()

demo = gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(lines=10, label="Input Text"),
    outputs=gr.Textbox(label="Summary"),
    title="Text Summarization",
    description="Enter text to summarize it using a pre-trained model."
)
demo.launch()






