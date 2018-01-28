from django.urls import path

from . import views


app_name = "quiz"

urlpatterns = [
	path("", views.index, name="index"),
	path("list/", views.list_, name="list"),
	path("start/<int:country_count>/", views.start, name="start"),
	path("quiz/<int:quiz_id>/", views.quiz, name="quiz"),
	path("answer/<int:quiz_id>/<int:answer_country_id>/", views.answer, name="answer"),
	path("results/<int:quiz_id>/", views.results, name="results"),
]


