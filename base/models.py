from django.db import models

class CachedVideo(models.Model):
    query = models.CharField(max_length=255, unique=True)   # step/topic searched
    videos = models.JSONField()  # store video list as JSON
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
