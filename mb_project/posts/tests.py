from django.test import TestCase
from django.urls import reverse
from . import models

# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        models.Post.objects.create(text="just a test")

    def test_text_content(self):
        post = models.Post.objects.get(id=1)
        """
        We create a variable called post that represents the first id on
        our Post model. Remember that Django automatically sets this id for us. If we created
        another entry it would have an id of 2, the next one would be 3, and so on.
        """
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, "just a test")

"""
f strings which are a very cool addition to Python 3.6. They
let us put variables directly in our strings as long as the variables are surrounded by
brackets {}. Here we’re setting expected_object_name to be the string of the value in
post.text, which should be just a test.

use assertEqual to check that our newly created entry does in
fact match what we input at the top.

"""


class HomePageViewTest(TestCase):

    def setUp(self):
        models.Post.objects.create(text = "this is another test")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("posts:all"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("posts:all"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "posts/posts.html")
