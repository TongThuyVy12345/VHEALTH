from VHealth import app
from flask import Flask, render_template, request, jsonify, session
from VHealth.Text_Predict import Text_classification_predict
from VHealth.Text_Predict.Text_classification_predict import TextClassificationPredict
from VHealth.Text_Predict.Text_classification_predict import TextClassificationPredict
from VHealth.model.LDA import make_texts_corpus
from VHealth.model.SVM import SVM_Model
from VHealth.model.distances import get_most_similar_documents
from VHealth.common import File
from gensim.models.ldamodel import LdaModel
from gensim.test.utils import datapath
from VHealth.model import admin
from googletrans import Translator
from flask_admin import Admin
from VHealth.model import control
from flask import Flask, jsonify
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from wtforms import DateField
from datetime import datetime
from VHealth.model import numerology
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView
import numpy as np
import pandas as pd
import os
import json
import pandas as pd
import gensim  # noqa
import joblib  # noqa
import VHealth.common.Settings
import time
app = Flask(__name__)
admin = Admin(app, name="Admin Vhealth")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/chat")
def chat():
    return render_template('Chat.html')


@app.route("/schedule")
def schedule():
    return render_template('schedule.html')


@app.route("/schedule_post", methods=["POST"])
def schedule_post():
    global is_task_finished
    is_task_finished = False
    driver = webdriver.Chrome('../Chrome/chromedriver.exe')
    name_task = request.form.get('task_name')
    # url = request.form.get('url')
    url = "https://www.youtube.com/playlist?list=PLxKLMN7WdG5Co3waYK4T0jFDIjWfEIFmy"
    element_url = request.form.get('element_url')
    element_title = request.form.get('element_title')
    datatime = request.form.get('start_date')
    driver.get(url)
    title = driver.find_elements(By.CSS_SELECTOR, element_title)
    url = driver.find_elements(By.CSS_SELECTOR, element_url)
    schedule.every().day.at(datatime).do(schedule_post)
    while True:
        schedule.run_pending()
        time.sleep(1)
    is_task_finished = True
    if is_task_finished:
        completed = "Finished"
    else:
        completed = "Wait"
    with open('Data_Execrises.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for i in range(len(title)):
            writer.writerow(
                [title[i].text, url[i].get_attribute("href"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    return render_template('schedule.html', name_task=name_task, url=url, datatime=datetime,
                           element_title=element_title, element_url=element_url, completed=completed)


@app.route("/quizHolland")
def tempale_holland():
    return render_template('Holland.html')


@app.route("/holland", methods=["POST"])
def holland():
    # Get the message from the request
    data = request.json
    msg = data.get('message')
    # Initialize variables to store total scores
    total_scoreA, total_scoreB, total_scoreC, total_scoreD, total_scoreE, total_scoreF = 0, 0, 0, 0, 0, 0
    # If the message is valid, return the next question
    if msg:
        # Load JSON file
        with open('C:\\Users\\ADMIN\\PycharmProjects\\ModelQA_NCKH\\VHealth\\data\\JSON\\HOLLAND_JSON.json', 'r',
                  encoding="utf8") as json_data:
            intents = json.load(json_data)

        # Create a Pandas DataFrame from the JSON data
        df = pd.DataFrame(intents)
        luachon1 = "Chưa bao giờ đúng"
        luachon2 = "Đúng trong 1 vài trường hợp"
        luachon3 = "Đúng trong đa số các trường hợp"
        luachon4 = "Đúng trong tất cả trường hợp"
        # Get data input
        for i in range(len(df)):
            if df['Label'][i] == 'A':
                total_scoreA += int(msg)
            if df['Label'][i] == 'B':
                total_scoreA += int(msg)
            if df['Label'][i] == 'C':
                total_scoreC += int(msg)
            if df['Label'][i] == 'D':
                total_scoreD += int(msg)
            if df['Label'][i] == 'E':
                total_scoreE += int(msg)
            if df['Label'][i] == 'F':
                total_scoreF += int(msg)
        max_score = max(total_scoreA, total_scoreB, total_scoreC, total_scoreD, total_scoreE, total_scoreF)
        # Get the current index from the session
        max_index = len(df) - 1

        index = session.get("index", 0)
        if index >= max_index:
            if max_score == total_scoreA:
                content_max = "Chào bạn, chào mừng bạn đến với trắc nghiệm nghề nghiệp Holland. Đầu tiên cảm ơn bạn đã tham gia thử nghiệm trắc nghiệm. Kết quả của bạn sẽ được trả chi tiết ngay sau đây: " \
                              "BẢNG A: Realistic - Người thực tế" \
                              "Người thuộc nhóm sở thích nghề nghiệp này thường có khả năng về: kỹ thuật, công nghệ, hệ thống; ưa thích làm việc với đồ vật, máy móc, động thực vật; thích làm các công việc ngoài trời. Ngành nghề phù hợp với nhóm này bao gồm: Các nghề về kiến trúc, an toàn lao động, nghề mộc, xây dựng, thủy  sản, kỹ thuật, máy tàu thủy, lái xe, huấn luyện viên, nông – lâm nghiệp (quản lý trang trại, nhân giống cá, lâm nghiệp…), cơ khí (chế tạo máy, bảo trì và sữa chữa thiết bị, luyện kim, cơ khí ứng dụng, tự động...), điện - điện tử, địa lý - địa chất (đo đạc, vẽ bản đồ địa chính), dầu khí, hải dương học, quản lý công nghiệp.."
            elif max_score == total_scoreB:
                content_max = "Chào bạn, chào mừng bạn đến với trắc nghiệm nghề nghiệp Holland. Đầu tiên cảm ơn bạn đã tham gia thử nghiệm trắc nghiệm. Kết quả của bạn sẽ được trả chi tiết ngay sau đây: " \
                              "BẢNG B: Investigative - Người nghiên cứu" \
                              "Có khả năng về: quan sát, khám phá, phân tích đánh giá và giải quyết các vấn đề. Ngành nghề phù hợp với nhóm này bao gồm: Các ngành thuộc lĩnh vực khoa học tự nhiên (toán, lý, hóa, sinh, địa lý, địa chất, thống kê…); khoa học xã hội (nhân học, tâm lý, địa lý…); y - dược (bác sĩ gây mê, hồi sức, bác sĩ phẫu thuật, nha sĩ…); khoa học công nghệ (công nghệ thông tin, môi trường, điện, vật lý kỹ thuật, xây dựng…); nông lâm (nông học, thú y…)"
            elif max_score == total_scoreC:
                content_max = "Chào bạn, chào mừng bạn đến với trắc nghiệm nghề nghiệp Holland. Đầu tiên cảm ơn bạn đã tham gia thử nghiệm trắc nghiệm. Kết quả của bạn sẽ được trả chi tiết ngay sau đây:" \
                              "BẢNG C: Artistic - Người có tính nghệ sĩ" \
                              "Có khả năng về: nghệ thuật, khả năng về trực giác, khả năng tưởng tượng cao, thích làm việc trong các môi trườn mang tính ngẫu hứng, không khuôn mẫu.Ngành nghề phù hợp với nhóm này bao gồm: Các ngành về văn chương; báo chí (bình luận viên, dẫn chương trình…); điện ảnh, sân khấu, mỹ thuật, ca nhạc, múa, kiến trúc, thời trang, hội họa, giáo  viên dạy sử/Anh văn, bảo tàng, bảo tồn..."
            elif max_score == total_scoreD:
                content_max = "Chào bạn, chào mừng bạn đến với trắc nghiệm nghề nghiệp Holland. Đầu tiên cảm ơn bạn đã tham gia thử nghiệm trắc nghiệm. Kết quả của bạn sẽ được trả chi tiết ngay sau đây:" \
                              "BẢNG D: Social - Người có tính xã hội " \
                              "Có khả năng về: ngôn ngữ, giảng giải, thích làm những việc như giảng dạy, cung cấp thông tin, sự chăm sóc, giúp  đỡ, hoặc huấn luyện cho người khác. Ngành nghề phù hợp với nhóm này bao gồm: sư phạm;  giảng viên; huấn luyện viên điền kinh; tư vấn - hướng nghiệp; công tác xã hội, sức khỏe cộng đồng, thuyền  trưởng, thầy tu, thư viện, bác sĩ chuyên khoa, thẩm định giá, nghiên cứu quy hoạch đô thị, kinh tế gia đình, tuyển dụng nhân sự, cảnh sát, xã hội học, bà đỡ, chuyên gia về Xquang, chuyên gia dinh dưỡng…"
            elif max_score == total_scoreE:
                content_max = "Chào bạn, chào mừng bạn đến với trắc nghiệm nghề nghiệp Holland. Đầu tiên cảm ơn bạn đã tham gia thử nghiệm trắc nghiệm. Kết quả của bạn sẽ được trả chi tiết ngay sau đây:" \
                              "BẢNG E: Enterprising - Dám nghĩ, dám làm" \
                              "Có khả năng về: kinh doanh, mạnh bạo, dám nghĩ dám làm, có thể gây ảnh hưởng, thuyết phục Người khác, có khả năng quản lý.Ngành nghề phù hợp với nhóm này bao gồm: Các ngành về quản trị kinh doanh (quản lý khách sạn, quản trị nhân sự,…), thương mại, marketing, kế toán – tài chính, luật sư, dịch vụ khách hàng, tiếp viên hàng không, thông dịch viên, pha chế rượu, kỹ sư công nghiệp (ngành kỹ thuật hệ thống công nghiệp), bác sĩ cấp cứu, quy hoạch đô thị, bếp trưởng (nấu ăn), báo chí (phóng viên, biên tập viên…)"
            elif max_score == total_scoreF:
                content_max = "Chào bạn, chào mừng bạn đến với trắc nghiệm nghề nghiệp Holland. Đầu tiên cảm ơn bạn đã tham gia thử nghiệm trắc nghiệm. Kết quả của bạn sẽ được trả chi tiết ngay sau đây:" \
                              "BẢNG F: Conventional - Người công chức" \
                              "Có khả năng về: số học, thích thực hiện những công việc chi tiết, thích làm việc với những số liệu,  theo chỉ dẫn của người khác hoặc các công việc văn phòng. Ngành nghề phù hợp với nhóm này bao gồm: Các ngành nghề về hành chính, thống kê, thanh tra ngành, người giữ trẻ, điện thoại viên..."

            return jsonify(
                {'success': True, 'message': content_max, 'labelA': total_scoreA, 'labelB': total_scoreB,
                 'labelC': total_scoreC, 'labelB': total_scoreD, 'labelE': total_scoreE, 'labelF': total_scoreF,
                 'choice': luachon1, 'choice2': luachon2, 'choice3': luachon3, 'choice4': luachon4}), 200
        else:
            index += 1
            question = df.iloc[index]['Question']

            # Clear the session once the quiz is complete
            session.clear()
            # Store the updated index in the session
            session["index"] = index
        # Return the question as a JSON response, along with the updated index
        return jsonify(
            {'success': True, 'message': question, 'index': index, 'msg': msg, 'choice': luachon1, 'choice2': luachon2,
             'choice3': luachon3, 'choice4': luachon4}), 200

        # If the message is invalid, return an error response
    else:
        return jsonify({'success': False, 'message': 'Dữ liệu không hợp lệ'}), 400


@app.route("/quizMBTI")
def tempale_mbti():
    return render_template('MBTI.html')


@app.route("/mbti", methods=["POST"])
def mbti():
    # Get the message from the request
    data = request.json
    msg = data.get('message')
    # Initialize variables to store total scores
    total_scoreA, total_scoreB, total_scoreC, total_scoreD, total_scoreE, total_scoreF, total_scoreG, total_scoreH, total_scoreM, total_scoreN, total_scoreO, total_scoreP, total_scoreQ, total_scoreR, = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    # If the message is valid, return the next question
    if msg:
        # Load JSON file
        with open('C:\\Users\\ADMIN\\PycharmProjects\\ModelQA_NCKH\\VHealth\\data\\JSON\\BMTI.json', 'r',
                  encoding="utf8") as json_data:
            intents = json.load(json_data)

        df = pd.DataFrame(intents)
        for i in range(len(df)):
            if msg == "A":
                if df['Label_A'][i] == '1':
                    total_scoreA += 1
                if df['Label_A'][i] == '3':
                    total_scoreC += 1
                if df['Label_A'][i] == '5':
                    total_scoreE += 1
                if df['Label_A'][i] == '7':
                    total_scoreG += 1
                if df['Label_A'][i] == '9':
                    total_scoreM += 1
                if df['Label_A'][i] == '11':
                    total_scoreO += 1
                if df['Label_A'][i] == '13':
                    total_scoreQ += 1
            if msg == "B":
                if df['Label_B'][i] == '2':
                    total_scoreB += 1
                if df['Label_B'][i] == '4':
                    total_scoreD += 1
                if df['Label_B'][i] == '6':
                    total_scoreF += 1
                if df['Label_B'][i] == '8':
                    total_scoreH += 1
                if df['Label_B'][i] == '10':
                    total_scoreN += 1
                if df['Label_B'][i] == '12':
                    total_scoreP += 1
                if df['Label_B'][i] == '14':
                    total_scoreR += 1
        # max_score = max(total_scoreA, total_scoreB, total_scoreC, total_scoreD,total_scoreE, total_scoreF, total_scoreM, total_scoreN,total_scoreQ, total_scoreO,total_scoreP)
        # Tạo danh sách các cặp giá trị và nhãn
        E = total_scoreA
        I = total_scoreB
        S = total_scoreC + total_scoreE
        N = total_scoreD + total_scoreF
        T = total_scoreG + total_scoreM
        F = total_scoreH + total_scoreN
        J = total_scoreO + total_scoreQ
        P = total_scoreP + total_scoreR
        scores = [
            (E, "E"),
            (I, "I"),
            (S, "S"),
            (N, "N"),
            (T, "T"),
            (F, "F"),
            (J, "J"),
            (P, "P"),
        ]

        # Sắp xếp danh sách theo giá trị giảm dần
        sorted_scores = sorted(scores, reverse=True)

        top_4_labels = []
        for score, label in sorted_scores[:4]:
            top_4_labels.append(label)
        result = ''.join(top_4_labels)
        overlap_values = []
        A = {"INFP", "INFJ", "ENFJ", "ENFP", "INTJ", "ENTJ", "ENTP", "INTP", "ESFJ", "ESFP", "ISFJ", "ISFP", "ESTJ",
             "ESTP", "ISTJ", "ISTP"}

        for label in A:
            if label == result:
                content = "OK"
            else:
                content = "Ko "

        max_index = len(df) - 1
        index = session.get("index", 0)
        if index >= max_index:

            return jsonify(
                {'success': True, 'question': content, 'labelA': total_scoreA, 'labelB': total_scoreB,
                 'labelC': total_scoreC, 'labelB': total_scoreD, 'labelE': total_scoreE, 'labelF': total_scoreF,
                 'choice1': "Null", 'choice2': "Null"}), 200
        else:
            index += 1
            question = df.iloc[index]['Question']
            answer1 = df.iloc[index]['Answer_A']
            answer2 = df.iloc[index]['Answer_B']
            # Clear the session once the quiz is complete
            session.clear()
            # Store the updated index in the session
            session["index"] = index

        return jsonify(
            {'success': True, 'question': question, 'index': index, 'msg': msg, 'choice1': answer1,
             'choice2': answer2
             }), 200
    else:
        return jsonify({'success': False, 'question': 'Dữ liệu không hợp lệ'}), 400


@app.route("/login")
def login():
    return render_template('login.html')


# Register
@app.route("/register")
def register():
    return render_template("register.html")


# Numberology
@app.route("/get_bot_response", methods=["GET", "POST"])
def get_bot_response():
    message = request.form.get('question_test')
    if datetime.strptime(message, '%d-%m-%Y'):
        response = numerology.numerology(message)
    if "exercise" in message:
        response = control.show_post(message)
    return render_template(
        'Chat.html', response=response
    )


if __name__ == '__main__':
    app.run(debug=True)
