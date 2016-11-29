from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from .models import Book, Category


class BookInventoryListView(ListView):
    """Implement view for rendering and querying books."""

    template_name = 'inventory/index.html'
    context_object_name = 'categories'
    queryset = Category.objects.order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.kwargs['category_num'] != '':
            context['books'] = Book.objects.filter(category=self.queryset[int(self.kwargs['category_num']) - 1])
        else:
            if 'q' in self.request.GET:
                query = Q(title__contains=self.request.GET['q']) | Q(category__name__iexact=self.request.GET['q'])
                context['books'] = Book.objects.filter(query)
            else:
                context['books'] = Book.objects.all()

        return context
