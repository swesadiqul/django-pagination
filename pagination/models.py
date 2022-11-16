from email.policy import default
from django.db import models

# Create your models here.
class Service(models.Model):
    img = models.ImageField(default="static/img/card/car-service.jpg", upload_to="pagination/media/img/card")
    title = models.CharField(max_length=225)
    description = models.TextField()

    def __str__(self):
        return self.title