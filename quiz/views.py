from django.shortcuts import render

from .models import Country


def index(request):
	all_countries = Country.objects.all()
	context = {'all_countries': all_countries}
	return render(request, 'index.html', context)