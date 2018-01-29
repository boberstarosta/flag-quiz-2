from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Country
from .quiz import Quiz


def login(request):
	return render(request, "registration/login.html", {})

@login_required
def home(request):
	return render(request, "index.html", {"levels": Quiz.levels.values()})

def index(request):
	levels = Quiz.levels.values()
	return render(request, "index.html", {"levels": levels})
	
	
def list_(request):
	all_countries = Country.objects.order_by("country_name").all()
	context = {"all_countries": all_countries}
	return render(request, "list.html", context)


def start(request, level_name=None):
	try:
		level = Quiz.levels[level_name]
	except KeyError:
		return HttpResponseRedirect(reverse("quiz:index"))
	quiz = Quiz(level)
	return HttpResponseRedirect(reverse("quiz:quiz", args=[quiz.id]))


def quiz(request, quiz_id):
	try:
		quiz = Quiz.instances[quiz_id]
	except KeyError:
		return HttpResponseRedirect(reverse("quiz:index"))
	question = quiz.get_current_question()
	context = {
		"quiz_id": quiz.id,
		"quiz": quiz,
		"question": question,
	}
	return render(request, "quiz.html", context)


def answer(request, quiz_id, answer_country_id):
	try:
		quiz = Quiz.instances[quiz_id]
	except KeyError:
		return HttpResponseRedirect(reverse("quiz:index"))
	quiz.answer_current_question(answer_country_id)
	if quiz.has_all_answers():
		return HttpResponseRedirect(reverse("quiz:results", args=[quiz_id]))
	else:
		return HttpResponseRedirect(reverse("quiz:quiz", args=[quiz_id]))
	
def results(request, quiz_id):
	try:
		quiz = Quiz.instances[quiz_id]
	except KeyError:
		return HttpResponseRedirect(reverse("quiz:index"))
	context = {"quiz": quiz}
	return render(request, "results.html", context)
	
