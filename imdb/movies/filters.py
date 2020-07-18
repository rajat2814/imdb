from django_filters import rest_framework as filters

from .models import Movie, Genre, Director


class MoviesFilterSet(filters.FilterSet):
	name = filters.CharFilter(field_name='name', lookup_expr='icontains')

	class Meta:
		model = Movie
		fields = '__all__'

class GenresFilterSet(filters.FilterSet):
	name = filters.CharFilter(field_name='name', lookup_expr='icontains')

	class Meta:
		model = Genre
		fields = '__all__'


class DirectorsFilterSet(filters.FilterSet):
	name = filters.CharFilter(field_name='name', lookup_expr='icontains')

	class Meta:
		model = Director
		fields = '__all__'
