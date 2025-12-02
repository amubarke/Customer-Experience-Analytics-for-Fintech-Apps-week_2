import re
import pandas as pd

class ReviewCleaner:
    """
    Handles text cleaning, duplicate removal, date normalization,
    and source tagging for scraped Google Play reviews.
    """

    def __init__(self):
        pass

    @staticmethod
    def clean_text(text):
        if not isinstance(text, str):
            return ""
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[^A-Za-z0-9 .,!?]", "", text)
        return text.strip().lower()

    @staticmethod
    def normalize_date(date_value):
        try:
            date = pd.to_datetime(date_value, errors="coerce")
            if pd.isna(date):
                return None
            return date.strftime("%Y-%m-%d")
        except:
            return None

    def clean_dataframe(self, df):
        if "content" not in df.columns:
            raise KeyError("DataFrame must contain a 'content' column")

        # Drop rows with missing content
        df = df.dropna(subset=["content"])

        # Clean text
        df["cleaned_text"] = df["content"].apply(self.clean_text)

        # Normalize date if 'at' column exists
        if "at" in df.columns:
            df["review_date"] = df["at"].apply(self.normalize_date)

        # Remove duplicates
        df = df.drop_duplicates(subset=["cleaned_text"])

        # Add source column
        df["source"] = "Google Play"

        return df

    def clean_and_save(self, input_path, output_path):
        df = pd.read_csv(input_path)
        df = self.clean_dataframe(df)
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved → {output_path}")
        return df
