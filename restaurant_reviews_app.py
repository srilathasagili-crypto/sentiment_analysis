import streamlit as st
import pickle

# Load TF-IDF vectorizer
with open("tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

# Load trained Naive Bayes model
# Change the filename below if your model file has a different name
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# App title
st.set_page_config(page_title="Restaurant Reviews Sentiment Analysis")
st.title("🍽️ Restaurant Reviews Sentiment Analysis")

st.write("Enter a restaurant review to predict whether it is Positive or Negative.")

# User input
review = st.text_area("Enter your review here")

# Prediction
if st.button("Predict Sentiment"):
    if review.strip():
        review_tfidf = tfidf.transform([review])
        prediction = model.predict(review_tfidf)

        if prediction[0] == 1:
            st.success("😊 Positive Review")
        else:
            st.error("☹️ Negative Review")
    else:
        st.warning("Please enter a review.")
