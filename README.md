# OSS-Docker

오픈소스소프트웨어실습 실습 5 - Docker

## 과제 개요

기존 Courses FastAPI 애플리케이션을 Docker 환경에서 실행하고 AWS Learner Lab EC2 환경에 배포한 프로젝트입니다.

## 구현 내용

* FastAPI 애플리케이션 Docker 컨테이너화
* Dockerfile 작성
* Docker를 이용한 컨테이너 실행
* AWS EC2 환경 배포
* `restart: always` 정책 적용
* 브라우저를 통한 서비스 접속 확인

## 실행 방법

### Docker 이미지 빌드

```bash
docker build -t todoapi .
```

### Docker 컨테이너 실행

```bash
docker run -d --name todoapi --restart always -p 80:80 todoapi
```

### 실행 상태 확인

```bash
docker ps
```

## 접속 확인

### Courses API

```text
http://EC2_IP/courses
```

### FastAPI Docs

```text
http://EC2_IP/docs
```

## 프로젝트 구성

* `main.py`
* `courses.json`
* `requirements.txt`
* `Dockerfile`
* `.gitignore`
* `.dockerignore`
