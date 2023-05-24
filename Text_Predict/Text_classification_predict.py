from VHealth.common import File
import pandas as pd
import random
from VHealth.model.SVM import SVM_Model

class TextClassificationPredict(object):
    def __init__(self, question_test, db_train, db_train_extend, db_answers):
        self.model=self.select_model(1)
        self.question_test = question_test
        self.db_train = db_train
        self.db_answers = db_answers
        self.db_train_extend = db_train_extend

    def select_model(self, i_model):
        if i_model == 1:
            self.model = SVM_Model()
    def Text_Predict(self):
        fallback_intent = File.get_fallback_intent()
        df_train_extend = pd.DataFrame(self.db_train_extend)
        df_train = pd.DataFrame(self.db_train)
        df_answers = pd.DataFrame(self.db_answers)  # List Answers
        db_Predict = []
        db_Predict.append({"Question_tokens": self.question_test})
        df_Predict = pd.DataFrame(db_Predict)
        # Predict in Question Text
        self.select_model(1)
        clf = self.model.clf.fit(df_train_extend["Question_tokens"], df_train_extend.Label)
        list_score = clf.predict_proba(df_Predict["Question_tokens"]).flatten()  # --> array of score
        predicted = list_score.tolist().index(list_score.max())

        if (list_score[predicted] >= 0.5):
            mess = "Answer: "
            mess += df_answers["Answer"][predicted] \
                    + "\n(Score:" + str(round(list_score[predicted], 3)) \
                    + ")"
            return mess
        else:
            print("Question: " + self.question_test + "\n")
            mess = fallback_intent[random.randint(0, len(fallback_intent) - 1)]
            return mess


