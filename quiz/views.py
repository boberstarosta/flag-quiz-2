from django.shortcuts import render

from .models import Country


def index(request):
	all_countries = Country.objects.order_by("country_name").all()
	context = {'all_countries': all_countries}
	return render(request, 'index.html', context)