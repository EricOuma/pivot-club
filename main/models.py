from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = CloudinaryField('image', null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ResearchPaper(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



class Gallery(models.Model):
    caption = models.CharField(max_length=100)
    description = models.TextField()
    photo = CloudinaryField('image', null=True)

    def __str__(self):
        return self.caption