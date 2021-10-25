from django.urls import path
from . import views


urlpatterns = [
    path("todo", views.TodoView.as_view({"post": "post"}), name="todo"),
    path("todo/<int:pk>",
         views.TodoView.as_view({"get": "get_todo"}), name="todo"),
    path("todos", views.TodoView.as_view(
        {"get": "get_todo_list"}), name="todo"),
    path("todo/<int:pk>",
         views.TodoView.as_view({"put": "put"}), name="todo"),
    path("todo/<int:pk>",
         views.TodoView.as_view({"delete": "delete"}), name="todo"),
]
