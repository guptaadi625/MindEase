import json

# Sample data for the chatbot dataset
data = [
    {
        "QuestionText": "I'm feeling overwhelmed and anxious, what can I do?",
        "Topic": "anxiety",
        "AnswerText": "It's important to take small steps. Try deep breathing exercises and take breaks when needed. Therapy might also be beneficial."
    },
    {
        "QuestionText": "I've been feeling down and unmotivated lately. Could this be depression?",
        "Topic": "depression",
        "AnswerText": "It's possible, as feelings of sadness and low motivation are common signs. Consider speaking with a mental health professional to explore this."
    },
    {
        "QuestionText": "How can I manage my stress at work?",
        "Topic": "stress management",
        "AnswerText": "Setting boundaries, taking short breaks, and organizing tasks can help. Mindfulness techniques and exercise are also effective for stress management."
    },
    {
        "QuestionText": "What are some coping strategies for anxiety?",
        "Topic": "anxiety",
        "AnswerText": "Deep breathing, grounding exercises, and talking to someone can help. Practicing these techniques regularly can improve results."
    },
    {
        "QuestionText": "I feel alone and like nobody cares about me. What should I do?",
        "Topic": "depression",
        "AnswerText": "These feelings can be very tough. Remember, you're not alone and there are people who care. Reaching out to a therapist can help you feel supported."
    }
    # Add more entries as needed
]

# Save data to JSON file
json_file_path = "/mnt/data/mental_health_chatbot_dataset.json"
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Dataset saved at {json_file_path}")
