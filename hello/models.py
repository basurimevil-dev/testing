from django.db import models


class Message(models.Model):
    """A simple model to store hello world messages."""
    text = models.CharField(max_length=255, default='Hello, World!')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
