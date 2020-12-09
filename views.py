from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blog.models import Post
from django.db.models import Q
from django.utils import timezone

class SearchResultsView(ListView):
    model = Post
    template_name = 'query/results.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context.update({
            'top_hits': Post.objects.filter(published_date__lte=timezone.now()).order_by("-hit_count_generic__hits")[:10],
        })
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query) | Q(published_date__icontains=query)
        )
        return object_list