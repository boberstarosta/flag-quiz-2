import random

from .models import Country


class Question:
	def __init__(self, country, all_countries, fake_count):
		self.country = country
		all_fakes = [c for c in all_countries if c != country]
		fakes = random.sample(all_fakes, fake_count)
		self.answers = [country] + fakes
		random.shuffle(self.answers)
		self.answer = None


class Quiz:
	instances = {}
	last_id = random.rand_int(1000000)
		
	def __init__(self, country_count=50, question_count=30, fake_count=4):
		Quiz.last_id += 1
		self.id = Quiz.last_id
		Quiz.instances[Quiz.self.id] = self
		self.questions = self.generate_questions(country_count, question_count, fake_count)
		self.current_question_index = 0
	
	def generate_questions(self, country_count, question_count, fake_count):
		result = []
		
		all_countries = Country.objects.order_by("-population").all()[:country_count]
		used_countries = []
		
		for i in range(question_count):
			unused_countries = [c for c in all_countries if c not in used_countries]
			country = random.choice(unused_countries)
			question = Question(country, all_countries, fake_count)
			result.append(question)
		
		return result
	
	def get_current_question(self):
		try:
			return self.questions[self.current_question_index]
		except IndexError:
			return None
		
	def answer_current_question(self, answer_country_id):
		question = self.get_current_question()
		country = Country.objects.get(pk=answer_country_id)
		question.answer = country
		self.current_question_index += 1
	
	def good_answer_count(self):
		return len([q for q in self.questions if q.answer == q.country])



