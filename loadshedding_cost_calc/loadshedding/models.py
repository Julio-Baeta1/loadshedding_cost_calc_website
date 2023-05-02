from django.db import models

class Duration(models.Model):
    duration_text = models.CharField(max_length=200)

    def __str__(self):
        return self.duration_text
