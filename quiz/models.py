import os

from django.db import models


def get_image_path(instance, filename):
	return os.path.join("images", str(instance.id), filename)


class Flag(models.Model):
	flag_image = models.ImageField(upload_to=get_image_path)


class Country(models.Model):
	flag = models.ForeignKey(Flag, on_delete=models.CASCADE)
	country_name = models.CharField(max_length=100)
	population = models.IntegerField(default=0)
	