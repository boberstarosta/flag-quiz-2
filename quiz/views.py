from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Country
from .quiz import Quiz


def index(request):
	levels = [50, 100, None]
	return render(request, "index.html", {"levels": levels})
	
	
def list_(request):
	all_countries = Country.objects.order_by("country_name").all()
	context = {"all_countries": all_countries}
	return render(request, "list.html", context)


def start(request, country_count=None):
	quiz = Quiz(country_count = country_count)
	return HttpResponseRedirect(reverse("quiz:quiz", args=[quiz.id]))


def quiz(request, quiz_id):
	try:
		quiz = Quiz.instances[quiz_id]
	except KeyError:
		return HttpResponseRedirect(reverse("quiz:index"))
	question = quiz.get_current_question()
	context = {
		"question_num": quiz.current_question_index + 1,
		"question_count": len(quiz.questions),
		"question": question,
	}
	return render(request, "quiz.html", context)


def answer(request, quiz_id, answer_country_id):
	quiz = Quiz.instances[quiz_id]
	quiz.answer_current_question(answer_country_id)
	return HttpResponseRedirect(reverse("quiz:quiz", args=[quiz_id]))
	
