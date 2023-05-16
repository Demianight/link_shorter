from django.db import models


class Link(models.Model):
    original_url = models.URLField()
    fake_url = models.URLField(null=True)
    slug = models.SlugField(null=True)
    name = models.CharField(max_length=32)

    class Meta:
        ordering = ('-id',)
