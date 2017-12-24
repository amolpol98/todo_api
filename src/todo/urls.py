from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [
    url(r'^todo_lists/$', views.ToDoList.as_view()),
    url(r'^todo_lists/(?P<todo_list_id>[0-9]+)$', views.ToDoList.as_view()),
    url(r'^todo_lists/(?P<todo_list_id>[0-9]+)/items$', views.ToDoListItem.as_view()),
    url(r'^todo_lists/items/(?P<todo_list_item_id>[0-9]+)$', views.ToDoListItem.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
