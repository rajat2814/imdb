from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Director, Genre, Movie
from .serializers import MovieSerializer, ListMovieSerializer, GenreSerializer, DirectorSerializer
from .filters import MoviesFilterSet, GenresFilterSet, DirectorsFilterSet


class GenreViewSet(viewsets.ModelViewSet):

	queryset = Genre.objects.all()
	filterset_class = GenresFilterSet
	serializer_class = GenreSerializer

	def create(self, request):
		if not request.user.is_superuser:
			return Response({
					'Unauthorized Call'
				}, status=status.HTTP_401_UNAUTHORIZED)
		return super().create(request)

	def update(self, request, pk=None):
		if not request.user.is_superuser:
			return Response({
					'Unauthorized Call'
				}, status=status.HTTP_401_UNAUTHORIZED)
		return super().update(request, pk)

	def delete(self, request, pk=None):

		if not request.user.is_superuser:
			return Response({
					'Unauthorized Call'
				}, status=status.HTTP_401_UNAUTHORIZED)

		return super().delete(request, pk)


class DirectorViewSet(viewsets.ModelViewSet):

	queryset = Director.objects.all()
	filterset_class = DirectorsFilterSet
	serializer_class = DirectorSerializer

	def create(self, request):
		if not request.user.is_superuser:
			return Response({
					'Unauthorized Call'
				}, status=status.HTTP_401_UNAUTHORIZED)
		return super().create(request)

	def update(self, request, pk=None):
		if not request.user.is_superuser:
			return Response({
					'Unauthorized Call'
				}, status=status.HTTP_401_UNAUTHORIZED)
		return super().update(request, pk)

	def delete(self, request, pk=None):

		if not request.user.is_superuser:
			return Response({
					'Unauthorized Call'
				}, status=status.HTTP_401_UNAUTHORIZED)

		return super().delete(request, pk)


class MovieViewSet(viewsets.ModelViewSet):

	queryset = Movie.objects.all()
	filterset_class = MoviesFilterSet

	def get_serializer_class(self):
		if self.action in ['list', 'retrieve']:
			return ListMovieSerializer
		return MovieSerializer

	def create(self, request):
		if not request.user.is_superuser:
			return Response({
					'Unauthorized Call'
				}, status=status.HTTP_401_UNAUTHORIZED)
		return super().create(request)

	def update(self, request, pk=None):
		if not request.user.is_superuser:
			return Response({
					'Unauthorized Call'
				}, status=status.HTTP_401_UNAUTHORIZED)
		return super().update(request, pk)

	def delete(self, request, pk=None):

		if not request.user.is_superuser:
			return Response({
					'Unauthorized Call'
				}, status=status.HTTP_401_UNAUTHORIZED)

		return super().delete(request, pk)


	@action(detail=False, methods=['GET'])
	def top_rated_movies(self, request, *args, **kwargs):

		queryset = Movie.objects.filter(imdb_score__gte=8.0).order_by('-imdb_score')
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)
