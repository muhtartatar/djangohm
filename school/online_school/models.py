from django.db import models
import random


class User(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    course = models.CharField(max_length=100, choices=(('based', 'Based Course'), ('pro', 'Pro Course')))
    grade = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.grade = random.randint(0, 100)
        super().save(*args, **kwargs)
