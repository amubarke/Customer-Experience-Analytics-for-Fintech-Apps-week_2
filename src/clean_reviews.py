import pandas as pd
import re

class ReviewCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def drop_duplicates(self):
        """Remove duplicate rows."""
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        after = len(self.df)
        print(f"Removed {before - after} duplicate rows.")
        return self

    def handle_missing(self):
        """Drop rows where the review text or rating is missing."""
        before = len(self.df)
        self.df = self.df.dropna(subset=["review", "rating"])
        after = len(self.df)
        print(f"Removed {before - after} rows with missing data.")
        return self

    def normalize_dates(self):
        """Normalize date column to YYYY-MM-DD."""
        if "date" in self.df.columns:
            self.df["date"] = pd.to_datetime(self.df["date"], errors="coerce").dt.date
        else:
            print("⚠️ Warning: No 'date' column found.")
        return self

    def get_clean_data(self):
        """Return cleaned DataFrame."""
        return self.df
