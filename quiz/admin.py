from django.contrib import admin

from .models import Country


class CountryAdmin(admin.ModelAdmin):
	fields = ("country_name", "population", "flag_image", "flag_image_tag")
	readonly_fields = ("flag_image_tag",)
	list_display = ("country_name", "population", "flag_thumbnail_tag")
	list_filter = ("country_name", "population")
	search_fields = ("country_name",)
	ordering = ("-population",)

admin.site.register(Country, CountryAdmin)
