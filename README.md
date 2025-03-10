Project Title: AI-Powered Chatbot using NLP & TF-IDF Vectorization
📌 Project Overview
This project implements an AI-powered chatbot using Natural Language Processing (NLP) with TF-IDF Vectorization to process and respond to user queries. The chatbot is designed to answer questions on Artificial Intelligence (AI), Python, Machine Learning, Mathematics, General Knowledge, and Fun Facts.

🛠️ Technologies Used
Python (Main programming language)
Scikit-learn (For TF-IDF Vectorization & Cosine Similarity)
NLTK (Natural Language Toolkit) (For text preprocessing)
Cosine Similarity (To find the best-matching response)

📝 How It Works?
Predefined Knowledge Base: The chatbot stores a collection of common questions and their responses.
User Input Processing: The input text is lowercased and cleaned (punctuation removed).
TF-IDF Vectorization: Converts text data into numerical form for similarity comparison.
Cosine Similarity Calculation: Compares user input with stored questions to find the closest match.
Response Selection: If a match is found above a certain threshold, the corresponding response is returned; otherwise, it asks the user to rephrase the question.

💡 Features
✅ Handles AI, Python, and General Topics
✅ Understands Variations of User Queries
✅ Uses NLP to Find the Best-Matching Answer
✅ Can Engage in Small Talk (Greetings, Jokes, Fun Facts)
✅ Lightweight & Efficient (No External API Required)

🔮 Future Enhancements
Integrate a GUI (Tkinter or Flask-based Web App)
Use WordNet Lemmatization for Better Understanding
Train with More Data to Improve Accuracy
Implement Speech-to-Text for Voice-Based Chatbot
