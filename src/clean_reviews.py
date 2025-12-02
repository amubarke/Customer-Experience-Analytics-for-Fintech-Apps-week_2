import re
import pandas as pd

class ReviewCleaner:
    """
    Handles text cleaning, duplicate removal, and date normalization
    for scraped Google Play reviews.
    """

    def __init__(self):
        pass

    @staticmethod
    def clean_text(text):
        """
        Normalize a single review:
        - Ensure valid string
        - Remove extra spaces
        - Allow only alphanumeric + . , ! ?
        - Convert to lowercase
        """
        if not isinstance(text, str):
            return ""

        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[^A-Za-z0-9 .,!?]", "", text)
        return text.strip().lower()

    @staticmethod
    def normalize_date(date_value):
        """
        Normalize dates into YYYY-MM-DD.
        GooglePlayScraper sometimes returns:
            "January 1, 2024"
            "2023-11-05T12:00:00Z"
            pandas Timestamp objects
        """

        try:
            date = pd.to_datetime(date_value, errors="coerce")
            if pd.isna(date):
                return None
            return date.strftime("%Y-%m-%d")
        except:
            return None

    def clean_dataframe(self, df):
        """
        Clean the full DataFrame:
        - Ensure 'content' column exists
        - Remove missing content
        - Clean text
        - Remove duplicates (raw + cleaned text)
        - Normalize date column if exists
        """
        if "content" not in df.columns:
            raise KeyError("DataFrame must contain a 'content' column")

        # Drop rows where content is missing
        df = df.dropna(subset=["content"])

        # Clean text column
        df["cleaned_text"] = df["content"].apply(self.clean_text)

        # Normalize date column if present
        if "at" in df.columns:
            df["review_date"] = df["at"].apply(self.normalize_date)

        # Drop duplicate cleaned texts
        df = df.drop_duplicates(subset=["cleaned_text"])

        return df

    def clean_and_save(self, input_path, output_path):
        """
        Load → clean → save
        """
        df = pd.read_csv(input_path)
        df = self.clean_dataframe(df)
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved → {output_path}")
        return df
