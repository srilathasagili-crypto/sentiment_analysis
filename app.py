import streamlit as st
import pickle

# Load model and vectorizer
tfidf = pickle.load(open("tfidf.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

st.title("Restaurant Review Sentiment Analysis")

review = st.text_input("Enter your review")

if st.button("Predict"):
    
    review_vector = tfidf.transform([review])
    prediction = model.predict(review_vector)

    if prediction[0] == 1:
        st.success("Positive Review")
    else:
        st.error("Negative Review")