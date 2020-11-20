from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']



class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=155)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name + " | " + self.subject[:100]
    