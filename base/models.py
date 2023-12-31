from django.db import models


class Skills(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='portfolio', null=True)
    level = models.IntegerField()
    
    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    verification_link = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    website_link = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)
    skill = models.ManyToManyField(Skills)
    img = models.ImageField(upload_to='portfolio')

    def __str__(self):
        return self.title

