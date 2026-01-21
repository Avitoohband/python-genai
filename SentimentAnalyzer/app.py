import torch
import gradio as gr
from transformers import pipeline
import pandas as pd
import matplotlib.pyplot as plt

analyzer = pipeline("text-classification",
                model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(file):
    sentiment = analyzer(file)
    return sentiment[0]["label"]

def plot_sentiment_pie_chart(df):
    if "Sentiment" not in df.columns:
        raise ValueError("DataFrame must contain a 'Sentiment' column.")

    sentiment_counts = df["Sentiment"].value_counts()
    labels = sentiment_counts.index
    sizes = sentiment_counts.values
    colors = plt.cm.Set3.colors
    plt.figure(figsize=(6, 6))
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors[:len(labels)],
        wedgeprops=dict(edgecolor='white')
    )
    plt.title("Sentiment Distribution")
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    plt.tight_layout()
    return plt

def add_sentiment_to_reviews(file):
    df = pd.read_excel(file)

    # Check if 'Reviews' column exists
    if 'Reviews' not in df.columns:
        raise ValueError("Excel file must contain a 'Reviews' column.")

    # Apply sentiment analysis
    df['Sentiment'] = df['Reviews'].apply(analyze_sentiment)
    plot = plot_sentiment_pie_chart(df)
    return df, plot


gr.close_all()

demo = gr.Interface(
    fn=add_sentiment_to_reviews,
    inputs=gr.File(label="Input file", file_types=[".xlsx"]),
    outputs=[gr.Dataframe(label="Sentiment Analysis Result"), gr.Plot(label="Sentiment Analysis Pie Chart")],
    title="Sentiment Analyzer",
    description="Upload file to analyze its sentiment using a pre-trained model."
)
demo.launch()
