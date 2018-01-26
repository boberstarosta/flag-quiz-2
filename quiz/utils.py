import requests
from bs4 import BeautifulSoup
from .models import Country


def scrape_countries():
	page = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)")
	soup = BeautifulSoup(page.text, "html.parser")

	table = None
	for caption in soup.find_all("caption"):
		if caption.get_text() == "Countries and areas ranked by population in 2017":
			table = caption.find_parent("table")

	if table is not None:
		countries = []
		for tr in table.find_all("tr"):
			tds = tr.find_all("td")
			if len(tds) == 7:
				name_col = tds[1]
				name = name_col.get_text().split("[")[0].strip()
				if name == "World":
					continue
				
				population = int(tds[5].get_text().replace(",", ""))
				
				countries.append((name, population))
				
		return countries
	
def insert_countries(countries):
	for row in countries:
		name = row[0]
		pop = row[1]
		country = Country(country_name=name, population=pop)
		country.save()
		