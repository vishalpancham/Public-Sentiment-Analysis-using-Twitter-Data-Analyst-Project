import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("tweets_with_sentiment.csv")

# Title
st.title("📊 Real-Time Twitter Sentiment Dashboard")
st.markdown("Analyze public sentiment on trending topics using tweets.")

# Show raw data
with st.expander("🔍 Show Raw Tweets"):
    st.write(df[['text', 'Sentiment']])

# Pie chart of sentiment distribution
st.subheader("🧁 Sentiment Distribution")
sentiment_counts = df["Sentiment"].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", startangle=90)
ax1.axis("equal")
st.pyplot(fig1)

# Bar chart
st.subheader("📊 Sentiment Count")
st.bar_chart(sentiment_counts)

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
