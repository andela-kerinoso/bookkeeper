from django.conf.urls import url

from .views import BookInventoryListView

urlpatterns = [
    url(r'^(?P<category_num>)\d*/?$', BookInventoryListView.as_view(), name='bookpage'),
]
