from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from .models import Post
from django.urls import reverse

class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='password')
        
        cls.post = Post.objects.create(
            title='Test Post',
            body='This is a test post.',
            author=cls.user,
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.body, 'This is a test post.')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.get_absolute_url(), f'/post/{self.post.pk}/')
        
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get(f'/post/{self.post.pk}/')
        self.assertEqual(response.status_code, 200)
        
    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test post.')
        self.assertTemplateUsed(response, 'blog/post_list.html')
        
        
    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", args=[self.post.pk]))
        no_response = self.client.get('/post/9999/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'This is a test post.')
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        
    def test_post_createview(self):
        response = self.client.post(reverse("post_new"), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user.pk,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New title')
        self.assertEqual(Post.objects.last().body, 'New text')
        
    def test_post_updateview(self):
        response = self.client.post(reverse("post_edit", args=[self.post.pk]), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated title')
        self.assertEqual(self.post.body, 'Updated text')
        
    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())