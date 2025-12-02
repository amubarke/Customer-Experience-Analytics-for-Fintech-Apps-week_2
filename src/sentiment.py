import pandas as pd
from textblob import TextBlob
from config.config import DATA_PATHS
import os

class SentimentAnalyzer:
    """
    Performs sentiment analysis on cleaned review dataset.
    """
    def __init__(self):
        self.df = None

    @staticmethod
    def analyze_sentiment(text):
        """
        Compute polarity:
        - Positive (>0)
        - Negative (<0)
        - Neutral (=0)
        """
        if not isinstance(text, str) or text.strip() == "":
            return {"polarity": 0.0, "sentiment": "neutral"}
        
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        
        if polarity > 0:
            sentiment = "positive"
        elif polarity < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        return {"polarity": polarity, "sentiment": sentiment}

    def add_sentiment(self, input_path=DATA_PATHS['cleaned_reviews'], output_path=DATA_PATHS['sentiment_results']):
        """
        Load cleaned reviews, compute sentiment, and save results.
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        self.df = pd.read_csv(input_path)
        self.df = self.df.fillna({"cleaned_text": ""})  # ensure no empty text
        
        # Apply sentiment analysis
        sentiment_results = self.df['cleaned_text'].apply(self.analyze_sentiment)
        self.df['polarity'] = sentiment_results.apply(lambda x: x['polarity'])
        self.df['sentiment'] = sentiment_results.apply(lambda x: x['sentiment'])
        
        # Save to CSV
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_csv(output_path, index=False)
        print(f"Sentiment analysis completed. Saved to {output_path}")
        return self.df

    def aggregate_by_bank(self):
        """
        Aggregate sentiment counts and mean polarity per bank.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Run add_sentiment first.")
        
        agg = self.df.groupby('bank').agg(
            total_reviews=('sentiment', 'count'),
            positive_reviews=('sentiment', lambda x: (x=='positive').sum()),
            negative_reviews=('sentiment', lambda x: (x=='negative').sum()),
            neutral_reviews=('sentiment', lambda x: (x=='neutral').sum()),
            mean_polarity=('polarity', 'mean')
        ).reset_index()
        
        return agg

# Example usage
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    df_sentiment = analyzer.add_sentiment()
    print(analyzer.aggregate_by_bank())
