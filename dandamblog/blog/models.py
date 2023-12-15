from django.db import models
from django.contrib.auth.models import User

STATUS = [
    [0, 'Draft'],
    [1, 'Published']
]

class Category(models.Model):
    name = models.CharField(max_length=100, default='Category Name')
    slug = models.SlugField(unique=True, default='category-slug')
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    #TODO change name to create_date or create_time
    status = models.IntegerField(choices=STATUS, default=0)
    is_featured = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to='img/featured_images', default='img/featured_image.jpg')

    #relationships
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


