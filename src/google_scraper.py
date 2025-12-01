import pandas as pd
from google_play_scraper import Sort, reviews
import os
from config.config import APP_IDS, BANK_NAMES ,SCRAPING_CONFIG ,DATA_PATHS

class GooglePlayReviewScraper:
    def __init__(self, app_ids=APP_IDS, bank_names=BANK_NAMES, project_root=None):
        self.app_ids = app_ids
        self.bank_names = bank_names
        # Set project root (defaults to current working directory if not provided)
        self.project_root = project_root or os.getcwd()

    def scrape_app(self, app_name, app_id, limit=400):
        print(f"Scraping {app_name}...")
        all_reviews = []
        count = 0

        while count < limit:
            result, _ = reviews(
                app_id,
                lang='en',
                country='et',
                sort=Sort.NEWEST,
                count=200
            )
            if not result:
                break
            all_reviews.extend(result)
            count += len(result)

        df = pd.DataFrame(all_reviews)
        df["bank"] = app_name
        return df

    def scrape_all(self, relative_save_path='data/raw'):
        # Build absolute path
        save_path = os.path.join(self.project_root, relative_save_path)
        os.makedirs(save_path, exist_ok=True)
        all_data = []

        for bank_name, app_id in zip(self.bank_names, self.app_ids):
            df = self.scrape_app(bank_name, app_id)
            all_data.append(df)

        final_df = pd.concat(all_data, ignore_index=True)
        out_file = os.path.join(save_path, "google_play_reviews.csv")
        final_df.to_csv(out_file, index=False)

        print(f"Saved scraped data to {out_file}")
        return final_df
