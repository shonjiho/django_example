
### 3 Rule of Migration

 - (models.py) change model

 - python manage.py makemigrations # make migration about model`s change

 - python manage.py migrate # apply change to database

### 마이그레이션 파일 생성
$ python manage.py makemigrations <app-name>

### 마이그레이션 적용
$ python manage.py migrate <app-name>

### 마이그레이션 적용 현황
$ python manage.py showmigrations <app-name>

### 지정 마이그레이션의 SQL 내역
 python manage.py sqlmigrate <app-name> <migration-name>

# Django Model API 사용하기

Model API 를 확인해보고 테스트할 때 Django 쉘환경을 추천
(Django 프로젝트 PATH를 참조해준다.)
```py
python manage.py shell
```

DB Model API reference(https://docs.djangoproject.com/en/2.2/topics/db/queries/) 

Tutorial (https://docs.djangoproject.com/en/2.2/intro/tutorial02)
