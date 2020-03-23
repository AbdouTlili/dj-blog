from django.test import TestCase
from . models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse

class BlogPostTest(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret shshs'
        )

        self.post = Post.objects.create(
            author = self.user,
            title = 'testing title',
            body = ' this is a testttttttt  posssssst',
        )
        self.post.save()

    def test_string_representaion(self):
        post = Post(title = 'post Title')
        self.assertEqual(str(post),post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','testing title')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}',' this is a testttttttt  posssssst')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response ,' this is a testttttttt  posssssst')
        self.assertTemplateUsed(response ,'home.html')

    def test_post_detail_view(self):
        response = self.client.get('')
        no_response = self.client.get('/post/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, ' this is a testttttttt  posssssst')
        self.assertTemplateNotUsed(response, 'post_detail.html')