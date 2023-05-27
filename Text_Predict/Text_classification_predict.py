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
    new_sentences=[query]
    X_train = vectorizer.fit_transform(df['Question_tokens'])
    X_new = vectorizer.transform(new_sentences)
    predictions = svm_model.predict(X_new)
    for sentence, prediction in zip(df['Question'], predictions):
        similarity = "Similar" if prediction == 1 else "Dissimilar"
        # print(f"'{sentence}' is {similarity} to the new sentence.")
        index = df[df['Question'] == sentence].index[0]
        answer = df.loc[index, 'Answer']
        # print(f"Answer: {answer}")
        return answer
query="what is the psychology ?"
print(Text_Predict(query))
