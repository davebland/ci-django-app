from django.test import TestCase
from django.shortcuts import get_object_or_404, HttpResponse
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    def test_add_says_hello(self):
        page = self.client.get("/hello/")
        self.assertEqual(page.status_code, 200)
        self.assertEqual(b'Hello World', page.content)
        
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")
        
    def test_get_add_item_page(self):
        page = self.client.get('/add')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
        
    def test_get_edit_item_page(self):
        item = Item(name='Create a Test')
        item.save()
        page = self.client.get('/edit/{0}'.format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
        
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get('/edit/123')
        self.assertEqual(page.status_code, 404)
        
    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name":"Create a Test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
        
    def test_post_edit_an_item(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id
        response = self.client.post("/edit/{0}".format(id), {"name":"A new name"})
        item = get_object_or_404(Item, pk=id)
        self.assertEqual("A new name", item.name)
        
    def test_toggle_status(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id
        response = self.client.post("/toggle/{0}".format(id))
        item = get_object_or_404(Item, pk=id)
        self.assertTrue(item.done)