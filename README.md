## Sentiment Analysis using Transformer Pipeline
## Project Overview

This project is a web-based Sentiment Analysis application built using Python and Streamlit. It uses a pre-trained Transformer model from Hugging Face to analyze the sentiment of user-provided text and classify it as Positive or Negative.

The application also displays the confidence score of the prediction.

## Features
- Analyze the sentiment of any text
- Classify text as Positive or Negative
- Display prediction confidence score
- Simple and user-friendly Streamlit interface
- Uses a pre-trained Transformer model
- Uses Hugging Face Inference API
- No local model training required
- Real-time sentiment prediction
- Technologies Used
- Python
- Streamlit
- Hugging Face Hub
- Transformer Model
- Hugging Face Inference API
- Model Used

## The project uses:
### Model
  "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

This is a pre-trained DistilBERT model fine-tuned for sentiment classification.

## How It Works
- The user enters a sentence or paragraph in the text area.
- The application sends the text to the Hugging Face Inference API.
- The Transformer model analyzes the text.
- The model predicts whether the sentiment is Positive or Negative.
- The application displays the sentiment along with its confidence score.

## Example:

- Input
  - I really enjoyed the movie.
   
- Output
  - Positive — 99.99%

## Another example:

- Input
  - Nobody likes me.

- Output:
  - Negative — 99.95%

## DEMO
## Screenshot

<img width="1920" height="1080" alt="Screenshot (125)" src="https://github.com/user-attachments/assets/43ad7ade-ed96-42e1-b663-bd43be383a80" />


<img width="1920" height="1080" alt="Screenshot (126)" src="https://github.com/user-attachments/assets/143cbc4f-a162-4862-8673-bd2ec54bc466" />

## Future Enhancements
- Support for multiple languages
- Emotion detection
- Sentiment history
- Batch text analysis
- Graphical sentiment statistics
- Support for longer text documents
