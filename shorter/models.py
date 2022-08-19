from django.db import models
from .utils import create_shortened_url


class URL(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    times_followed = models.IntegerField(default=0, blank=True)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def times_followed_incr(self):
        self.times_followed += 1

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)
