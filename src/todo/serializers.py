from rest_framework import serializers
from todo import models

class ToDoListItem(serializers.ModelSerializer):
    class Meta:
        model = models.ToDoListItem
        fields = ('id', 'todo_list_id', 'title', 'description')

class ToDoList(serializers.ModelSerializer):
    items = ToDoListItem(many=True)

    class Meta:
        model = models.ToDoList
        fields = ('id', 'title', 'items')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        todo_list = models.ToDoList.objects.create(**validated_data)
        for item_data in items_data:
            item_data['todo_list_id'] = todo_list.id
            models.ToDoListItem.objects.create(**item_data)

        return todo_list
