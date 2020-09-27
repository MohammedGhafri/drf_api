from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Blog
# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='mohammed', password='M123456$')
        test_user.save()

        test_blog = Blog.objects.create(
            author = test_user,
            title = '401 is amazing',
            body = 'Django is super crazy'
        )
        test_blog.save() # Save the object to mock Database

    def test_blog_content(self):
        blog = Blog.objects.get(id=1)
        actual_author = str(blog.author)
        actual_title = str(blog.title)
        actual_body = str(blog.body)
        self.assertEqual(actual_author, 'mohammed')
        self.assertEqual(actual_title, '401 is amazing')
        self.assertEqual(actual_body, 'Django is super crazy')

    def test_response(self):
        URL = reverse('blog')
        response = self.client.get(URL)
        actual=response.status_code
        self.assertEquals(actual,200)

    

