import tweepy

# ✅ Replace this with your actual Bearer Token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFOC2wEAAAAAqIxGVj81p4ToaasvxU%2FyMlhCp7I%3DEFqBTlponqoiKeY7uAzjxCsY27X6Zqbux55DauFzl4KC0Z17OG"

# Initialize Tweepy client
client = tweepy.Client(bearer_token=bearer_token)

# Define your search query
query = "elections 2025 -is:retweet lang:en"  # You can change the topic

# Get tweets (latest 10)
response = client.search_recent_tweets(
    query=query,
    max_results=10,
    tweet_fields=['created_at', 'text']
)

# Print tweets
print("🟢 Tweets on:", query)
for tweet in response.data:
    print(f"- {tweet.text}")
    print("-" * 80)
