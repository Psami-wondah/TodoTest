from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status


class TodoView(ViewSet):
    serializer_class = TodoSerializer

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        instance = Todo.objects.create(
            title=data["title"],
            content=data["content"],
            due_date=data["due_date"]

        )
        instance.save()
        return Response(data, status=status.HTTP_201_CREATED)

    def get_todo(self, request, pk=None):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(todo)
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def get_todo_list(self, request):
        try:
            instance = Todo.objects.all()
            serializer = TodoSerializer(instance, many=True)
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if request.method == "PUT":
            try:
                serializer = TodoSerializer(data=request.data)
                serializer.is_valid()
                data = serializer.data
                todo = Todo.objects.filter(pk=pk).update(title=data["title"],
                                                         content=data["content"],
                                                         due_date=data["due_date"])

                return Response({"new_data": data,
                                 "update": todo}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            todo = Todo.objects.filter(pk=pk).delete()
            return Response({"mesage": "delete_succesful",
                             "delete": todo}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
