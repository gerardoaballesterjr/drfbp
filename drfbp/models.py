from django.db import models

from drfbp import utils


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    is_trashed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = utils.slug_generator(self)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
