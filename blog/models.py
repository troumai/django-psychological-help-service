from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    date = models.DateTimeField()
    anons = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='article_images/')
    full_text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.id}'