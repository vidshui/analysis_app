from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    skin_category = models.CharField(max_length=10, blank=True)
    body_type = models.CharField(max_length=50, blank=True)

