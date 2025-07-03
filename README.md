# 🧠 Public Sentiment Analysis Dashboard (Twitter NLP Project)

This project analyzes public sentiment in real time using tweets. It fetches tweets via the Twitter API, 
applies NLP sentiment analysis using the VADER model, and displays the results in a clean, interactive dashboard using Streamlit.

---

## 📌 Project Overview

- 🔍 Tracks trending topics (like Elections, Tech, Sports) using Twitter data
- 🧠 Classifies tweets into **Positive**, **Negative**, or **Neutral**
- 📊 Visualizes results using **pie charts**, **bar charts**, and raw tweet logs
- 🌐 Fully deployed live using **Streamlit Cloud**

---

## 🛠️ Tech Stack

| Tool         | Purpose                            |
|--------------|-------------------------------------|
| Python       | Core programming language           |
| Tweepy       | Fetching tweets using Twitter API   |
| VADER        | Sentiment analysis (NLP)            |
| Pandas       | Data handling                       |
| Matplotlib   | Charts and graphs                   |
| Streamlit    | Web dashboard and UI                |

---

## 📂 Folder Structure

📁 Public-Sentiment-Analysis/
├── tweets.csv # Original tweet data
├── tweets_with_sentiment.csv # Data after sentiment labeling
├── sentiment_analysis.py # Python file for VADER NLP
├── app.py # Streamlit dashboard app
├── requirements.txt # Required packages for deployment

## 🚀 Live App Link

👉 **Deployed on Streamlit**:  
[https://vishalpancham.streamlit.app  
*(Replace this with your actual link if different)*](https://public-sentiment-analysis-using-twitter-data-analyst-project-p.streamlit.app/)


---

## ✅ How It Works

1. Collect tweets using Twitter API (Tweepy)
2. Run VADER Sentiment Analyzer to tag each tweet
3. Save results in CSV and display via Streamlit
4. Deploy to Streamlit Cloud with `requirements.txt`

---

## 🔥 Key Highlights

- Real-time tweet processing (up to 100/month with Free Twitter API)
- Fast & beginner-friendly NLP using VADER
- Clean and interactive frontend with 1-click deployment
- Portfolio-ready project for Data Analyst or NLP profile

---

## 🙌 Credits

Built with 💻 by Vishal as part of a Data Analyst Internship task  

---
## 💡 Bonus Tip

> We can also export `tweets_with_sentiment.csv` to use in Tableau or Power BI!



