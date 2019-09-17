from django.urls import path

from . import views

# wire new views into urls module
urlpatterns = [
	# ex: /polls/
    path('', views.index, name='index'),
	# ex: /polls/5
	path('<int:question_id>/', views.detail, name='detail'),
	# ex: /polls/5/result
	path('<int:question_id>/results/', views.results, name='results'),
	# ex: /polls/5/vote
	path('<int:question_id>/vote', views.vote, name='vote'),
]
