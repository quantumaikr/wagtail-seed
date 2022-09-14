# Wagtail Seed Project

Wagtail Seed Project 입니다. 

--- 

## 설치하기

설치안내입니다. 다음의 순서를 실행해주세요.

### 1. github 에서 코드 클론 받기

```bash
git clone https://github.com/quantumaikr/wagtail-seed
```

### 2. 가상환경 만들기 virtualenv 

```bash
virtualenv venv
source venv/bin/activate
```

### 3. 관련 라이브러리 install 
```bash
pip install -r requirements.txt
```

### 4. DB 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. admin 계정생성

```bash
python manage.py createsuperuser
```

### 6. 서버 실행

```bash
python manage.py runserver
```

## Docker 관리하기

### 1. 도커 개발(dev) 서버 관리

```bash
docker compose -f docker-compose-dev.yml up -d
docker compose -f docker-compose-dev.yml down

docker compose -f docker-compose-dev.yml exec web python manage.py makemigrations
docker compose -f docker-compose-dev.yml exec web python manage.py migrate
docker compose -f docker-compose-dev.yml exec web python manage.py createsuperuser
```


### 2. 도커 운영(prod) 서버 관리

```bash
docker compose up -d
docker compose down

docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```


### 3. 도커 이미지 삭제

```bash
sudo docker rmi -f $(sudo docker images -aq)
```