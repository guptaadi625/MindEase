import json
import random
import numpy as np
from sklearn.model_selection import train_test_split
import nltk
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Load dataset
with open('mental_health_chatbot_dataset.json', 'r') as file:
    dataset = json.load(file)

# Extract questions and answers
questions = [entry['QuestionText'] for entry in dataset]
answers = [entry['AnswerText'] for entry in dataset]

# Tokenization
def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Lowercasing and tokenizing
    return ' '.join(tokens)

# Apply preprocessing to questions and answers
processed_questions = [preprocess_text(question) for question in questions]
processed_answers = [preprocess_text(answer) for answer in answers]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(processed_questions, processed_answers, test_size=0.2)