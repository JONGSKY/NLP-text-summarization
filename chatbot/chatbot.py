from flask import Flask, request, jsonify
import sys
app = Flask(__name__)
import pandas as pd

data = pd.read_csv('chatbot_data/20201008-19.csv')

data_list = []
for i in range(len(data[data['news_type'] == "today_main_news"])):
    data_dict = {}

    title = data[data['news_type'] == "today_main_news"].loc[i].title
    description = data[data['news_type'] == "today_main_news"].loc[i].summarisation
    imageUrl = data[data['news_type'] == "today_main_news"].loc[i].image_url
    webLinkUrl = data[data['news_type'] == "today_main_news"].loc[i].news_url

    data_dict['title'] = title
    data_dict['description'] = description
    data_dict['thumbnail'] = {"imageUrl":imageUrl}
    data_dict['buttons'] = [{"action":  "webLink", "label": "뉴스기사 보러가기", "webLinkUrl": webLinkUrl}]
    
    data_list.append(data_dict)

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
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": data_list
                        }
                    }
                ]
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
                            "items": [
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
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
                            "items": [
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
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
                            "items": [
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
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
                            "items": [
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
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
                            "items": [
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
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
                            "items": [
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                },
                                {
                                    "title": "뉴스기사 제목",
                                    "description": "뉴스기사 요약 3줄",
                                    "thumbnail": {
                                        "imageUrl": "https://imgnews.pstatic.net/image/081/2020/10/07/0003129476_001_20201007151624533.jpg?type=w647"
                                    },
                                    "buttons": [
                                        {
                                            "action":  "webLink",
                                            "label": "뉴스기사 보러가기",
                                            "webLinkUrl": "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003129476"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    else:
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "몰라"
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
