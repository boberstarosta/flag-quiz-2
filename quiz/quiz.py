import random

from .models import Country


class Question:
	def __init__(self, country, all_countries, fake_count, mode="flags"):
		self.country = country
		all_fakes = [c for c in all_countries if c != country]
		fakes = random.sample(all_fakes, fake_count)
		self.answers = [country] + fakes
		random.shuffle(self.answers)
		self.answer = None
		self.mode = mode


class Difficulty:
	def __init__(self, name, country_count, desc):
		self.name = name
		self.country_count = country_count
		self.desc = desc
		

class Quiz:
	instances = {}
	last_id = random.randrange(1000000)
	
	levels = {
			"Easy": Difficulty("Easy", 50, "50 most populous"),
			"Medium": Difficulty("Medium", 100, "100 most populous"),
			"Hard": Difficulty("Hard", None, "ALL"),
		}
	
	def __init__(self, level, question_count=30, fake_count=4):
		Quiz.last_id += 1
		self.id = Quiz.last_id
		Quiz.instances[self.id] = self
		
		country_count = level.country_count
		self.questions = self.generate_questions(country_count, question_count, fake_count)
		self.current_question_index = 0
	
	def generate_questions(self, country_count, question_count, fake_count):
		result = []
		
		all_countries = Country.objects.order_by("-population").all()[:country_count]
		used_countries = []
		
		for i in range(question_count):
			unused_countries = [c for c in all_countries if c not in used_countries]
			country = random.choice(unused_countries)
			used_countries.append(country)
			mode = "flags" if i < question_count // 2 else "names"
			question = Question(country, all_countries, fake_count, mode=mode)
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
	
	def question_count(self):
		return len(self.questions)
	
	def good_answer_question_list(self):
		return [q for q in self.questions if q.answer == q.country]
	
	def wrong_answer_question_list(self):
		return [q for q in self.questions if q.answer != q.country]
		
	def good_answer_count(self):
		return len(self.good_answer_question_list())
	
	def has_all_answers(self):
		return None not in [q.answer for q in self.questions]
	
	def results_message(self):
		ratio = self.good_answer_count() / self.question_count()
		if ratio == 1.0:
			return "Perfect!"
		elif ratio >= 0.90:
			return "Excellent!"
		elif ratio >= 0.80:
			return "Very good."
		elif ratio >= 0.70:
			return "Good."
		elif ratio >= 0.60:
			return "Not bad."
		else:
			return "You can do better."
	



