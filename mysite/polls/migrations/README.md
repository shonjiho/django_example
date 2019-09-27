
python manage.py makemigrations polls
# make in polls/migration/0001_initial.py

python manage.py sqlmigrate polls 0001
# show generated sql table 

