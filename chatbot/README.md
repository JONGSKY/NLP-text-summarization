## Intro File

#### crawling_data.py

- [네이버 뉴스](https://news.naver.com/)에서 제공하는 헤드라인뉴스, 정치, 경제, 사회, 생활/문화, 세계, IT/과학 기사 데이터를 가져옵니다.

#### summarization.py

#### chatbot.py

- 서버 8080 포트로 카카오 챗봇을 실행시킵니다.

#### crontab

1. crawling_data.py 은 하루에 2번 오전6시, 오후6시 2번 실행됩니다.
2. summarization.py 은 하루에 2번 crawling_data.py 실행 이후 실행됩니다.
3. chatbot.py 는 하루에 2번 summarization.py 실행 이후 refresh됩니다.

## Reference site

#### summarization
- 모델링 관련 사이트

#### chatbot
- [kakao i developers - 챗봇 주요 기능 사용법](https://i.kakao.com/docs/tutorial-chatbot-key-features#%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4-%EC%95%88%EC%97%90%EC%84%9C-%EB%B8%94%EB%A1%9D-%EB%A7%8C%EB%93%A4%EA%B8%B0)
- [kakao i developers - 응답 타입별 JSON 포맷](https://i.kakao.com/docs/skill-response-format#skillpayload)

#### Crontab
- [리눅스 크론탭(Linux Crontab) 사용법](https://jdm.kr/blog/2)
