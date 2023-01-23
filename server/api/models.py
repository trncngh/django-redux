from django.db import models

# Create your models here.
class Project(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnail/images')
    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=50)
    description = models.TextField()
    demo = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title