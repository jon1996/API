from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CHOICES = (
	("1", "Entree"),
	("2", "Sortie")
)

class reportModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    Date = models.DateTimeField(auto_now_add=True)
    Description = models.TextField(max_length=200)
    mouvement = models.CharField(choices=CHOICES, max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name
