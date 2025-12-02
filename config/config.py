"""
Configuration file for Bank Reviews Analysis Project
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bank Names (Ordered)
BANK_NAMES = [
    'Commercial Bank of Ethiopia',
    'Bank of Abyssinia',
    'Dashen Bank'
]

# Matching App IDs (Same Order!)
APP_IDS = [
    os.getenv('CBE_APP_ID', 'com.combanketh.mobilebanking'),
    os.getenv('ABYSSINIA_APP_ID', 'com.boa.boaMobileBanking'),
    os.getenv('DASHEN_APP_ID', 'com.dashen.dashensuperapp')
]

# Scraping Configuration
SCRAPING_CONFIG = {
    'reviews_per_bank': int(os.getenv('REVIEWS_PER_BANK', 400)),
    'max_retries': int(os.getenv('MAX_RETRIES', 3)),
    'lang': 'en',
    'country': 'et'
}

# File Paths
DATA_PATHS = {
    'scraped_reviews': 'data/raw',
    'cleaned_reviews': 'data/processed/cleaned.csv',
    'sentiment_results': 'data/processed/sentiment.csv'
}
