from django.test import TestCase
from todo.models import ToDoList, ToDoListItem

class ToDoListTestCase(TestCase):

    def test_todo_list(self):
        ToDoList.objects.create(title='Test list')
        todo_list = ToDoList.objects.get(title='Test list')
        self.assertEqual(todo_list.title, 'Test list')
        todo_list.delete()
        try:
            retrieved_list = ToDoList.objects.get(title='Test list')
        except ToDoList.DoesNotExist:
            retrieved_list = None
        self.assertEqual(retrieved_list, None)

    def test_todo_list_items(self):
        todo_list = ToDoList.objects.create(title="Test")
        todo_list_item = ToDoListItem.objects.create(
            todo_list=todo_list,
            title="Test Item",
            description="This is a test todo list item")

        self.assertEqual(todo_list.items.count(), 1)
        self.assertEqual(todo_list.items.first(), todo_list_item)

        todo_list.delete()
        try:
            retrieved_item = ToDoListItem.objects.get(title="Test Item")
        except ToDoListItem.DoesNotExist:
            retrieved_item = None
        self.assertEqual(retrieved_item, None)
