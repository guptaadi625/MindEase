import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Load the data
data = pd.read_csv('/mnt/data/20200325_counsel_chat.csv')

# Select necessary columns
data = data[['questionText', 'answerText']].dropna()

# Split data into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)


# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)

# Fit and transform questionText for the training set, and transform the test set
X_train = vectorizer.fit_transform(train_data['questionText'])
X_test = vectorizer.transform(test_data['questionText'])

# Target variable (answers)
y_train = train_data['answerText']
y_test = test_data['answerText']



# Initialize and train a Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


def get_response(question):
    question_vec = vectorizer.transform([question])
    response = model.predict(question_vec)
    return response[0]

# Test the function
print(get_response("I'm feeling very anxious these days. What should I do?"))
