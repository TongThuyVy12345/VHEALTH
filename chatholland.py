import json
import pandas as pd
import random

import torch

from VHealth.model.model_holland import NeuralNet
from VHealth.Utils import bag_of_words, tokenize
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('C:\\Users\ADMIN\PycharmProjects\ModelQA_NCKH\VHealth\data\JSON\HOLLAND_JSON.json', 'r',
          encoding="utf8") as json_data:
    intents = json.load(json_data)

df = pd.DataFrame(intents)
def get_question_holland():
    for index, row in df.iterrows():
        question=row['Question']
    return question
def calculate_scores(text):
    # Initialize total scores
    total_scoreA = 0
    total_scoreB = 0
    total_scoreC = 0
    total_scoreD = 0
    total_scoreE = 0
    total_scoreF = 0
    answer = text
    for index, row in df.iterrows():
        if answer == 'A':
            total_scoreA += row['A']
        elif answer == 'B':
            total_scoreB += row['B']
        elif answer == 'C':
            total_scoreC += row['C']
        elif answer == 'D':
            total_scoreD += row['D']
        elif answer == 'E':
            total_scoreE += row['E']
        elif answer == 'F':
            total_scoreF += row['F']
        max_score = max(total_scoreA, total_scoreB, total_scoreC, total_scoreD, total_scoreE, total_scoreF)
        return max_score
if __name__ == '__main__':
    print(get_question_holland())
    answer=input()
    print(answer)
    print(calculate_scores(answer))
