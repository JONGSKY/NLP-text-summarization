from flask import Flask, request, jsonify
import sys, os
import datetime
import pandas as pd

os.system("fuser -k 8080/tcp")
               
app = Flask(__name__)

FILE_TIME = datetime.datetime.now().strftime('%Y%m%d-%H')
time_objective = f"{FILE_TIME}.csv"

# BASE_DIR = os.getcwd()
BASE_DIR = "/home/jingsky/workspace/NLP-text-summarization/chatbot/"
DATA_DIR = "chatbot_data"
FILE_NAME = time_objective
FILE_NAME

data = pd.read_csv(os.path.join(BASE_DIR, DATA_DIR, FILE_NAME))

news_type_list = ['today_main_news', 'section_politics', 'section_economy', 'section_society','section_life','section_world','section_it']

all_data_dict = {}

quick_replies = [{
        "messageText": "헤드라인 기사",
        "action": "message",
        "label": "헤드라인 기사"
      },
      {
        "messageText": "정치 뉴스",
        "action": "message",
        "label": "정치 뉴스"
      },
      {
        "messageText": "경제 뉴스",
        "action": "message",
        "label": "경제 뉴스"
      },
      {
        "messageText": "사회 뉴스",
        "action": "message",
        "label": "사회 뉴스"
      },
      {
        "messageText": "생활/문화 뉴스",
        "action": "message",
        "label": "생활/문화 뉴스"
      },
      {
        "messageText": "세계 뉴스",
        "action": "message",
        "label": "세계 뉴스"
      },
      {
        "messageText": "IT/과학 뉴스",
        "action": "message",
        "label": "IT/과학 뉴스"
      }
    ]
for news_type in news_type_list:
    data_list = []
    for i in range(len(data[data['news_type'] == news_type])):
        data_dict = {}

        reset_df = data[data['news_type'] == news_type].reset_index(drop=True)
        
        title = reset_df.loc[i].title
        description = reset_df.loc[i].summarisation
        imageUrl = reset_df.loc[i].image_url
        webLinkUrl = reset_df.loc[i].news_url

        data_dict['title'] = title
        data_dict['description'] = description
        data_dict['thumbnail'] = {"imageUrl":imageUrl}
        data_dict['buttons'] = [{"action": "message", "label": "3줄 요약보기", "messageText": '<기사제목> \n\n' + title + '\n\n <기사3줄요약> \n\n' + '.\n'.join(description.split('.'))},
                                {"action":  "webLink", "label": "뉴스기사 보러가기", "webLinkUrl": webLinkUrl}]   
        
        data_list.append(data_dict)
        # data_list.append(quick_replies)

    all_data_dict[news_type] = data_list    

@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():

    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    if content == u"헤드라인 기사":
        dataSend={
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": all_data_dict['today_main_news']
                        }
                    }
                ],
                    "quickReplies": quick_replies
            }
        }
    elif content == u"정치 뉴스":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": all_data_dict['section_politics']
                        }
                    }
                ],
                    "quickReplies": quick_replies
            }
        }
    elif content == u"경제 뉴스":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": all_data_dict['section_economy']
                        }
                    }
                ],
                    "quickReplies": quick_replies
            }
        }
    elif content == u"사회 뉴스":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": all_data_dict['section_society']
                        }
                    }
                ],
                    "quickReplies": quick_replies
            }
        }
    elif content == u"생활/문화 뉴스":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": all_data_dict['section_life']
                        }
                    }
                ],
                    "quickReplies": quick_replies
            }
        }
    elif content == u"세계 뉴스":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": all_data_dict['section_world']
                        }
                    }
                ],
                    "quickReplies": quick_replies
            }
        }
    elif content == u"IT/과학 뉴스":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": all_data_dict['section_it']
                        }
                    }
                ],
                    "quickReplies": quick_replies
            }
        }
    else:
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "버튼으로 클릭해주세요"
                        }
                    }
                ],
                    "quickReplies": quick_replies
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
