import codecs
import os
def get_parentDir():
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    return parentDir
def get_dbtrain():
    filename = get_parentDir() + '\data\CSV\FINAL_EN.csv'
    f = codecs.open(filename, 'rU', 'utf-8')  # Read Unicode text
    db_train = []
    for i, line in enumerate(f):
        if i == 0:
            continue  # skip header row
        data = line.split(",")
        if len(data) < 4:
            continue  # skip lines with insufficient columns
        db_train.append(
            {"Question_tokens": data[2].replace("\r\n", ""), "Label": (data[0].replace("\ufeff", ""))})
    return db_train

def get_dbtrain_extend():
    # filename = get_parentDir() + '\data\Questions_Extend.csv'
    filename = get_parentDir() + '\data\CSV\FINAL_EN.csv'
    f = codecs.open(filename, 'rU', 'utf-8')  # Read Unicode text
    db_train_extend = []
    for i, line in enumerate(f):
        if i == 0:
            continue  # skip header row
        data = line.split(",")
        if len(data) < 4:
            continue  # skip lines with insufficient columns
        db_train_extend.append(
            {"Question_tokens": data[2].replace("\r\n", ""), "Label": (data[0].replace("\ufeff", ""))})
    return db_train_extend


def get_dbanswers():
    filename = get_parentDir() + '\data\CSV\FINAL_EN.csv'
    f = codecs.open(filename, 'rU', 'utf-8')  # Read Unicode text
    db_answers = []
    for i, line in enumerate(f):
        if i == 0:
            continue  # skip header row
        data = line.split(",")
        if len(data) < 4:
            continue  # skip lines with insufficient columns
        db_answers.append(
            {"Answer": data[3].replace("\r\n", ""), "Label": (data[0].replace("\ufeff", ""))})
    return db_answers


def get_fallback_intent():
    fallback_intent=["Sorry! I don't understand what you mean, please ask a more complete question.",
                       "Please describe fully, so that I can find the most suitable answer!",
                       "I still don't understand your question, please describe more fully!",
                       "I don't understand this question, can you describe it fully or I will send this question to Customer Care Department to assist you!"]
    return fallback_intent
# print(get_dbanswers())
