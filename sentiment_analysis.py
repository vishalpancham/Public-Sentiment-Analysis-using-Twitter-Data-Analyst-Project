import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the tweets CSV
df = pd.read_csv("tweets.csv")

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define function to label sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["text"].apply(get_sentiment)

# Save to a new CSV file
df.to_csv("tweets_with_sentiment.csv", index=False)

# Print preview
print("✅ Sentiment analysis done! Preview:")
print(df.head(10))
