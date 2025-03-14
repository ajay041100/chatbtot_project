import json
import random
import nltk
import string
import numpy as np
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# Load intents.json
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

# Extract patterns and responses
corpus = []
responses = []
tags = []

for intent in intents:
    tag = intent["tag"]
    for pattern in intent["patterns"]:
        corpus.append(pattern)
        responses.append(random.choice(intent["responses"]))  # Random response selection
        tags.append(tag)

# Preprocessing function
def preprocess_text(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    return text

# Vectorizing text using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([preprocess_text(q) for q in corpus])

# Chatbot response function
def chatbot_response(user_input):
    user_input = preprocess_text(user_input)
    user_tfidf = vectorizer.transform([user_input])
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix)
    similarity_score = cosine_similarities.flatten()

    response_index = similarity_score.argmax()
    if similarity_score[response_index] > 0.3:  # Threshold for response accuracy
        return responses[response_index]
    else:
        return "I'm sorry, I don't understand. Can you rephrase?"

# Streamlit UI
st.title("🤖 AI Chatbot using NLP")
st.markdown("A simple chatbot that answers basic questions using TF-IDF & Cosine Similarity.")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# User Input
user_input = st.text_input("Ask a question:", key="user_input")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = chatbot_response(user_input)
    # Append bot response
    st.session_state.messages.append({"role": "bot", "content": response})

    # Display messages
    st.chat_message("user").write(user_input)
    st.chat_message("bot").write(response)
