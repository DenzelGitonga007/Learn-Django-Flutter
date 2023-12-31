from django.db import models

# Create your models here.
# Notes
class Note(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50] # return 50 characters

    class Meta:
        ordering = ['-updated']
