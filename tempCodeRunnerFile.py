

import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import random

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Define a dictionary of responses
responses = {
    'hello': ['Hi, how are you?', 'Hello! How can I help you today?'],
    'how are you': ['I\'m doing well, thanks for asking!', 'I\'m here to help you, so I\'m doing great!'],
    'what is your purpose': ['I\'m here to provide mental health support and resources.', 'I\'m a chatbot designed to help you with stress and anxiety.'],
    'i am stressed': ['I\'m so sorry to hear that. Would you like some coping strategies?', 'That can be really tough. Have you tried deep breathing exercises?'],
    'i am anxious': ['I\'m here to listen. Would you like to talk about what\'s on your mind?', 'That can be really overwhelming. Have you tried journaling or meditation?']
}

# Define a dictionary of resources
resources = {
    'hotlines': ['National Suicide Prevention Lifeline: 1-800-273-TALK (8255)', 'Crisis Text Line: Text HOME to 741741'],
    'websites': ['National Alliance on Mental Illness (NAMI): https://www.nami.org/', 'Mental Health America: https://www.mentalhealthamerica.net/']
}

# Define a function to process user input
def process_input(input_text):
    # Tokenize the input text
    inputs = tokenizer.encode_plus(
        input_text,
        add_special_tokens=True,
        max_length=512,
        return_attention_mask=True,
        return_tensors='pt'
    )

    # Get the BERT embeddings
    outputs = model(inputs['input_ids'], attention_mask=inputs['attention_mask'])
    embeddings = outputs.last_hidden_state[:, 0, :]

    # Calculate the similarity between the input and response embeddings
    similarities = []
    for response in responses:
        response_inputs = tokenizer.encode_plus(
            response,
            add_special_tokens=True,
            max_length=512,
            return_attention_mask=True,
            return_tensors='pt'
        )
        response_outputs = model(response_inputs['input_ids'], attention_mask=response_inputs['attention_mask'])
        response_embeddings = response_outputs.last_hidden_state[:, 0, :]
        similarity = cosine_similarity(embeddings, response_embeddings)
        similarities.append(similarity)

    # Get the most similar response
    most_similar_response = np.argmax(similarities)
    return responses[list(responses.keys())[most_similar_response]]

# Define a function to provide resources
def provide_resources():
    return 'Here are some resources that may be helpful:\n\n' + '\n'.join(resources['hotlines']) + '\n\n' + '\n'.join(resources['websites'])

# Main chatbot loop
while True:
    user_input = input('User: ')
    response = process_input(user_input)

    if response:
        print('Chatbot: ', response)
    else:
        print('Chatbot: ', provide_resources())
