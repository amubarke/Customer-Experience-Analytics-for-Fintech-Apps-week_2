from src.google_scraper import GooglePlayReviewScraper
from src.clean_reviews import ReviewCleaner
from src.sentiment import SentimentAnalyzer
from config.config import DATA_PATHS


class ReviewPipeline:
    """
    Full end-to-end pipeline:
    1. Scrape Google Play reviews
    2. Clean + preprocess reviews
    3. Run sentiment analysis
    """

    def __init__(self):
        self.scraper = GooglePlayReviewScraper()
        self.cleaner = ReviewCleaner()
        self.sentiment = SentimentAnalyzer()

    def run(self):
        print("📌 Step 1: Scraping Google Play reviews...")
        self.scraper.scrape_all_banks(DATA_PATHS['scraped_reviews'])

        print("📌 Step 2: Cleaning reviews...")
        self.cleaner.clean_and_save(
            input_path=DATA_PATHS['scraped_reviews'],
            output_path=DATA_PATHS['cleaned_reviews']
        )

        print("📌 Step 3: Running sentiment analysis...")
        self.sentiment.add_sentiment(
            input_path=DATA_PATHS['cleaned_reviews'],
            output_path=DATA_PATHS['sentiment_results']
        )

        print("🎉 Pipeline completed successfully!")


def main():
    pipeline = ReviewPipeline()
    pipeline.run()


if __name__ == "__main__":
    main()
