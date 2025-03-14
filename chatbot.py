import json
import random
import nltk
import string
import numpy as np
import tkinter as tk
from tkinter import scrolledtext
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

# Function to send message
def send_message():
    user_message = user_input.get()
    if user_message.strip() == "":
        return

    chat_window.insert(tk.END, "You: " + user_message + "\n", "user")
    response = chatbot_response(user_message)
    chat_window.insert(tk.END, "Bot: " + response + "\n", "bot")

    user_input.delete(0, tk.END)

# Create UI Window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("400x500")

# Chat Display
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_window.pack(pady=10)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

# User Input Field
user_input = tk.Entry(root, width=40)
user_input.pack(pady=5)

# Send Button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Run the chatbot UI
root.mainloop()
