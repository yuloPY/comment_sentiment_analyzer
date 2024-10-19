# comment_sentiment_analyzer
 ## Table of Contents
 - [Introduction](#intruduction)
 - [Selenium Web Driver](#selenium)
 - [NLTK VADER](#vader)
 - [Usage](#usage)

 # Introduction
 This project was developed using **Selenium Web Driver** and **NLTK VADER** to perform **sentiment analysis of the comments** of a target youtube video.

 # Selenium
 In this project, **Selenium WebDriver** is used for **web scraping**. In cases where traditional HTTP-based web scraping methods (e.g. BeautifulSoup) are not sufficient, **Selenium provides the ability to view and capture dynamic and JavaScript-loaded content through the browser.**

 In this project, Selenium was chosen because YouTube comments load dynamically as you scroll down the page. Since traditional scraping methods are inadequate to deal with such dynamic content, **Selenium mimics a real user interaction on the browser** to ensure complete retrieval of comments.

 # VADER
 **VADER (Valence Aware Dictionary and sEntiment Reasoner)** is a rule-based sentiment analysis model for **sentiment analysis in social media** and other short texts. It is part of the NLTK (Natural Language Toolkit) library and is optimized to effectively evaluate positive, negative and neutral sentiment in text, especially from social media platforms.

  ## VADER's Features
  - **Valence (Sentiment Value) Based:** Evaluates the positive or negative emotional content (valence) of words with a scoring system.

  - **Rule-Based Approach:** It takes into account various factors such as capitalization, exclamation marks, grammar rules used in context when determining the emotional value of words.

  - **Social Media Compatible:** Recognize and evaluate elements typical for social media, such as acronyms, emojis, exclamation marks and other elements of social media language.

  - **Fast and Efficient:** It works faster compared to deep learning models and does not require any training. It is based on a ready-made dictionary of words, which makes it easy to use and effective.

**VADER** assigns a positive, negative or neutral score to each sentence of text and uses these scores to produce an overall sentiment score. It is widely used in projects that want to analyze sentiment in short and informal texts such as social media and customer reviews.


# Usage
The aim of my project is to **scrape comments** from Youtube and make an **sentiment analysis** of the comments of the target youtube video.

I will explain here how do you use it in your computer.

- You must have **[Firefox browser](https://www.mozilla.org/tr/firefox/new/)** and **[geckodriver.exe](https://github.com/mozilla/geckodriver/releases)** installed on your computer.

- `pip install -r requirements.txt`

- Add the target youtube video to the url variable in the **[scraper.py](sentiment_analyzer/scraper.py)** file and scrape it.

- Run your **[sentiment_analyzer.ipynb](sentiment_analyzer/sentiment_analyzer.ipynb)** using the resulting `comments.csv` file and enjoy the pie chart.