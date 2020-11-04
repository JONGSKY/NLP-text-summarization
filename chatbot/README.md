## Intro File

#### crawling_data.py

- [네이버 뉴스](https://news.naver.com/)에서 제공하는 헤드라인뉴스, 정치, 경제, 사회, 생활/문화, 세계, IT/과학 기사 데이터를 가져옵니다.

#### summarization.py

#### chatbot.py

- 서버 8080 포트로 카카오 챗봇을 실행시킵니다.

#### crontab

1. crawling_data.py 은 하루에 8번 3시간 주기로 실행됩니다.
  - ``` 1 */3 * * * ~/anaconda3/envs/python_3/bin/python ~/workspace/NLP-text-summarization/chatbot/crawling_data.py > ~/workspace/NLP-text-summarization/chatbot/log/crawling/crawling_`date "+\%Y-\%m-\%d \%H:\%M:\%S"`.log 2>&1 ```
2. summarization.py 은 하루에 8번 crawling_data.py 실행 이후 실행됩니다.
  - ``` 5 */3 * * * ~/anaconda3/envs/python_3/bin/python ~/workspace/NLP-text-summarization/chatbot/summarization.py > ~/workspace/NLP-text-summarization/chatbot/log/summarization/summarization_`date "+\%Y-\%m-\%d \%H:\%M:\%S"`.log 2>&1 ```
3. chatbot.py 는 하루에 8번 summarization.py 실행 이후 refresh됩니다.
  - ``` 10 */3 * * * ~/anaconda3/envs/python_3/bin/python ~/workspace/NLP-text-summarization/chatbot/chatbot.py > ~/workspace/NLP-text-summarization/chatbot/log/chatbot/chatbot_`date "+\%Y-\%m-\%d \%H:\%M:\%S"`.log 2>&1 ```


## Reference site

#### summarization
- [TextRank 기법을 이용한 핵심 어구 추출 및 텍스트 요약](https://bab2min.tistory.com/552)
- [‘쉽게 설명한’ 구글의 페이지 랭크 알고리즘](https://sungmooncho.com/2012/08/26/pagerank/)
- [페이지 랭크 알고리즘(Page Rank Algorithm)](https://medium.com/@dbwodlf3/%ED%8E%98%EC%9D%B4%EC%A7%80-%EB%9E%AD%ED%81%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-page-rank-algorithm-6d83c78fcbd3)
- [PageRank 알고리즘 이해하기](https://eyeballs.tistory.com/36)
- [TextRank 를 이용한 키워드 추출과 핵심 문장 추출 (구현과 실험)](https://lovit.github.io/nlp/2019/04/30/textrank/)
- [페이지랭크 알고리즘(PageRank Algorithm)을 사용하여 웹 사이트의 순위 매기기](https://kr.mathworks.com/help/matlab/math/use-page-rank-algorithm-to-rank-websites.html)

#### chatbot
- [kakao i developers - 챗봇 주요 기능 사용법](https://i.kakao.com/docs/tutorial-chatbot-key-features#%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4-%EC%95%88%EC%97%90%EC%84%9C-%EB%B8%94%EB%A1%9D-%EB%A7%8C%EB%93%A4%EA%B8%B0)
- [kakao i developers - 응답 타입별 JSON 포맷](https://i.kakao.com/docs/skill-response-format#skillpayload)

#### crontab
- [리눅스 크론탭(Linux Crontab) 사용법](https://jdm.kr/blog/2)
- [[Linux] Python(.py)을 가상환경(virtualenv)에서 주기별로 실행하기](https://teddylee777.github.io/linux/python-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-crontab-%EC%A3%BC%EA%B8%B0%EB%A7%88%EB%8B%A4-%EC%8B%A4%ED%96%89)
