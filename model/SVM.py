# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import GridSearchCV
# from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
#
# from sklearn.svm import SVC
# from VHealth.common import File
# import codecs
# import os
# import json
# import pandas as pd
# import json
# import pickle
#
#
# def get_parentDir():
#     fileDir = os.path.dirname(os.path.abspath(__file__))
#     parentDir = os.path.dirname(fileDir)
#     return parentDir
#
#
# csv_path = os.path.join(get_parentDir(), 'data', 'CSV', 'FINAL_EN.csv')
# df = pd.read_csv(csv_path, encoding='utf8')
#
# # Preprocess the text data using TF-IDF vectorization
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(df['Question_tokens'])
#
# # X_train, X_test, y_train, y_test = train_test_split(X, df['Label'], test_size=0.2, random_state=42)
#
# target_sentence = "where can i learn about types of mental health treatment?"
# target_vector = vectorizer.transform([target_sentence])
#
# svm_model = SVC(kernel='linear', C=2, gamma=0.1, probability=True)
# svm_model.fit(X, range(len(df['Question_tokens'])))
# # model_path = os.path.join(get_parentDir(), 'model', 'svm_model.pkl')
# # with open(model_path, 'wb') as file:
# #     pickle.dump(svm_model, file)
# predicted_index = svm_model.predict(target_vector)[0]
# most_similar_sentence = df['Question_tokens'][predicted_index]
# print("Câu giống nhất:", most_similar_sentence)
# # accuracy = svm_model.score(X_test, y_test)
# # print("Accuracy:", accuracy)
# #
# # # Calculate and print F1 score
# # y_pred = svm_model.predict(X_test)
# # f1 = f1_score(y_test, y_pred, average='weighted')
# # print("F1 Score:", f1)
# #
# # # Calculate and print precision
# # precision = precision_score(y_test, y_pred, average='weighted')
# # print("Precision:", precision)
# #
# # # Calculate and print recall
# # recall = recall_score(y_test, y_pred, average='weighted')
# # print("Recall:", recall)
