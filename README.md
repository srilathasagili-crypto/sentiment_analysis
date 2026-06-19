# 🍽️ Restaurant Reviews Sentiment Analysis Using Naive Bayes

## Overview

This project performs sentiment analysis on restaurant reviews using Natural Language Processing (NLP) and the Naive Bayes algorithm. It classifies customer reviews as **Positive** or **Negative** based on the text provided.

## Features

* Text preprocessing using NLP techniques
* TF-IDF vectorization
* Sentiment classification using Multinomial Naive Bayes
* Interactive web application built with Streamlit
* Real-time sentiment prediction

## Dataset

The dataset contains restaurant reviews labeled as:

* **1** → Positive Review
* **0** → Negative Review

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle

## Project Structure

```text
Restaurant-Reviews-Sentiment-Analysis-Using-Naive-Bayes/
│
├── app.py
├── Restaurant_Reviews.ipynb
├── Restaurant_Reviews.tsv
├── tfidf.pkl
├── naive_bayes_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/deepthi417/Restaurant-Reviews-Sentiment-Analysis-Using-Naive-Bayes
```

Navigate to the project directory:

```bash
cd Restaurant-Reviews-Sentiment-Analysis-Using-Naive-Bayes
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, allowing you to enter restaurant reviews and predict their sentiment.

## 📊 Model

* Feature Extraction: **TF-IDF Vectorizer**
* Algorithm: **Multinomial Naive Bayes**

## 📝 Example Reviews

### Positive

* The food was delicious and the service was excellent.
* Amazing experience! Highly recommended.

### Negative

* The food was cold and the staff was rude.
* Worst restaurant experience ever.

## 🌐 Deployment

The application can be deployed using:

* Streamlit Community Cloud
* Render
* Heroku
* AWS
* Azure

## 📜 License

This project is intended for educational and learning purposes.

## 👩‍💻 Author

Developed as a Machine Learning and NLP project using Python and Streamlit.
