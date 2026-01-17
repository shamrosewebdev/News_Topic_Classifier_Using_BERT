# app.py
# News Topic Classifier Using BERT (Gradio App)

import torch
import gradio as gr
from transformers import BertTokenizer, BertForSequenceClassification

LABELS = ["World", "Sports", "Business", "Sci/Tech"]

MODEL_PATH = "./news_bert_model"

tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

def classify_news(text):
    if text.strip() == "":
        return "Please enter a news headline."

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()

    return LABELS[prediction]

interface = gr.Interface(
    fn=classify_news,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Enter news headline here..."
    ),
    outputs="text",
    title="News Topic Classifier (BERT)",
    description="Fine-tuned BERT model that classifies news headlines into World, Sports, Business, or Sci/Tech."
)

if __name__ == "__main__":
    interface.launch(share=True)
