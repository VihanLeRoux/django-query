from django.urls import path

from .views import *

app_name = 'query'
urlpatterns = [
    path('', SearchResultsView.as_view(), name='query_results'),
]