from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='article_images')
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title if self.title else f"Image for {self.article.title}"
