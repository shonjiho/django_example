
### 3 Rule of Migration

 - (models.py) change model

 - python manage.py makemigrations # make migration about model`s change

 - python manage.py migrate # apply change to database

# 마이그레이션 파일 생성
$ python manage.py makemigrations <app-name>

# 마이그레이션 적용
$ python manage.py migrate <app-name>

# 마이그레이션 적용 현황
$ python manage.py showmigrations <app-name>

# 지정 마이그레이션의 SQL 내역
 python manage.py sqlmigrate <app-name> <migration-name>
