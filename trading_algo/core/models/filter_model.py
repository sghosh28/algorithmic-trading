from django.db import models


class FilterModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    scan_clause = models.CharField(max_length=200)
    post_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name
