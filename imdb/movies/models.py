from django.db import models


class Genre(models.Model):
	name = models.CharField(max_length=1024)

	def __str__(self):
		return 'Genre: {0}'.format(self.name)


class Director(models.Model):
	name = models.TextField(max_length=2048)

	def __str__(self):
		return 'Director Name: {0}'.format(self.name)


class Movie(models.Model):
	popularity = models.FloatField(default=0.0)
	director = models.ForeignKey(Director, on_delete=models.DO_NOTHING)
	imdb_score = models.FloatField(default=0.0)
	name = models.TextField()
	genre = models.ManyToManyField(Genre)

	
	def __str__(self):
		return 'Movie Name: {0}'.format(self.name)