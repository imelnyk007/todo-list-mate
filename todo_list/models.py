from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-completed", "-created_at"]

    def __str__(self):
        return self.content
