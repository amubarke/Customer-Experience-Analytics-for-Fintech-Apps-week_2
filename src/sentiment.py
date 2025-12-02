import pandas as pd
from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    return 'neutral'

def add_sentiment(input_path, output_path):
    df = pd.read_csv(input_path)

    df['sentiment'] = df['cleaned_text'].apply(get_sentiment)

    df.to_csv(output_path, index=False)
    print(f"Sentiment results saved → {output_path}")
