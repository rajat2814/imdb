import json

from itertools import chain

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from imdb.movies.models import Director, Genre, Movie

from imdb.users.models import User



class SetupViewSet(viewsets.ViewSet):

	@action(detail=False, methods=['POST'])
	def setup(self, request, *args, **kwargs):

		super_user = User.objects.create

		with open('imdb/administrator/data/imdb.json') as f:
			data = json.load(f)

		# Batching Directors

		directors_list = list(set([x.get('director') for x in data]))

		directors_in_db = Director.objects.filter(name__in=directors_list).values_list('name', flat=True)

		if directors_in_db.count() > 0:
			directors_to_add = list(set(directors_list) - set(directors_in_db))
		else:
			directors_to_add = directors_list

		if directors_to_add:
			directors_obj = [Director(name=x) for x in directors_to_add]
			Director.objects.bulk_create(directors_obj)

		#Batching Genre

		genres_list = list(set(list(chain(*[x.get('genre') for x in data]))))

		genres_in_db = Genre.objects.filter(name__in=genres_list).values_list('name', flat=True)

		if genres_in_db.count() > 0:
			genres_to_add = list(set(genres_list) - set(genres_in_db))
		else:
			genres_to_add = genres_list

		if genres_to_add:
			genres_obj = [Genre(name=x) for x in genres_to_add]
			Genre.objects.bulk_create(genres_obj)

		#Batching Movies

		movies_list = list(set([x.get('name') for x in data]))

		movies_in_db = Movie.objects.filter(name__in=movies_list).values_list('name', flat=True)

		if movies_in_db.count() > 0:
			movies_to_add = list(set(movies_list) - set(movies_in_db))
		else:
			movies_to_add = movies_list

		for movie in data:

			if movie.get('name') in movies_to_add:

				create_dict = {
					'name': movie.get('name'),
					'popularity': movie.get('99popularity'),
					'imdb_score': movie.get('imdb_score')
				}

				try:
					create_dict.update({
						'director': Director.objects.get(name=movie.get('director'))
					})
				except Director.DoesNotExist:
					pass

				added_movie = Movie.objects.create(**create_dict)

				added_movie.genre.add(*[y for y in Genre.objects.filter(name__in=movie.get('genre'))])


		return Response({
			'number_of_directors_batched': len(directors_to_add),
			'number_of_genres_batched': len(genres_to_add),
			'number_of_movies_batched': len(movies_to_add)
		})
