# Bitcoin Price Prediction Using Twitter Sentiments

## Presentation Speech

### Slide 1: Introduction

Hello everyone! Today, we'll be discussing our project on Bitcoin price prediction using Twitter sentiment analysis.
I'm Conghui, and alongside my teammate Ruby, we aim to uncover if analyzing Twitter sentiments can provide meaningful insights for predicting short-term Bitcoin price movements.

### Slide 2: Background

Let me start with some background here.

Bitcoin, as many of you know, is the leading cryptocurrency by market capitalization and has become a focal point in digital currency markets. Inspired by previous research and tools like Kaito.ai, our project explores the potential of using Twitter sentiment analysis to predict Bitcoin prices. Studies have shown that market sentiments can significantly impact price fluctuations, and social media platforms, especially Twitter, serve as rich sources of such data. This project builds on the foundation set by research into using sentiment analysis to forecast market trends, particularly for stocks and cryptocurrencies."

### Slide 3: References

We are inspired by a selection of papers and researches including the benchmark Sentiment analysis of Twitter data for predicting stock market movements

### Slide 4: Methodology

"Our methodology consists of several critical steps:

#### Data Collection and Processing

- We gathered historical Bitcoin price data from Yahoo Finance, serving as our primary financial data source， including daily open, high, low, close prices, and trading volume
- Following Xu & Cohen's approach, we collected Twitter data using keywords like 'bitcoin', 'BTC', and '$BTC'
- Implemented data cleaning procedures to remove noise, including duplicate tweets and irrelevant content
- Focused on tweets with substantial engagement and relevance to Bitcoin, as recommended by Prajapati's 2020 study

#### Sentiment Analysis Tools

We employed three sophisticated sentiment analysis tools:

- VADER (Valence Aware Dictionary and sEntiment Reasoner): Specifically optimized for social media content， providing polarity scores (positive, negative, neutral) and compound scores
- TextBlob: Providing both polarity and subjectivity analysis, helping us understand not just if sentiment is positive or negative, but how subjective the opinions are
- Flair: Utilizing deep learning-based contextual word embeddings for enhanced accuracy， this is A state-of-the-art NLP library that excels at sentiment analysis tasks, providing more nuanced sentiment detection

#### Technical Implementation

Our Python-based implementation included:

- Pandas and Numpy for data manipulation and numerical operations
- TensorFlow for machine learning model development
- Real-time data processing pipelines inspired by KryptoOracle, we implemented real-time data processing pipelines
- Feature engineering techniques from Lewinson's Python For Finance Cookbook, including:
  - Moving averages of sentiment scores
  - Price momentum indicators
  - Volume-weighted sentiment scores

#### Machine Learning Models

We experimented with two types of advanced models:

**Transformer Model:**

- Based on Xu & Cohen's work, we implemented a self-attention mechanism to capture long-range dependencies in both price and sentiment data
- Architecture includes:
  - Multi-head attention layers
  - Position-wise feed-forward networks
  - Layer normalization and residual connections

**LSTM (Long Short-Term Memory) Network:**

- Following Prajapati's approach, we designed to capture temporal dependencies in both price and sentiment data
- Capture long-term dependencies in time series data
- Processes variable-length input sequences
- Handles both numerical and sentiment features effectively

#### Evaluation

We used Root Mean Squared Error (RMSE) as our primary evaluation metric, as it effectively captures the prediction accuracy by penalizing larger errors more heavily. This method aligns with best practices in predictive financial analysis, as it emphasizes both precision and the ability to generalize."

### Slide 5: Conclusion

"Thank you for your attention! We hope this presentation has provided some insight into how Twitter sentiments can be applied in Bitcoin price prediction. We're excited about the potential applications of this approach in cryptocurrency trading and financial analysis.

We welcome any questions about our methodology or findings."
