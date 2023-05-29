from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os
import pandas as pd
def Text_Predict(query):
    with open('C:\\Users\ADMIN\PycharmProjects\ModelQA_NCKH\VHealth\svm_model.pkl', 'rb') as file:
        svm_model = pickle.load(file)
    def get_parentDir():
        fileDir = os.path.dirname(os.path.abspath(__file__))
        parentDir = os.path.dirname(fileDir)
        return parentDir

    csv_path = os.path.join(get_parentDir(), 'data', 'CSV', 'FINAL_EN.csv')
    df = pd.read_csv(csv_path, encoding='utf8')
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['Question_tokens'])
    target_sentence = query
    target_vector = vectorizer.transform([target_sentence])
    svm_model.fit(X, range(len(df['Question_tokens'])))
    predicted_index = svm_model.predict(target_vector)[0]
    most_similar_sentence = df['Answer'][predicted_index]
    return(most_similar_sentence)

# Text_Predict("where can i learn about types of mental health treatment?")
