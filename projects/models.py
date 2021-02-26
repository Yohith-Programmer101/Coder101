from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=500)
    blob = models.TextField()
    is_site = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
