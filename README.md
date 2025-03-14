📌 Project Description: AI Chatbot using Streamlit & NLP
🔹 Overview
This project develops a web-based AI chatbot using Natural Language Processing (NLP) techniques. It leverages TF-IDF Vectorization and Cosine Similarity to process user queries and find the most relevant response. The chatbot is integrated with Streamlit, providing an interactive web interface for seamless user interaction.

🔹 Objectives
✔ Develop a chatbot that can answer AI, Python, and general knowledge queries
✔ Implement TF-IDF & Cosine Similarity for intelligent response selection
✔ Create a user-friendly web interface using Streamlit
✔ Ensure chatbot remembers chat history using session state

🔹 Problem Statement
Traditional chatbots require large datasets and deep learning models for training
Rule-based chatbots lack flexibility and fail to understand variations in user queries
Need a lightweight, efficient chatbot that does not require external APIs and can provide accurate responses
🔹 Solution
Uses predefined Q&A from intents.json to generate responses
Preprocesses text (lowercasing, punctuation removal) for better NLP processing
Converts text into numerical form using TF-IDF Vectorization
Matches the best response using Cosine Similarity
Provides an interactive web UI using Streamlit
🔹 Methodology
1️⃣ Data Loading – Load intents.json with predefined user queries and responses
2️⃣ Text Preprocessing – Convert text to lowercase and remove punctuation
3️⃣ Feature Extraction – Convert text into numerical form using TF-IDF
4️⃣ Similarity Matching – Use Cosine Similarity to compare user queries with stored data
5️⃣ Web UI Integration – Display chatbot conversation using Streamlit

🔹 Tools & Technologies Used
🔹 Python – Main programming language
🔹 NLTK – Text processing and tokenization
🔹 Scikit-learn – TF-IDF vectorization & similarity computation
🔹 Streamlit – Web UI for chatbot interaction
🔹 JSON – Storing chatbot responses

🔹 Features
✔ Web-based chatbot UI using Streamlit
✔ Remembers chat history using session state
✔ Accurate response selection using TF-IDF & Cosine Similarity
✔ Handles small talk, AI, and Python-related queries

🔹 Expected Outcome
✅ A fully functional AI-powered chatbot accessible via web browser
✅ Can accurately process and respond to various user queries
✅ Provides an intuitive and interactive chat experience

🔹 Future Enhancements
🚀 Integrate Speech-to-Text for voice-based chatbot interaction
🚀 Expand knowledge base with more AI-related topics
🚀 Deploy chatbot on a cloud server for public access
