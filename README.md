# Customer-Experience-Analytics-for-Fintech-Apps-week_2## Week 2 Methodology – Customer Experience Analytics for Fintech Apps

### Objectives

- Implement Google Play review scraping for target banks: CBE, Abyssinia, and Dashen.
- Develop a review cleaning and preprocessing pipeline to normalize text and remove duplicates.
- Prepare the data for sentiment analysis in the upcoming weeks.
- Ensure a modular code structure for scraper, cleaner, and sentiment analyzer.

### Scraping Reviews

- **Tool:** `google-play-scraper` Python package.
- **Target Apps:** Mobile banking apps for CBE, Bank of Abyssinia, and Dashen Bank.
- **Parameters:** 
  - Language: English (`en`)
  - Country: Ethiopia (`et`)
  - Reviews per bank: 400 (configurable)
- **Process:** 
  1. Implemented `GooglePlayReviewScraper` class for modular scraping.
  2. Scraped reviews are stored as CSV in `data/raw/google_play_reviews.csv`.
  3. Each review is tagged with the corresponding bank name.

### Review Cleaning

- **Tool:** Custom Python class `ReviewCleaner`.
- **Steps:** 
  1. Remove empty review rows.
  2. Normalize text (lowercase, remove extra spaces, remove unwanted characters except `. , ! ?`).
  3. Remove duplicate reviews based on cleaned text.
- **Output:** Cleaned CSV saved at `data/processed/cleaned.csv`.

### Pipeline Organization

- Project structured into modules: 
  - `src/google_scraper.py` – Scraper code.
  - `src/clean_reviews.py` – Cleaning/preprocessing code.
  - `src/sentiment.py` – Sentiment analysis module (to be implemented).
  - `config/config.py` – Stores App IDs, bank names, scraping parameters, and file paths.

- `ReviewPipeline` class combines scraping, cleaning, and sentiment steps for full automation.

### Current Results

| Step | Status | Output |
|------|--------|--------|
| Scraping Google Play Reviews | ✅ Completed | `data/raw/google_play_reviews.csv` |
| Review Cleaning | ✅ Completed | `data/processed/cleaned.csv` |
| Sentiment Analysis | ⚪ Pending | `data/processed/sentiment.csv` |

### Challenges

- Import and module path issues due to Jupyter Notebook folder structure.
- Initial confusion with relative paths when accessing CSV files.
- Ensuring modular code to allow independent testing of scraper, cleaner, and sentiment modules.

### Next Steps

- Implement sentiment analysis using TextBlob or advanced models.
- Generate visualizations: sentiment distribution, top keywords, review counts over time.
- Perform exploratory data analysis (EDA) on the cleaned dataset.
- Refine pipeline automation: scraping → cleaning → sentiment → visualization.
