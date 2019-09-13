# Django test

### polls Example
https://docs.djangoproject.com/ko/2.2/intro/tutorial01/


### 1. virtualenv setting
    
    python3 -m pip install virtualenv
    cd django_example/
    python3 -m virtualenv myvenv
    source myvenv/bin/activate

    # dependency library install 
    pip install -r requirements.txt
    # current lib dependency 
    pip freeze > requirements.txt

### 2. django setting
    pip install django
    django-admin startproject mysite

### 3. polls app start
    python manage.py startapp polls
    # edit polls/views.py
        # path() arguments is 
    # edit polls/urls.py
    # edit mysite/urls.py
    # make models (Question, Choice) in polls/models.py
    
    # convert python object to SQL Schema
    python manage.py makemigrations polls

    # add polls app in mysite. in mysite/settings.py
    
    # model activation, really make database table.
    python manage.py migrate
   
     

    


