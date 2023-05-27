from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from VHealth.common import File
import codecs
import os
import json
import pandas as pd
import json
import pickle

def get_parentDir():
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    return parentDir

csv_path = os.path.join(get_parentDir(), 'data', 'CSV', 'FINAL_EN.csv')
df = pd.read_csv(csv_path, encoding='utf8')

# Preprocess the text data using TF-IDF vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Question_tokens'])

X_train, X_test, y_train, y_test = train_test_split(X, df['Label'], test_size=0.2, random_state=42)
svm_model = SVC(kernel='linear', C=1, gamma=10.0, probability=True)
svm_model.fit(X_train, y_train)

# Save the trained SVM model
model_file = 'C:\\Users\ADMIN\PycharmProjects\ModelQA_NCKH\VHealth\svm_model.pkl'
with open(model_file, 'wb') as file:
    pickle.dump(svm_model, file)
