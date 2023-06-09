from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.CharField(max_length=6, default="")
    upload = models.FileField(upload_to='blog/uploads/', null=True)

    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]