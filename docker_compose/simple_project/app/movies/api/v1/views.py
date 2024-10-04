from typing import Any
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from movies.models import FilmWork


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ['get']

    def get_queryset(self):
        return FilmWork.objects.all()
    
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = 50
    
    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        
        title = self.request.GET.get('title', None)
        genres = self.request.GET.getlist('genres') 
        
        if title:
            queryset = queryset.filter(title__icontains=title)
        if genres:
            queryset = queryset.filter(genres__name__in=genres).distinct()  
        
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, self.paginate_by)
        context = {
            'count': paginator.count,
            "total_pages": paginator.num_pages,
            "next": page.next_page_number() if page.has_next() else None,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'results': list(queryset.values()),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    def get_context_data(self, **kwargs):
        film = self.get_object()
        context = {
            'id': film.id,
            'title': film.title,
            'description': film.description,
            'rating': film.rating,
        }
        return context
