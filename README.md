<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>News Topic Classifier Using BERT</title>
</head>
<body>

<h1>Task 1: News Topic Classifier Using BERT</h1>

<h2>Objective</h2>
<p>
The objective of this task is to fine-tune a transformer-based language model (BERT)
to automatically classify news headlines into predefined topic categories.
The project demonstrates the complete workflow of tokenization, model fine-tuning,
evaluation, and deployment using modern NLP tools.
</p>

<hr>

<h2>Dataset</h2>
<p>
<strong>AG News Dataset</strong>
</p>
<ul>
    <li>Source: Hugging Face Datasets</li>
    <li>Description: A collection of news headlines categorized into four classes</li>
    <li>Total Classes:
        <ul>
            <li>World</li>
            <li>Sports</li>
            <li>Business</li>
            <li>Sci/Tech</li>
        </ul>
    </li>
</ul>

<hr>

<h2>Problem Type</h2>
<p><strong>Multi-class Text Classification</strong></p>

<hr>

<h2>Approach &amp; Methodology</h2>

<h3>1. Data Loading</h3>
<p>
The AG News dataset was loaded using the Hugging Face <code>datasets</code> library,
providing standardized access to training and testing splits.
</p>

<h3>2. Tokenization &amp; Preprocessing</h3>
<ul>
    <li>Text data tokenized using <code>bert-base-uncased</code> tokenizer</li>
    <li>Padding and truncation applied to maintain fixed input length</li>
    <li>Data formatted for PyTorch training</li>
</ul>

<h3>3. Model Fine-Tuning</h3>
<ul>
    <li>Pretrained <code>bert-base-uncased</code> model used</li>
    <li>Model fine-tuned on AG News training data</li>
    <li>Transfer learning applied to adapt BERT for news classification</li>
</ul>

<h3>4. Model Evaluation</h3>
<p>
The fine-tuned model was evaluated on the test dataset using the following metrics:
</p>
<ul>
    <li>Accuracy</li>
    <li>Weighted F1-score</li>
</ul>

<h3>5. Model Saving</h3>
<p>
The trained model and tokenizer were saved locally to enable reuse during deployment
without retraining.
</p>

<h3>6. Deployment</h3>
<p>
The model was deployed using <strong>Gradio</strong> to provide an interactive web-based
interface where users can input news headlines and receive predicted topic labels
in real time. Deployment logic is implemented in <code>app.py</code>.
</p>

<hr>

<h2>Model Used</h2>
<ul>
    <li>BERT (bert-base-uncased)</li>
</ul>

<hr>

<h2>Evaluation Metrics</h2>
<ul>
    <li>Accuracy</li>
    <li>F1-score (Weighted)</li>
</ul>

<hr>

<h2>Tools &amp; Libraries</h2>
<ul>
    <li>Python</li>
    <li>Hugging Face Transformers</li>
    <li>Hugging Face Datasets</li>
    <li>Evaluate</li>
    <li>PyTorch</li>
    <li>Gradio</li>
</ul>

<hr>

<h2>Example Usage</h2>
<pre><code>
Input: "Apple releases new AI-powered smartphone"
Output: Business
</code></pre>

<hr>

<h2>Project Structure</h2>
<pre><code>
News-Topic-Classifier-Using-BERT/
│
├── app.py
├── news_bert_model/
│   ├── config.json
│   ├── pytorch_model.bin
│   └── tokenizer files
│
├── News_Topic_Classifier_Using_BERT.ipynb
├── README.md
└── requirements.txt
</code></pre>

<hr>

<h2>Skills Gained</h2>
<ul>
    <li>Natural Language Processing using Transformers</li>
    <li>Transfer learning and model fine-tuning</li>
    <li>Text classification evaluation using accuracy and F1-score</li>
    <li>Model deployment using Gradio</li>
    <li>Practical ML engineering workflow</li>
</ul>

<hr>

<h2>Notes</h2>
<p>
Due to file size constraints, the fine-tuned BERT model may be stored using Git LFS
or hosted externally. The application dynamically loads the saved model during deployment.
</p>

<hr>

<h2>Shamrose Khan</h2>
<p>
Internship Project – AI / Machine Learning
</p>

</body>
</html>

