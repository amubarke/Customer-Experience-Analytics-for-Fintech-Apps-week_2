Week 2 — Customer Experience Analytics for Fintech Apps

Data Cleaning • Sentiment Analysis • Thematic Analysis • Visual Insights

This week focused on transforming raw Google Play Store reviews into a clean, structured, and analyzable dataset. The pipeline for preprocessing, sentiment scoring, and theme extraction was completed, along with key exploratory visualizations. The outputs from Week 2 form the core analytical foundation for subsequent modeling and insights.

🏁 1. Objectives for Week 2

Build a robust review preprocessing pipeline

Standardize and clean reviews: duplicates, missing data, tokenization, lemmatization

Execute sentiment analysis (TextBlob baseline)

Extract keywords using spaCy + TF-IDF

Group extracted keywords into 3–5 themes per bank

Produce key exploratory visualizations

Save structured results to CSV for database ingestion

Evaluate early insights for each bank (CBE, BOA, Dashen)

📂 2. Project Folder Structure


Customer-Experience-Analytics-for-Fintech-Apps-week_2/
│
├── data/
│   ├── raw/                 # Original scraped reviews
│   ├── processed/           # Cleaned CSVs + sentiment results
│
├── notebooks/
│   ├── week2_sentiment.ipynb
│   ├── week2_theme_analysis.ipynb
│
├── src/
│   ├── clean_reviews.py     # Cleaning + preprocessing pipeline
│   ├── sentiment.py         # SentimentAnalyzer class
│   ├── themes.py            # Keyword extraction + theme clustering
│   ├── utils.py
│
├── reports/
│   ├── Week2_Report.pdf     # Full PDF report (10 pages)
│
└── README.md

🧹 3. Data Cleaning Pipeline (clean_reviews.py)
The cleaning script performs:

Duplicate removal

Missing value handling

Text-level normalization

Tokenization

Lemmatization

Stop-word removal

Bank tagging

Source field addition (google_play)

Output:
data/processed/cleaned.csv
Columns include:

review_id
bank
review_text
cleaned_text
rating
review_date
source


😊 4. Sentiment Analysis (sentiment.py)

Using TextBlob, each review receives:

sentiment_label (positive, neutral, negative)

sentiment_score (float)

Output:
data/processed/cleaned_with_sentiment.csv

Sample summary:

| Bank              | Total | Positive | Negative | Neutral | Mean Polarity |
| ----------------- | ----- | -------- | -------- | ------- | ------------- |
| Bank of Abyssinia | 286   | 121      | 63       | 102     | 0.1027        |
| CBE               | 296   | 146      | 27       | 123     | 0.2296        |
| Dashen Bank       | 286   | 171      | 44       | 71      | 0.2303        |

🔍 5. Keyword & Theme Extraction
Using spaCy + TF-IDF, top keywords were extracted and grouped into themes:

| Theme                       | Count |
| --------------------------- | ----- |
| Transaction Performance     | 107   |
| Feature Requests            | 65    |
| Customer Support            | 51    |
| User Interface & Experience | 49    |
| Account Access Issues       | 47    |

📊 6. Visualizations (Week 2)

✔ Rating distribution per bank
✔ Sentiment distribution bar charts
✔ Keyword frequency stacked bar chart
✔ Per-bank stacked keyword visualization
✔ Word cloud for top keywords
✔ Theme frequency bar chart
✔ Sentiment by rating bucket
✔ Top 20 TF-IDF keywords visual
✔ Cleanliness summary statistics
✔ Sentiment polarity histogram

🧠 7.  Insights (Week 2)
🔸 Positive Highlights

Dashen and CBE show strong polarity averages

High number of positive reviews mention good UI and fast transfers

🔸 Major Pain Points

Account access (login/OTP failures)

Transaction failures (EFT & CBEBirr issues)

Poor customer support responsiveness
