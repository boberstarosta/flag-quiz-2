import os

from django.db import models
from django.utils.safestring import mark_safe


class Country(models.Model):
	country_name = models.CharField(max_length=100)
	population = models.IntegerField(default=0)
	flag_image = models.ImageField(upload_to="flags")
	
	def __str__(self):
		return self.country_name
	
	def flag_image_tag(self):
		return mark_safe(u'<img src="%s" />' % self.flag_image.url)
	flag_image_tag.short_description = 'Flag image'
	
	def flag_thumbnail_tag(self):
		return mark_safe(u'<img src="%s" height="30px" />' % self.flag_image.url)
	flag_thumbnail_tag.short_description = 'Flag image'
	
	class Meta:
		verbose_name_plural = "Countries"


