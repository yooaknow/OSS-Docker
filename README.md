# FastAPI Course Records API

FastAPI를 이용하여 수강기록을 관리하는 간단한 REST API 서버입니다.

수강기록 데이터는 Python 코드 안에 하드코딩하지 않고, `courses.json` 파일에 JSON list 형태로 저장합니다. GET 요청을 통해 전체 수강기록을 조회할 수 있고, POST 요청을 통해 새로운 수강기록을 추가할 수 있습니다.

## 프로젝트 구조

```txt
.
├── main.py
├── models.py
├── courses.json
├── requirements.txt
└── .gitignore
```

## 주요 기능

### GET `/courses`

현재 `courses.json` 파일에 저장되어 있는 전체 수강기록을 반환합니다.

응답 예시:

```json
[
  {
    "course_name": "오픈소스소프트웨어실습",
    "year": "2026",
    "semester": "1",
    "grade": "A+"
  }
]
```

### POST `/courses`

새로운 수강기록을 추가합니다.

요청으로 보낸 과목 정보는 기존 JSON list의 마지막에 추가되고, 변경된 내용은 다시 `courses.json` 파일에 저장됩니다.

요청 Body 예시:

```json
{
  "course_name": "인간로봇상호작용",
  "year": "2026",
  "semester": "2",
  "grade": "A+"
}
```

응답 예시:

```json
{
  "message": "Course added successfully",
  "course": {
    "course_name": "인간로봇상호작용",
    "year": "2026",
    "semester": "2",
    "grade": "A+"
  },
  "total_count": 3
}
```

## 데이터 저장 방식

수강기록은 `courses.json` 파일에 저장됩니다.

POST 요청이 들어오면 서버는 다음 순서로 동작합니다.

1. `courses.json` 파일을 읽습니다.
2. 기존 수강기록 list에 새로운 과목 정보를 추가합니다.
3. 변경된 list를 다시 `courses.json` 파일에 저장합니다.

따라서 서버를 종료했다가 다시 실행해도 추가된 수강기록은 파일에 남아 있습니다.

## 실행 방법

필요한 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

FastAPI 서버를 실행합니다.

```bash
python -m uvicorn main:app --reload
```

서버 실행 후 아래 주소에서 API를 사용할 수 있습니다.

```txt
http://127.0.0.1:8000
```

FastAPI 자동 문서 페이지는 아래 주소에서 확인할 수 있습니다.

```txt
http://127.0.0.1:8000/docs
```

## 사용한 기술

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON file
