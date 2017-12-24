from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo import serializers, models

# Create your views here.

class ToDoList(APIView):

    def get(self, request, format=None):
        print('entered todolist get view')
        todo_lists = models.ToDoList.objects.all()

        serializer = serializers.ToDoList(todo_lists, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        print('post view')
        serializer = serializers.ToDoList(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_list_id, format=None):
        try:
            todo_list = models.ToDoList.objects.get(id=todo_list_id)
            todo_list.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.ToDoList.DoesNotExist:
            raise Http404

class ToDoListItem(APIView):

    def post(self, request, todo_list_id, format=None):
        try:
            todo_list = models.ToDoList.objects.get(id=todo_list_id)
            serializer = serializers.ToDoListItem(data=request.data)

            if serializer.is_valid():
                serializer.validated_data['todo_list_id'] = todo_list_id
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.ToDoList.DoesNotExist:
            raise Http404

    def delete(self, request, todo_list_item_id, format=None):
        try:
            item = models.ToDoListItem.objects.get(id=todo_list_item_id)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.ToDoListItem.DoesNotExist:
            return Http404
